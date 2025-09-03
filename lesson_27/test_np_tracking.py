# test_np_tracking.py
import pytest
from selenium import webdriver
from np_tracking_page import NPTrackingPage

@pytest.mark.parametrize("tracking_number,expected_status", [
    ("20451231601172", "Отримана"),
])
def test_np_tracking_status(tracking_number, expected_status):
    driver = webdriver.Chrome()
    page = NPTrackingPage(driver)

    try:
        page.open()
        page.enter_tracking_number(tracking_number)
        status = page.get_status()

        assert status == expected_status, f"Очікував: '{expected_status}', отримав: '{status}'"
    finally:
        driver.quit()