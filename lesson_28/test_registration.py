import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def test_user_registration(register_user, driver):
    email = f"test_{int(time.time())}@mail.com"
    register_user("Test", "User", email, "Password123!")

    # Чекаємо появу логотипу
    logo = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, "a.header_logo"))
    )
    assert logo.is_displayed()