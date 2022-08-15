# 7. Click next button, preview button in navBar
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.tvo.org/series-docs')

driver.maximize_window()

driver.implicitly_wait(10)

next = driver.find_element(By.XPATH, "//div[@class='series-docs-nav__nav-button series-docs-nav__next-button']")

time.sleep(0.5)
next.click()

time.sleep(0.5)

prev = driver.find_element(By.XPATH, "//div[@class='series-docs-nav__nav-button series-docs-nav__prev-button']")

time.sleep(0.5)
prev.click()
