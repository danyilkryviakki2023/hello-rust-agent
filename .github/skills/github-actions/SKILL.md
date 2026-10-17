---
name: github-actions
description: Створює .github/workflows/ci.yml з однією job і matrix для ubuntu-latest, windows-latest, macos-latest; workflow лише викликає ci.sh / ci.bat. Використовуй для command create-actions.
---

# Skill: github-actions

## Коли застосовувати

- викликано command `create-actions`;
- немає `.github/workflows/ci.yml` або в ньому бракує однієї з трьох ОС.

## Вхідні дані

- наявні `ci.sh` та `ci.bat` (результат skill `build-and-test`);
- гілки, для яких запускається CI: `develop`, `master`.

## Результат (файли)

`.github/workflows/ci.yml`:

- тригери: `push` і `pull_request` для `develop` та `master` (+ `workflow_dispatch`);
- одна job `build-and-test`, `strategy.matrix.os: [ubuntu-latest, windows-latest, macos-latest]`,
  `fail-fast: false`;
- кроки: `actions/checkout@v4`; `bash ci.sh` (Linux/macOS, `if: runner.os != 'Windows'`);
  `ci.bat` з `shell: cmd` (Windows); `actions/upload-artifact@v4` для `dist/`;
- **жодних** секретів, токенів, паролів у файлі; жодної логіки складання в YAML.

## Кроки

1. Якщо файл існує — порівняй із вимогами й виправ лише відмінності.
2. Якщо відсутній — створи повністю.
3. Перевір відступи (YAML чутливий до пробілів, табуляція заборонена).

## Перевірки

- файл успішно парситься як YAML (якщо доступний `python -c "import yaml"`);
- у файлі є рівно три ОС із матриці та виклики `ci.sh` і `ci.bat`;
- у файлі немає рядків `secrets.`, `token`, `password`.

## Типова помилка

`mapping values are not allowed here` / помилка відступів → виправ відступи на
2 пробіли, без табів, і перевір ще раз. Не «вирішуй» помилку видаленням ОС із матриці.

## Приклад

Вхід: `ci.sh`, `ci.bat` існують. Результат: job із трьома запусками
(`ubuntu-latest`, `windows-latest`, `macos-latest`), кожен завантажує артефакт
`hello-<os>`.
