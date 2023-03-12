from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time
import math


def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))


try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    x_element1 = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element1.text
    y = calc(x)

    input2 = browser.find_element(By.ID, "answer")
    input2.send_keys(y)

    input = browser.find_element(By.TAG_NAME, "input")
    browser.execute_script("return arguments[0].scrollIntoView(true);", input)

    option1 = browser.find_element(By.CSS_SELECTOR, "[id='robotCheckbox']")
    option1.click()

    option2 = browser.find_element(By.CSS_SELECTOR, "[value='robots']")
    option2.click()

    button = browser.find_element(By.XPATH, "//button[@class='btn btn-primary']")
    button.click()

finally:
    # успеваем скопировать код за 30 секунд
    time.sleep(5)
    # закрываем браузер после всех манипуляций
    browser.quit()
