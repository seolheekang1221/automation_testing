# 6. series-docs page -> search page -> "go to Search all of TVO Today..." -> search "Eat me" and Enter -> click the "Eat Me video"
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

driver = webdriver.Chrome()
driver.get('https://www.tvo.org/series-docs')

driver.maximize_window()

actions = ActionChains(driver)

time.sleep(1)
search_page = driver.find_element(By.TAG_NAME, "button").click()

time.sleep(1)
search_button = driver.find_element(By.TAG_NAME, "input").click()

time.sleep(1)
actions.send_keys('Eat Me').key_down(Keys.RETURN).perform()

time.sleep(2)
click_video = driver.find_element(By.XPATH, "//a[@href='https://www.tvo.org/programs/eat-me-or-try-not-to']").click()

