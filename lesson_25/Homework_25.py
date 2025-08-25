
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

# Запуск Chrome
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("https://shop.kyivstar.ua/")
time.sleep(3)  # Даем странице прогрузиться

# Локаторы по ID
id_locators = ["obmen", "cart", "tehnika", "__next", "pick-number"]
for locator in id_locators:
    try:
        element = driver.find_element(By.ID, locator)
        print(f"ID '{locator}' найден: {element.tag_name}")
    except:
        print(f"ID '{locator}' не найден")

# Локаторы по NAME
name_locators = ["search", "description", "next-head-count", "viewport", "application-name"]
for locator in name_locators:
    try:
        element = driver.find_element(By.NAME, locator)
        print(f"NAME '{locator}' найден: {element.tag_name}")
    except:
        print(f"NAME '{locator}' не найден")

# Локаторы по CLASS_NAME
class_locators = ["body_", "_search_wrap__HGm8j", "_punkts__o5aQK", "_top_menu_inner__SSWFt", "_footer__V38Zw"]
for locator in class_locators:
    try:
        element = driver.find_element(By.CLASS_NAME, locator)
        print(f"CLASS_NAME '{locator}' найден: {element.tag_name}")
    except:
        print(f"CLASS_NAME '{locator}' не найден")

# Локаторы по CSS_SELECTOR
css_locators = [
    "#__next > div.page-container > div > div.limit-container > div > div._bottom__bHy0g > div._search__7giPW.desktop > div._search_wrap__HGm8j > input[type=hidden]",
    "#__next > div.page-container > div > div.limit-container > div > div._bottom__bHy0g > div._search__7giPW.desktop > div._search_wrap__HGm8j > div.select-search._select_search__5VboM.lupa > div > input",
    "#__next > div.page-container > div > div.limit-container > div > div._bottom__bHy0g > div._catalog__NBoD9.desktop.opened > div._menu__y9wUL > div._punkts__o5aQK",
    "#__next > div.page-container > div > div.limit-container > div > div._bottom__bHy0g > div._catalog__NBoD9.desktop.opened > div._menu__y9wUL > div._punkts__o5aQK > div:nth-child(2) > a",
    "#__next > div.page-container > div > div._footer__V38Zw > div > div > div:nth-child(4) > div"
]
for locator in css_locators:
    try:
        element = driver.find_element(By.CSS_SELECTOR, locator)
        print(f"CSS_SELECTOR '{locator}' найден: {element.tag_name}")
    except:
        print(f"CSS_SELECTOR '{locator}' не найден")

# Локаторы по XPATH
xpath_locators = [
    "//*[@id=\"__next\"]/div[5]/div/div[1]/div/div[3]/div[1]/div[2]/div[2]",
    "//*[@id=\"__next\"]/div[5]/div/div[2]/div[1]/div/div[1]/div/a[1]/button/div",
    "//*[@id=\"__next\"]/div[5]/div/div[1]/div/div[2]/div[2]",
    "//*[@id=\"__next\"]/div[5]/div/div[2]/div[2]/div/div[1]/div[1]/div[1]",
    "//*[@id=\"__next\"]/div[5]/div/div[3]/div/div/div[2]"
]
for locator in xpath_locators:
    try:
        element = driver.find_element(By.XPATH, locator)
        print(f"XPATH '{locator}' найден: {element.tag_name}")
    except:
        print(f"XPATH '{locator}' не найден")

# Закрываем браузер
driver.quit()