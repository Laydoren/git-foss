# Password Manager

Это программа для генерации криптографически стойких паролей и управления ими. Пароли хранятся локально в JSON-файле

Сам проект демонстрирует организацию Python-окружения, статический анализ типов, проверку зависимостей и автоматизацию через Makefile

---

## Быстрый старт
 
```bash
make install
make run
```

## Makefile-таргеты

`make install` - Создаёт `.venv` и устанавливает зависимости  
`make run` - Запускает интерактивный CLI  
`make typecheck` - Запускает `mypy` - статическую проверку типов  
`make format` - Форматирует код через `black`  
`make lint` - Проверяет форматирование без изменений  
`make test` - Запускает тесты через `pytest`  
`make check-requirements` - Сравнивает импорты в `src/` с `requirements.txt`  
`make check` - Запускает `lint`, `typecheck`, `test`, `check-requirements`  
`make run-full` - Сначала запускает `install`, потом `check` и в конце `run`  

## Запуск без Make

```bash
# 1. Создать окружение
python -m venv .venv

# 2. Установить зависимости
.venv/bin/python -m pip install --upgrade pip
.venv/bin/python -m pip install -r requirements.txt

# 3. Запустить приложение
.venv/bin/python -m src.main

# 4. Проверка типов
.venv/bin/python -m mypy src tests

# 5. Форматирование
.venv/bin/python -m black src tests scripts

# 6. Линтер (без изменений кода)
.venv/bin/python -m black --check src tests scripts

# 7. Тесты
.venv/bin/python -m pytest

# 8. Проверка зависимостей
.venv/bin/python scripts/check_requirements.py
```

---

## Логика работы

### Генератор паролей (`src/generator.py`)

Использует модуль `secrets` вместо `random`. Поддерживает настройку длины, включения/исключения цифр и спецсимволов. Функция `check_strength` оценивает пароль по пяти критериям (длина ≥ 12, строчные, заглавные, цифры, спецсимволы) и возвращает `"weak"` / `"medium"` / `"strong"`

### Хранилище (`src/storage.py`)

Записи хранятся в `data/vault.json`. Файл создаётся автоматически при первом сохранении. Каждая запись содержит: `service`, `username`, `password`, `created_at`

### Интерактивное меню (`src/main.py`)

Интерактивное меню с пятью действиями:
1. Сгенерировать и сохранить пароль
2. Добавить пароль вручную
3. Показать все записи
4. Получить пароль для сервиса
5. Удалить запись

---

## Виртуальное окружение

Окружение создаётся в `.venv/` внутри проекта. В Makefile все вызовы идут через явный путь `.venv/bin/python`, а не через `source .venv/bin/activate`, поскольку каждая строка таргета Make выполняется в отдельном shell-процессе и активация не сохраняется между строками

---

## Проверка зависимостей (`scripts/check_requirements.py`)

`scripts/check_requirements.py` вызывает `pip-check-reqs` - инструмент, который анализирует импорты в `src/` и сравнивает их с `requirements.txt`

---

## Тесты

Тесты покрывают:
- генерацию пароля заданной длины и с разными флагами
- оценку стойкости пароля
- `add_entry`, `get_entry`, `delete_entry`, `list_entries` через изолированное временное хранилище (`tmp_path`)
