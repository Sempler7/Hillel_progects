import requests
import os
import logging

# 🔧 Настройки
SERVER_URL = 'http://127.0.0.1:8080'
UPLOAD_ENDPOINT = f'{SERVER_URL}/upload'
IMAGE_ENDPOINT = f'{SERVER_URL}/image'
DELETE_ENDPOINT = f'{SERVER_URL}/delete'
IMAGE_PATH = 'example.jpg'  # путь к локальному изображению

# 📋 Настройка логгера
logging.basicConfig(level=logging.INFO, format='%(levelname)s:%(message)s')


def upload_image(image_path: str) -> str:
    """📤 Загружает изображение на сервер"""
    if not os.path.exists(image_path):
        logging.error(f'Файл не найден: {image_path}')
        return ''

    with open(image_path, 'rb') as image_file:
        files = {'image': image_file}
        response = requests.post(UPLOAD_ENDPOINT, files=files)

    if response.status_code == 201:
        image_url = response.json()['image_url']
        logging.info(f'Изображение загружено: {image_url}')
        return os.path.basename(image_path)
    else:
        logging.error(f'Ошибка при загрузке: {response.text}')
        return ''


def get_image(filename: str, as_url=True) -> None:
    """📥 Получает изображение: либо URL, либо сам файл"""
    headers = {'Content-Type': 'text' if as_url else 'image'}
    response = requests.get(f'{IMAGE_ENDPOINT}/{filename}', headers=headers)

    if response.status_code == 200:
        if as_url:
            logging.info(f"Ссылка на изображение: {response.json()['image_url']}")
        else:
            output_path = f'downloaded_{filename}'
            with open(output_path, 'wb') as f:
                f.write(response.content)
            logging.info(f'Изображение скачано: {output_path}')
    else:
        logging.warning(f'Ошибка при получении: {response.text}')


def delete_image(filename: str) -> None:
    """🗑️ Удаляет изображение на сервере"""
    response = requests.delete(f'{DELETE_ENDPOINT}/{filename}')
    if response.status_code == 200:
        logging.info(f"Удалено: {response.json()['message']}")
    else:
        logging.warning(f'Ошибка удаления: {response.text}')


# 🧪 Последовательное выполнение
if __name__ == '__main__':
    filename = upload_image(IMAGE_PATH)
    if filename:
        get_image(filename, as_url=True)
        get_image(filename, as_url=False)
        delete_image(filename)