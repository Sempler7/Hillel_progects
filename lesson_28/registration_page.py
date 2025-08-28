from selenium.webdriver.common.by import By

class RegistrationPage:
    def __init__(self, driver):
        self.driver = driver

    # Локатори
    REGISTER_BUTTON = (By.XPATH, "//button[text()='Sign up']")
    NAME_INPUT = (By.ID, "signupName")
    LASTNAME_INPUT = (By.ID, "signupLastName")
    EMAIL_INPUT = (By.ID, "signupEmail")
    PASSWORD_INPUT = (By.ID, "signupPassword")
    REPASSWORD_INPUT = (By.ID, "signupRepeatPassword")
    SUBMIT_BUTTON = (By.XPATH, "//button[text()='Register']")

    def element(self, locator):
        return self.driver.find_element(*locator)