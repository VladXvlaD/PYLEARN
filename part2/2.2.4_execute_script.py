from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time

browser = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#browser.execute_script("alert('Robots at work');")
#browser.execute_script("document.title='Script executing';")
browser.execute_script("document.title='Script executing';alert('Robots at work');")

time.sleep(5)
browser.quit()