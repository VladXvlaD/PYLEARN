from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
link = "https://SunInJuly.github.io/execute_script.html"
browser.get(link)
button = browser.find_element(By.TAG_NAME, "button")
browser.execute_script("return arguments[0].scrollIntoView(true);", button)
#browser.execute_script("window.scrollBy(0, 100);") # Эта команда проскроллит страницу на 100 пикселей вниз
button.click()

time.sleep(5)
browser.quit()