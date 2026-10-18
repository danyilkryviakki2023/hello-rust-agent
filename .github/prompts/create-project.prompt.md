---
description: "create-project — створює початковий Rust-проєкт Hello World (skill project-scaffold)"
agent: build-engineer
---

# Command: create-project

**Передумови:** встановлено Rust (`cargo --version` працює).

**Дії:** застосуй skill `project-scaffold` із параметрами `language=Rust`,
`project_name=hello`. Створи лише відсутні файли.

**Очікувані файли:** `Cargo.toml`, `src/lib.rs`, `src/main.rs`, `README.md`.

**Перевірка:** `cargo run` виводить `Hello, World!`.

**Повідомлення про помилку:** `create-project: <причина>`; якщо немає `cargo` —
попроси встановити Rust із https://rustup.rs і зупинись.

Повторний запуск не змінює вже створені файли.
