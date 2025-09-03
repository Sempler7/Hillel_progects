from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging

class NPTrackingPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://tracking.novaposhta.ua/#/uk"
        self.input_locator = (By.ID, "en")  # Оновлений ID поля вводу
        self.status_locator = (By.CLASS_NAME, "header__status-text")

    def open(self):
        logging.info("Відкриваємо сторінку Нової Пошти")
        self.driver.get(self.url)

    def enter_tracking_number(self, number):
        try:
            logging.info(f"Вводимо номер накладної: {number}")
            input_elem = WebDriverWait(self.driver, 15).until(
                EC.visibility_of_element_located(self.input_locator)
            )
            input_elem.clear()
            input_elem.send_keys(number)
            input_elem.submit()  # Альтернатива: input_elem.send_keys(Keys.ENTER)
        except Exception as e:
            logging.error(f"Помилка при введенні номера: {e}")
            raise

    def get_status(self):
        try:
            logging.info("Очікуємо статус посилки...")
            status_elem = WebDriverWait(self.driver, 20).until(
                EC.visibility_of_element_located(self.status_locator)
            )
            status_text = status_elem.text.strip()
            logging.info(f"Статус отримано: {status_text}")
            return status_text
        except Exception as e:
            logging.error(f"Не вдалося отримати статус: {e}")
            raise