#Побудова образу  -  docker build -t students-system .
#Запуск контейнеру - docker run --rm students-system

# Вихідний образ з Python
FROM python:3.11-slim

# Робоча директорія всередині контейнера
WORKDIR /app

# Копіюємо скрипт у контейнер
COPY students_system.py ./students_system.py

# Встановлюємо залежності
RUN pip install sqlalchemy

# Команда запуску
CMD ["python", "students_system.py"]

# Додатково до Python
RUN pip install pytest allure-pytest

# Копіюємо тести
COPY tests/ ./tests/

# Запускаємо тести
CMD ["pytest", "--alluredir=allure-results"]