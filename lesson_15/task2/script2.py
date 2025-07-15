import json
import logging
import os

# 🔧 Налаштування логера
logging.basicConfig(
    filename='json__erenkov.log',
    level=logging.ERROR,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# 📂 Список JSON-файлів
json_files = ['localizations_en.json', 'localizations_ru.json', 'login.json', 'swagger.json']

# ✅ Перевірка кожного файлу
for file_name in json_files:
    try:
        with open(file_name, 'r', encoding='utf-8') as f:
            json.load(f)
        print(f"✅ {file_name} — валідний JSON")
    except Exception as e:
        logging.error(f"{file_name} — невалідний JSON: {e}")
        print(f"❌ {file_name} — невалідний JSON. Деталі записані в лог.")