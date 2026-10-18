# Інструкція запуску

## 0. Передумови

- Git, [Rust](https://rustup.rs) (`cargo --version`), Python 3;
- VS Code + розширення **GitHub Copilot** і **Copilot Chat**, вхід під акаунтом із
  активним GitHub Copilot Student.

## 1. Запуск AI-агента

1. Відкрити каталог репозиторію у VS Code.
2. Відкрити Copilot Chat (`Ctrl+Alt+I` / `Cmd+Ctrl+I`), перемкнути режим на **Agent**
   і вибрати агента **build-engineer** у списку агентів.
3. Ввести slash-команду повного сценарію:

   ```text
   /init
   ```

   Окремі операції: `/git-init`, `/create-project`, `/create-build`,
   `/create-actions`, `/check`.
4. Якщо агента, skills чи команд не видно — перевірте, що файли лежать у
   `.github/agents`, `.github/prompts`, `.github/skills`; для skills у налаштуваннях VS Code
   (пошук «agent skills») має бути увімкнена їх підтримка; перезавантажте вікно VS Code.
5. Переглянути кожну зміну, яку пропонує агент, і лише потім приймати (Keep).

## 2. Локальна перевірка

```bash
python scripts/check_repo.py     # структура, manifest, skills, commands, CI, .gitignore
cargo build --release            # складання
cargo test                       # має бути: test BasicAddition ... ok
```

Те саме одним кроком, як у CI:

```bash
bash ci.sh        # Linux / macOS / Git Bash
ci.bat            # Windows cmd
```

## 3. Запуск зібраного проєкту

```bash
cargo run                  # через Cargo
./dist/hello               # Linux / macOS після ci.sh
dist\hello.exe             # Windows після ci.bat
```

Очікуваний вивід:

```text
Hello, World!
2 + 3 = 5
```

## 4. Git-процес

```bash
git switch develop                  # агент з інструкціями
git switch feature/hello-rust       # повний проєкт, створений агентом
git push -u origin master develop feature/hello-rust
```

Потім на GitHub: Pull request `feature/hello-rust` → `develop` з назвою
`lab1/finish`; після успішного CI — злиття у `master`.
