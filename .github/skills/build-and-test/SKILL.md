---
name: build-and-test
description: Налаштовує складання та юніт-тестування Rust-проєкту — тест BasicAddition і скрипти ci.sh / ci.bat, що збирають, тестують та пакують виконуваний файл у dist/. Використовуй для command create-build.
---

# Skill: build-and-test

## Коли застосовувати

- викликано command `create-build`;
- немає `tests/basic_addition.rs`, `ci.sh` або `ci.bat`.

## Вхідні дані

- наявний проєкт зі skill `project-scaffold` (`Cargo.toml`, `src/lib.rs`);
- ім'я пакета (`hello`).

## Результат (файли)

- `tests/basic_addition.rs` — інтеграційний тест:
  - `BasicAddition` перевіряє `add(2, 3) == 5`, `add(-1, 1) == 0`, `add(0, 0) == 0`
    (атрибут `#[allow(non_snake_case)]`, щоб ім'я тесту було точно `BasicAddition`);
  - `greeting_is_hello_world` перевіряє текст привітання;
- `ci.sh` — `set -euo pipefail`; `cargo build --release`; `cargo test --release`;
  копіювання `target/release/hello[.exe]` у `dist/`; запуск і перевірка виводу;
- `ci.bat` — те саме для Windows, після кожної команди `if errorlevel 1 exit /b 1`.

## Кроки

1. Створи відсутні файли; наявні не перезаписуй.
2. Зроби `ci.sh` виконуваним (`chmod +x`), якщо ОС це підтримує.
3. Запусти `cargo build --release` і `cargo test`.

## Перевірки

- `cargo test` показує `test BasicAddition ... ok`;
- після `bash ci.sh` існує `dist/hello` (або `dist\hello.exe` після `ci.bat`);
- `dist/` і `target/` не відстежуються Git (`git status` їх не показує).

## Типова помилка

Тест падає (`assertion left == right failed`) → знайди причину в `src/lib.rs`,
виправ код. **Забороняється** змінювати очікуване значення, щоб тест пройшов.
Якщо помилка в самому тесті — поясни це у звіті.

## Приклад

Вхід: проєкт `hello`. Очікувано: `cargo test` → `2 passed; 0 failed`,
у `dist/` лежить виконуваний файл.
