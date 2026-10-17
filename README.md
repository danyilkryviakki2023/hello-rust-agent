# Hello World (Rust) + AI-агент Build Engineer

Лабораторна робота №1 «Проєктування AI-агента для автоматизації розробки та CI/CD».

| | |
|---|---|
| ПІБ | _[вкажіть]_ |
| Група | _[вкажіть]_ |
| Варіант | **4** — Rust, Cargo, `cargo test` |
| GitHub | _[посилання на профіль]_ |

## Що це

Кросплатформний застосунок Hello World мовою Rust і **AI-агент** (GitHub Copilot
custom agent + skills + prompt-команди), який створює, збирає, тестує та налаштовує
CI для цього проєкту на Windows, Linux і macOS.

## Швидкий старт

**Запустити зібраний проєкт** (потрібен [Rust](https://rustup.rs)):

```bash
cargo run
# Hello, World!
# 2 + 3 = 5
```

**Скласти, протестувати, упакувати** (як у CI):

```bash
bash ci.sh      # Linux / macOS / Git Bash
ci.bat          # Windows (cmd)
```

**Запустити AI-агента:** VS Code → Copilot Chat → режим *Agent* → обрати
`build-engineer` → ввести `/init`. Докладно — у [docs/usage.md](docs/usage.md).

**Перевірити репозиторій:** `python scripts/check_repo.py`

## Документація

- [docs/architecture.md](docs/architecture.md) — архітектура агента, skills, commands
- [docs/usage.md](docs/usage.md) — точні команди запуску
- [docs/ai-log.md](docs/ai-log.md) — журнал взаємодії з AI
