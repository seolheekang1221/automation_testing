# 3. How to find all broken links
from selenium import webdriver
from selenium.webdriver.common.by import By
from requests.exceptions import MissingSchema, InvalidSchema
import requests

broken_links = 0
valid_links = 0

driver = webdriver.Chrome()
driver.get('https://www.tvo.org')

driver.maximize_window()

all_links = driver.find_elements(By.TAG_NAME,"a")

for link in all_links:
    try:
        url = link.get_attribute('href')
        result = requests.head(url) 
        print(url, result.status_code)
        if (result.status_code == 404):
            broken_links = (broken_links + 1)
        else:
            valid_links = (valid_links + 1)
            
    except requests.exceptions.MissingSchema:
        print("Encountered MissingSchema Exception")
    except requests.exceptions.InvalidSchema:
        print("Encountered InvalidSchema Exception")     
    except:
        print("Encountered Some other Exception")
                   
print("Detection of broken links completed with " + str(broken_links) + " broken links and " + str(valid_links) + " valid links")
   
