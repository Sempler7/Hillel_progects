import pytest
from selenium import webdriver
from registration_page import RegistrationPage

@pytest.fixture(scope="session")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    driver.get("https://guest:welcome2qauto@qauto2.forstudy.space")
    yield driver
    driver.quit()

@pytest.fixture
def registration_page(driver):
    return RegistrationPage(driver)

@pytest.fixture
def open_registration(driver, registration_page):
    driver.find_element(*RegistrationPage.REGISTER_BUTTON).click()
    return registration_page

@pytest.fixture
def register_user(open_registration):
    def _register(name, lastname, email, password):
        page = open_registration
        page.element(page.NAME_INPUT).send_keys(name)
        page.element(page.LASTNAME_INPUT).send_keys(lastname)
        page.element(page.EMAIL_INPUT).send_keys(email)
        page.element(page.PASSWORD_INPUT).send_keys(password)
        page.element(page.REPASSWORD_INPUT).send_keys(password)
        page.element(page.SUBMIT_BUTTON).click()
    return _register