# 13. How to switch to new window 
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()

driver.get('https://www.tvo.org/series-docs')
driver.maximize_window()
print("First window title = " + driver.title)

main_page = driver.window_handles[0]
driver.find_element(By.XPATH, "//li[2]//button[1]").click()

driver.switch_to.window(driver.window_handles[1])
driver.get_window_position(driver.window_handles[1])

driver.find_element(By.LINK_TEXT, 'African Renaissance').click()

driver.switch_to.default_content()
driver.switch_to.window(driver.window_handles[0])
driver.close()




