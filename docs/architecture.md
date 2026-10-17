# Архітектура AI-агента

## Яку проблему вирішує агент

Ручне створення проєкту, системи складання, тестів і CI — повторювана робота, де
легко забути крок (тест, одну з ОС, `.gitignore`). Агент `build-engineer` виконує
її за зафіксованим процесом і сам перевіряє результат командою `check`.

## Компоненти

| Компонент | Файл | Роль |
|---|---|---|
| Agent manifest | `.github/agents/build-engineer.agent.md` | роль, обмеження, заборони, критерії завершення |
| Skill `project-scaffold` | `.github/skills/project-scaffold/SKILL.md` | створення Hello World-проєкту |
| Skill `build-and-test` | `.github/skills/build-and-test/SKILL.md` | тест `BasicAddition`, `ci.sh`, `ci.bat` |
| Skill `github-actions` | `.github/skills/github-actions/SKILL.md` | `ci.yml` з matrix із 3 ОС |
| Command `git-init` | `.github/prompts/git-init.prompt.md` | перевірка Git, `.gitignore`, статус |
| Command `create-project` | `.github/prompts/create-project.prompt.md` | викликає `project-scaffold` |
| Command `create-build` | `.github/prompts/create-build.prompt.md` | викликає `build-and-test` |
| Command `create-actions` | `.github/prompts/create-actions.prompt.md` | викликає `github-actions` |
| Command `check` | `.github/prompts/check.prompt.md` | лише перевірка (+ `scripts/check_repo.py`) |
| Orchestrator `init` | `.github/prompts/init.prompt.md` | запускає п'ять команд по черзі |

## Як вони взаємодіють

```text
/init  (orchestrator)
  ├─ git-init        ──► .gitignore, статус Git
  ├─ create-project  ──► skill project-scaffold ──► Cargo.toml, src/, README.md
  ├─ create-build    ──► skill build-and-test   ──► tests/, ci.sh, ci.bat
  ├─ create-actions  ──► skill github-actions   ──► .github/workflows/ci.yml
  └─ check           ──► scripts/check_repo.py + cargo build + cargo test
```

Manifest діє як «конституція»: його правила (ідемпотентність, заборонені дії,
критерії завершення) поширюються на всі skills і commands.

## Дані між етапами

Дані передаються **через файли репозиторію**: `create-build` очікує `Cargo.toml` та
`src/lib.rs` з попереднього кроку; `create-actions` очікує `ci.sh` та `ci.bat`;
`check` читає все створене. Жодного прихованого стану.

## Обробка помилок оркестратором

- Помилка будь-якого кроку → `init` **зупиняється**, показує повідомлення команди
  та що виправити; наступні кроки не запускаються.
- Успіх оголошується лише після `check` з кодом 0.
- Повторний запуск безпечний: команди створюють лише відсутні файли й не дублюють рядки.

## Відповідність файлів ролям (GitHub Copilot у VS Code)

Використано стандартні для Copilot каталоги: custom agents — `.github/agents/*.agent.md`;
prompt-файли (slash-команди) — `.github/prompts/*.prompt.md`; agent skills —
`.github/skills/<name>/SKILL.md`. Окремої відповідності не потрібно.

## Обмеження агента

Підтримує лише Rust + Cargo; не налаштовує GitHub (гілки, захист), не публікує
пакети, не вміє виправляти довільні помилки компіляції без участі людини. Результат
роботи AI завжди переглядає й пояснює студент.
