from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()
driver.get("https://www.tvo.org/series-docs")

watchout_link = driver.find_element(By.LINK_TEXT, "Docs")
watchout_link.click()

try:
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Beauty"))
    )
    element.click()
    
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Play Video"))
    )
    element.click()
    
    driver.back()
    driver.back()
    driver.back()
    
except:
    driver.quit()

