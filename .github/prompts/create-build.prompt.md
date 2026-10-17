---
description: "create-build — створює тест BasicAddition та скрипти складання ci.sh / ci.bat (skill build-and-test)"
agent: build-engineer
---

# Command: create-build

**Передумови:** існують `Cargo.toml` і `src/lib.rs` (виконано `create-project`).

**Дії:** застосуй skill `build-and-test`: створи відсутні `tests/basic_addition.rs`,
`ci.sh`, `ci.bat`; потім виконай `cargo build --release` і `cargo test`.

**Очікувані файли:** `tests/basic_addition.rs`, `ci.sh`, `ci.bat`.

**Перевірка:** у виводі `cargo test` є `BasicAddition ... ok`; після `bash ci.sh`
існує `dist/hello`.

**Повідомлення про помилку:** `create-build: <команда> завершилась з помилкою:
<останні рядки виводу>`. Не змінюй очікувані значення тестів, щоб «позеленіти».

Повторний запуск не перезаписує наявні файли.
