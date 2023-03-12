from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    link = "http://suninjuly.github.io/alert_accept.html"
    browser.get(link)
    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()

    confirm = browser.switch_to.alert
    confirm.accept()

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input.send_keys(y)

    button = browser.find_element(By.CSS_SELECTOR, "button.btn").click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()