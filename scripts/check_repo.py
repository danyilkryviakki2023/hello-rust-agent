#!/usr/bin/env python3
"""Перевірка репозиторію (command `check`). Нічого не змінює.

Запуск:  python scripts/check_repo.py      (код 0 = усе гаразд, 1 = є FAIL)
Лише стандартна бібліотека Python 3.
"""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
results = []


def check(name, ok, hint=""):
    results.append((name, bool(ok), hint))


def read(rel):
    p = ROOT / rel
    return p.read_text(encoding="utf-8") if p.is_file() else ""


# 1. Manifest агента
agent = read(".github/agents/build-engineer.agent.md")
check("manifest: файл існує", agent, ".github/agents/build-engineer.agent.md")
for title in ("Роль", "Заборонені дії", "Критерії успішного завершення"):
    check(f"manifest: розділ «{title}»", re.search(rf"^##\s+{title}", agent, re.M),
          f"додайте розділ «{title}»")

# 2. Skills
for skill in ("project-scaffold", "build-and-test", "github-actions"):
    text = read(f".github/skills/{skill}/SKILL.md")
    check(f"skill {skill}: файл існує", text, f".github/skills/{skill}/SKILL.md")
    for title in ("Коли застосовувати", "Вхідні дані", "Результат", "Перевірки", "Типова помилка"):
        check(f"skill {skill}: розділ «{title}»",
              re.search(rf"^##\s+{title}", text, re.M), f"додайте розділ «{title}»")

# 3. Commands + порядок викликів в init
commands = ("git-init", "create-project", "create-build", "create-actions", "check", "init")
for c in commands:
    t = read(f".github/prompts/{c}.prompt.md")
    check(f"command {c}: файл і description", t.startswith("---") and "description:" in t,
          f".github/prompts/{c}.prompt.md")
init = read(".github/prompts/init.prompt.md")
pos = [init.find(f"{c}.prompt.md") for c in commands[:5]]
check("init: викликає 5 команд у правильному порядку",
      all(p >= 0 for p in pos) and pos == sorted(pos),
      "порядок: git-init, create-project, create-build, create-actions, check")

# 4. Проєкт
for f in ("Cargo.toml", "src/lib.rs", "src/main.rs", "tests/basic_addition.rs",
          "ci.sh", "ci.bat", "README.md"):
    check(f"проєкт: {f}", (ROOT / f).is_file(), f"створіть {f}")
check("тест називається BasicAddition", "fn BasicAddition" in read("tests/basic_addition.rs"),
      "у tests/basic_addition.rs має бути fn BasicAddition")
check("ci.sh: set -euo pipefail", "set -euo pipefail" in read("ci.sh"))
check("ci.bat: перевірка errorlevel", "errorlevel" in read("ci.bat"))

# 5. Workflow
ci = read(".github/workflows/ci.yml")
check("ci.yml існує", ci, ".github/workflows/ci.yml")
for os_name in ("ubuntu-latest", "windows-latest", "macos-latest"):
    check(f"ci.yml: {os_name}", os_name in ci, f"додайте {os_name} до matrix")
check("ci.yml: matrix", "matrix:" in ci)
check("ci.yml: push і pull_request", "push:" in ci and "pull_request:" in ci)
check("ci.yml: гілки develop та master", "develop" in ci and "master" in ci)
check("ci.yml: викликає ci.sh та ci.bat", "ci.sh" in ci and "ci.bat" in ci)
check("ci.yml: без секретів", not re.search(r"secrets\.|password|token", ci, re.I),
      "приберіть секрети з workflow")
check("ci.yml: без табуляції", "\t" not in ci, "замініть таби на пробіли")
try:
    import yaml  # необов'язково

    try:
        yaml.safe_load(ci)
        check("ci.yml: валідний YAML", True)
    except Exception as e:  # noqa: BLE001
        check("ci.yml: валідний YAML", False, str(e).splitlines()[0])
except ImportError:
    pass  # PyYAML не встановлено — пропускаємо парсинг

# 6. .gitignore
gi = read(".gitignore").splitlines()
check(".gitignore: /target", "/target" in gi)
check(".gitignore: /dist", "/dist" in gi)
check(".gitignore: .env", ".env" in gi)

# 7. Git: build-каталоги та секрети
SECRET_RE = re.compile(r"ghp_[A-Za-z0-9]{36}|AKIA[0-9A-Z]{16}|-----BEGIN [A-Z ]*PRIVATE KEY-----")
try:
    out = subprocess.run(["git", "ls-files"], cwd=ROOT, capture_output=True, text=True, check=True)
    tracked = [l for l in out.stdout.splitlines() if l]
    in_git = True
except Exception:  # noqa: BLE001
    tracked = [str(p.relative_to(ROOT)) for p in ROOT.rglob("*")
               if p.is_file() and not any(x in p.parts for x in ("target", "dist", ".git"))]
    in_git = False
bad = [f for f in tracked if f.split("/")[0] in ("target", "dist") or f.startswith(".env")]
check("git: немає target/, dist/, .env" + ("" if in_git else " (git-репозиторій не знайдено)"),
      not bad, ", ".join(bad))
leaks = []
for f in tracked:
    p = ROOT / f
    if p.is_file():
        try:
            if SECRET_RE.search(p.read_text(encoding="utf-8")):
                leaks.append(f)
        except (UnicodeDecodeError, OSError):
            pass
check("git: у файлах немає токенів / приватних ключів", not leaks, ", ".join(leaks))

# 8. Документація
for f in ("docs/architecture.md", "docs/usage.md", "docs/ai-log.md"):
    check(f"документація: {f}", (ROOT / f).is_file(), f"створіть {f}")

# Підсумок
width = max(len(n) for n, _, _ in results)
failed = 0
for name, ok, hint in results:
    print(f"[{'PASS' if ok else 'FAIL'}] {name.ljust(width)}" + ("" if ok or not hint else f"  <- {hint}"))
    failed += (not ok)
print(f"\nПідсумок: {len(results) - failed}/{len(results)} PASS" + ("" if not failed else f", {failed} FAIL"))
sys.exit(1 if failed else 0)
