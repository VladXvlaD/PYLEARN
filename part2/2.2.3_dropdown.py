from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import Select
import time


browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "http://suninjuly.github.io/selects1.html"
browser.get(link)
try:
    a = browser.find_element(By.ID, 'num1').text
    b = browser.find_element(By.ID, 'num2').text
    s = str(int(a) + int(b))

    select = Select(browser.find_element(By.TAG_NAME, "select"))
    select.select_by_value(s)

    button = browser.find_element(By.CLASS_NAME, "btn.btn-default")
    button.click()

    print(browser.switch_to.alert.text.split()[-1])

finally:
      time.sleep(5)
      browser.quit()

#browser.find_element(By.TAG_NAME, "select").click()
#browser.find_element(By.CSS_SELECTOR, "option:nth-child(2)").click()

#select = Select(browser.find_element(By.TAG_NAME, "select"))
#select.select_by_value("1") # ищем элемент с текстом "Python"