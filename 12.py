# 12. Check "Described video" if turn on or off
from selenium import webdriver
# from selenium.webdriver.support.select.Select import Select
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.tvo.org/video/documentaries/building-bastille')
driver.maximize_window()

# check_box = driver.find_element(By.XPATH, "(//button[@aria-label='Described Video: Off'])[1]") 
# check_box.click()


check_boxes = driver.find_elements(By.TAG_NAME,"button")

for check_box in check_boxes:
    if check_boxes.is_selected():
        pass
    else:
        check_box.click()
   