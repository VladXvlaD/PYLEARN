from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
import time
import math
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def calc(x):
    return str(math.log(abs(12 * math.sin(int(x)))))

try:
    browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    link = "http://suninjuly.github.io/explicit_wait2.html"
    browser.get(link)

    WebDriverWait(browser, 12).until(
        EC.text_to_be_present_in_element((By.ID, "price"), "100")
    )
    btn = browser.find_element(By.ID, "book").click()

    x_element = browser.find_element(By.CSS_SELECTOR, "[id='input_value']")
    x = x_element.text
    y = calc(x)

    input = browser.find_element(By.CSS_SELECTOR, "[id='answer']")
    input.send_keys(y)

    button = browser.find_element(By.ID, "solve").click()

finally:
    # успеваем скопировать код за 10 секунд
    time.sleep(10)
    # закрываем браузер после всех манипуляций
    browser.quit()