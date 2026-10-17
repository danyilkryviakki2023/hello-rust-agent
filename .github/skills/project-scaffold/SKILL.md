---
name: project-scaffold
description: Створює мінімальний Hello World-проєкт на Rust: Cargo.toml, src/lib.rs, src/main.rs, README і .gitignore. Використовуй, коли в репозиторії ще немає вихідного коду або потрібно відновити початкову структуру.
---

# Skill: project-scaffold

## Коли застосовувати

- викликано command `create-project`;
- у репозиторії немає `Cargo.toml` або `src/main.rs`.

Не застосовуй, якщо проєкт уже створено й `check` проходить — тоді лише повідом
«нічого не змінено».

## Вхідні дані

| Параметр | За замовчуванням | Приклад |
|---|---|---|
| `language` | `Rust` | `Rust` |
| `project_name` | `hello` | `hello` |

Інші мови не підтримуються — зупинись і повідом про це.

## Результат (файли)

- `Cargo.toml` — пакет `{project_name}`, edition 2021, без залежностей;
- `src/lib.rs` — функції `greeting() -> String` («Hello, World!») та
  `add(a: i32, b: i32) -> i32`;
- `src/main.rs` — друкує привітання та `2 + 3 = 5`, використовуючи бібліотеку;
- `README.md` — лише якщо відсутній (ПІП, група, варіант, короткий опис, запуск);
- `.gitignore` — додай відсутні рядки `/target`, `/dist`, `.env`, `*.log`
  (не дублюй наявні).

## Кроки

1. Перевір наявність кожного файлу зі списку.
2. Створи лише відсутні; наявні — не переписуй.
3. Переконайся, що `src/main.rs` викликає `{project_name}::greeting()`.

## Перевірки

- усі файли зі списку існують;
- `cargo run` виводить рядок `Hello, World!`;
- `.gitignore` містить `/target` і `/dist` рівно по одному разу.

## Типова помилка

`cargo: command not found` → зупинись, попроси встановити Rust (rustup.rs),
нічого не створюй «наосліп».

## Приклад

Вхід: `language=Rust, project_name=hello`.
Очікуваний вивід `cargo run`:

```text
Hello, World!
2 + 3 = 5
```
