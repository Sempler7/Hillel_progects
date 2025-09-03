from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoAlertPresentException, TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import logging
import time

# Налаштування логування
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Ініціалізація драйвера
driver = webdriver.Chrome()
driver.get("http://localhost:8000/dz.html")

def verify_frame(frame_id, input_id, secret_text):
    try:
        logging.info(f"Переходимо у фрейм: {frame_id}")
        driver.switch_to.default_content()
        driver.switch_to.frame(frame_id)

        input_elem = driver.find_element(By.ID, input_id)
        input_elem.clear()
        input_elem.send_keys(secret_text)

        button = driver.find_element(By.TAG_NAME, "button")
        button.click()

        # Очікуємо появу alert
        WebDriverWait(driver, 5).until(EC.alert_is_present())
        alert = driver.switch_to.alert
        alert_text = alert.text
        logging.info(f"Отримано alert: {alert_text}")

        if "успішно" in alert_text:
            logging.info(f"✅ Верифікація у {frame_id} пройдена")
        else:
            logging.warning(f"❌ Верифікація у {frame_id} НЕ пройдена")

        alert.accept()
        logging.info("Alert закрито")

    except TimeoutException:
        logging.error("⏰ Alert не з'явився вчасно")
    except NoAlertPresentException:
        logging.error("🚫 Alert не знайдено")
    except Exception as e:
        logging.error(f"⚠️ Помилка: {e}")

# Верифікація у двох фреймах
verify_frame("frame1", "input1", "Frame1_Secret")
verify_frame("frame2", "input2", "Frame2_Secret")

# Завершення
time.sleep(2)
driver.quit()