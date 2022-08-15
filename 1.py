# 1. main page -> from the header navigate to Docs & Series -> Select All docs -> Show the All Docs
# 2. mouse hover action
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get("https://www.tvo.org")

driver.maximize_window() 

actions = webdriver.ActionChains(driver)

menu = driver.find_element(By.XPATH, '//div[text() = "Docs & Series"]') 
actions.move_to_element(menu).perform()

time.sleep(1)

submenu = driver.find_element(By.LINK_TEXT, 'All Docs') 
actions.move_to_element(submenu).perform()
submenu.click()

time.sleep(1)



