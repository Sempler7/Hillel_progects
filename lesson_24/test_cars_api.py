import pytest
import requests
import logging
from requests.auth import HTTPBasicAuth

BASE_URL = "http://127.0.0.1:8080"

@pytest.fixture(scope="class")
def session():
    s = requests.Session()
    auth_url = f"{BASE_URL}/auth"
    auth = HTTPBasicAuth("test_user", "test_pass")

    logging.info("🔐 Аутентифікація через /auth")
    response = s.post(auth_url, auth=auth)
    assert response.status_code == 200, "❌ Аутентифікація не вдалася"

    token = response.json().get("access_token")
    assert token, "❌ Токен не отримано"

    s.headers.update({"Authorization": f"Bearer {token}"})
    logging.info("✅ Токен додано до заголовків")
    return s

@pytest.mark.parametrize("sort_by,limit", [
    ("price", 3),
    ("year", 5),
    ("engine_volume", 2),
    ("brand", 4),
    ("price", 10),
    ("year", 1),
    ("engine_volume", 7),
])
def test_search_cars(session, sort_by, limit):
    url = f"{BASE_URL}/cars"
    params = {"sort_by": sort_by, "limit": limit}

    logging.info(f"📦 Запит: sort_by={sort_by}, limit={limit}")
    response = session.get(url, params=params)

    assert response.status_code == 200, f"❌ Статус код: {response.status_code}"
    cars = response.json()
    logging.info(f"✅ Отримано {len(cars)} записів")

    assert isinstance(cars, list), "❌ Відповідь не є списком"
    assert len(cars) <= limit, f"❌ Отримано більше записів, ніж очікувалось: {len(cars)} > {limit}"

    # Перевірка сортування
    values = [car[sort_by] for car in cars]
    assert values == sorted(values), f"❌ Дані не відсортовані по '{sort_by}'"
