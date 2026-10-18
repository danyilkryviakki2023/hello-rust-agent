# Журнал взаємодії з AI

> Інструмент у цьому записі: Claude (Anthropic), чат, 18.10.2026. Записи про сесії з
> GitHub Copilot (запуск `/init` у VS Code) студент додає нижче власноруч — див. розділ
> «Шаблон для сесії Copilot».

## Сесія 1 — проєктування та створення репозиторію

| № | Запит | Важлива відповідь / рішення |
|---|---|---|
| 1 | Виконати лабораторну (варіант 4: Rust, Cargo, `cargo test`) за методичними вказівками: агент, 3 skills, 6 commands, проєкт, CI. | Запропоновано структуру з методички: manifest `build-engineer`, skills `project-scaffold` / `build-and-test` / `github-actions`, commands `git-init`, `create-project`, `create-build`, `create-actions`, `check`, оркестратор `init`. |
| 2 | Як назвати артефакти складання для Rust? | Прийнято: `target/` (Cargo) і `dist/` (результат `ci.sh`/`ci.bat`) — обидва в `.gitignore`. |
| 3 | Як зробити тест із назвою `BasicAddition` у Rust? | Прийнято `#[allow(non_snake_case)]` перед `fn BasicAddition()`, щоб ім'я збігалося з вимогою без попередження компілятора. |
| 4 | Що має робити `ci.yml`? | Прийнято: лише виклики `ci.sh` / `ci.bat` + завантаження `dist/`; уся логіка складання — у скриптах (вимога методички). |
| 5 | Як перевіряти репозиторій у `check`? | Створено `scripts/check_repo.py` (лише стандартна бібліотека Python): manifest, skills, commands, порядок у `init`, файли, `ci.yml`, `.gitignore`, секрети, документація. |

## Помилка AI та її виправлення

**Помилка.** Під час створення каталогів AI виконав `mkdir -p .github/skills/{a,b,c}` у
оболонці `/bin/sh`, яка не підтримує розкриття фігурних дужок. Замість трьох каталогів
створився один із літеральною назвою `{project-scaffold,build-and-test,github-actions}`,
і запис трьох файлів `SKILL.md` завершився помилкою `Directory nonexistent`.

**Як виявили.** За повідомленням у `stderr` та переліком файлів (`find .github -type f`):
у ньому не було жодного `SKILL.md`.

**Виправлення.** Каталоги створено окремими аргументами
(`mkdir -p .github/skills/project-scaffold .github/skills/build-and-test .github/skills/github-actions`),
файли записано повторно, помилковий каталог видалено (`rmdir`). Додатково `check`
перевіряє наявність кожного `SKILL.md`, тож така помилка не пройде непоміченою.

## Докази перевірки результату

| Перевірка | Результат |
|---|---|
| `python scripts/check_repo.py` на повному репозиторії | 58/58 PASS, код завершення 0 |
| `check` до створення документації | 54/58 → 57/58 PASS; FAIL чесно вказали відсутні файли |
| Навмисно зламана перевірка: з `ci.yml` прибрано `macos-latest` | `[FAIL] ci.yml: macos-latest`, код завершення 1 |
| Скрипт `setup_git.sh` на копії | створено гілки `master`, `develop`, `feature/hello-rust`, 7 комітів |
| `cargo build` / `cargo test` | **не запускались у середовищі AI** (Rust там не встановлено) — студент запускає локально та в GitHub Actions і додає результат до звіту |

## Шаблон для сесії Copilot

| 1 | `/init` у режимі Agent, агент `build-engineer`, гілка `develop` у чистій копії репозиторію | Copilot виконав 29 кроків за 1 хв 45 с, створив 8 файлів (+113 −8): Cargo.toml, src/lib.rs, src/main.rs, tests/basic_addition.rs, ci.sh, ci.bat, ci.yml, docs/ai-log.md. Усі п'ять команд завершились зі статусом OK. |
| 2 | Перевірка результату після /init | У терміналі: `git status` показує лише нові файли, наявні файли агента з develop не змінено; `cargo test` — BasicAddition ok, 2 passed; `check_repo.py` — 58/58 PASS; `ci.bat` пройшов повністю. |
| 3 | Обмеження середовища | `bash ci.sh` у Copilot не запустився: на комп'ютері немає дистрибутива WSL. Windows-скрипт ci.bat пройшов повністю; Linux і macOS перевіряє GitHub Actions. |
| 4 | Спостереження про агента | Агент сам створив `docs/ai-log.md`: у гілці develop цього файлу не було, жоден skill його не описує, а `check_repo.py` його вимагає. Висновок: зелений check не доводить змістовної правильності, тому вміст файлів, створених агентом, треба читати. |
