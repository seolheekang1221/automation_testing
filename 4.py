# 4. Find the height of the current document and scroll down every 2 seconds until the height is 0
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.tvo.org/programs/a-stitch-in-time')

driver.maximize_window()

prev_height = driver.execute_script('return document.body.scrollHeight')

while True:
    driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
    time.sleep(3)

    current_height = driver.execute_script('return document.body.scrollHeight')    
   
    if prev_height == current_height:
        break
    prev_height = current_height

driver.implicitly_wait(10)

driver.execute_script('window.scrollTo(0,0)')




