#Find "Watch Now" button and click, go to that link, click play button
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium

driver = webdriver.Chrome()

driver.maximize_window() #화면 크게

driver.get('https://www.tvo.org')

