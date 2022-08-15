# 5. Find "Watch Now" button and click, go to that link, click play button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

driver = webdriver.Chrome()
driver.get('https://www.tvo.org/series-docs')

driver.maximize_window()

actions = ActionChains(driver)

time.sleep(1)

watch_now = driver.find_element(By.LINK_TEXT, 'Watch Now')
actions.move_to_element(watch_now).perform()

time.sleep(1)

watch_now.click()

time.sleep(2)

play_video = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, "//button[@title='Play Video']")))
play_video.click()




