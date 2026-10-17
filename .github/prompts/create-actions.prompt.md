---
description: "create-actions — створює CI workflow для Windows, Linux і macOS (skill github-actions)"
agent: build-engineer
---

# Command: create-actions

**Передумови:** існують `ci.sh` та `ci.bat` (виконано `create-build`).

**Дії:** застосуй skill `github-actions`: створи або виправ
`.github/workflows/ci.yml` (одна job, matrix з трьох ОС, лише виклики скриптів).

**Очікувані файли:** `.github/workflows/ci.yml`.

**Перевірка:** файл парситься як YAML; містить `ubuntu-latest`, `windows-latest`,
`macos-latest`, `ci.sh`, `ci.bat`; не містить секретів.

**Повідомлення про помилку:** `create-actions: <причина>`; для помилок YAML
вкажи рядок і виправ відступи (2 пробіли, без табів).

Повторний запуск не дублює кроки й не ламає наявний workflow.
