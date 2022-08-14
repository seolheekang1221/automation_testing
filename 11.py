#main page -> from the header navigate to Docs & Series -> Select All docs -> Show the All Docs
#python selenium hover over element
#Mouse actions APIs (Context click)
#보충해야할것 :  select All docs할때 색깔 표시가 없다
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium_move_cursor.MouseActions import move_to_element_chrome

import time

driver = webdriver.Chrome()
driver.get("https://www.tvo.org")

driver.maximize_window() #화면 크게

actions = webdriver.ActionChains(driver)

menu = driver.find_element(By.XPATH, '//div[text() = "Docs & Series"]') 
actions.move_to_element(menu).perform() #메뉴 커서 올리기
time.sleep(1)

submenu = driver.find_element(By.LINK_TEXT, 'All Docs') #섭메뉴 클릭하기
actions.move_to_element(submenu).perform()
submenu.click()

time.sleep(1)

driver.close()

