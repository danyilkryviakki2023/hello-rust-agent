<<<<<<< HEAD
pub fn greeting() -> String {
    "Hello, World!".to_string()
}

pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
=======
//! Бібліотека проєкту Hello World (лабораторна робота №1, варіант 4).

/// Повертає стандартне привітання.
pub fn greeting() -> String {
    String::from("Hello, World!")
}

/// Додає два цілих числа.
pub fn add(a: i32, b: i32) -> i32 {
    a + b
}
>>>>>>> origin/develop
