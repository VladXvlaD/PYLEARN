from time import time
from webbrowser import Chrome
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
#driver.set_window_size(1920,1080)

driver.get('https://funandfunction.com/')
searchbox = driver.find_element(By.NAME, 'q')
searchbox.send_keys('BL1562')
searchbox.send_keys(Keys.RETURN)

# button add to cart
atc_button = driver.find_element(By.XPATH, "//button[@class='jss566 action tocart primary fourtellAddToCart']")
atc_button.click()

#hover mini cart
element_to_hover_over = driver.find_element(By.XPATH, "//a[@class='action showcart']")
hover = ActionChains(driver).move_to_element(element_to_hover_over).perform()

#go to cart
view_cart = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//a[contains(.,'View Cart')]"))).click()

# Bolt checkout
checkout = driver.find_element(By.XPATH, "//main[@id='maincontent']/descendant::div[@data-tid='bolt-checkout-button']").click()

email = driver.find_element(By.XPATH, "//div[@class='_3J8meM6a_Pd2YnfTrgs7KE']/input[@type='email']").send_keys('xtest@mail.com')

country = driver.find_element(By.XPATH, "//select[@id='country-code-selector']").click()
select_country_us = driver.find_element(By.XPATH, "//select[@id='country-code-selector']//option[@value='US']").click()

phone_number = driver.find_element(By.NAME, 'phone').send_keys('2135986455')

first_name = driver.find_element(By.NAME, 'fname').send_keys('test')

last_name = driver.find_element(By.NAME, 'lname').send_keys('test')

street_sddress = driver.find_element(By.NAME, 'notSearchAddrss').send_keys('199 Twin Willow Lane')

country2 = driver.find_element(By.XPATH, "//select[@id='shippingCountry']").click()
select_country_us2 = driver.find_element(By.XPATH, "//select[@id='shippingCountry']//option[@value='US']").click()

zip_code = driver.find_element(By.NAME, 'ship-zip').send_keys('28546')

ship_city = driver.find_element(By.NAME, 'ship-city').send_keys('Jacksonville')

state = driver.find_element(By.XPATH, "//select[@id='shippingState']").click()
select_state = driver.find_element(By.XPATH, "//select[@id='shippingState']//option[@value='North Carolina']").click()

continuee = driver.find_element(By.XPATH, "//button[@data-tid='checkout-continue-button']").click()