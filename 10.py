# 9. Scroll down to "length 1080"
# 10. Scroll down to the bottom of the page
# 11. Scroll to specific elements((ex) "Cobalt" movie name click)
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

driver = webdriver.Chrome()
driver.get('https://www.tvo.org/series-docs')

driver.maximize_window()

time.sleep(2)

driver.execute_script('window.scrollTo(0, 1080)')

scroll_Cnt = 6

while scroll_Cnt > 1:
    scroll_Cnt = scroll_Cnt - 1
    print('There are ' + str(scroll_Cnt) + ' pages left to bottom of the page')
    time.sleep(2) 
    
driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
time.sleep(2) 

specific_element = driver.find_element(By.LINK_TEXT, 'Cobalt')
specific_element.location_once_scrolled_into_view






