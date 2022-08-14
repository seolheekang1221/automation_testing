#Click the menu button, mouse Hover actions, navBar
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get("https://www.tvo.org/series-docs")

element = driver.find_element

hover = ActionChains(driver).move_to_element(element)

hover.perform()

driver.find_element(By.CLASS_NAME, 'MuiButton-label-83')


# driver.back()
