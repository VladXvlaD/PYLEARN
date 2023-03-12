from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import math
import time

try:
    browser = webdriver.Chrome(executable_path=ChromeDriverManager().install())
    link = "http://suninjuly.github.io/huge_form.html"
    browser.get(link)

    elements = browser.find_elements(By.TAG_NAME, "input")
    for element in elements:
        element.send_keys("Hello World!")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()


finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()