#how to find all broken links
#에러 [45104:42904:0814/101248.860:ERROR:device_event_log_impl.cc(214)] [10:12:48.860] USB: usb_device_handle_win.cc:1048 Failed to read descriptor from node connection: ???? ??? ??? ???? ????. (0x1F)
#위에 에러 찾아봐
from selenium import webdriver
from selenium.webdriver.common.by import By
from requests.exceptions import MissingSchema, InvalidSchema
import requests

broken_links = 0
valid_links = 0

driver = webdriver.Chrome()

driver.maximize_window() #화면 크게

driver.get('https://www.tvo.org')

#get all links, web elements by the “a” property.
all_links = driver.find_elements(By.TAG_NAME,"a")

#check each link if it is broken or not
for link in all_links:
    try:
        #extract url from href attribute
        url = link.get_attribute('href')
        #send request to the url and get the result
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
        print("Encountered Some other Execption")
                   
print("Detection of broken links completed with " + str(broken_links) + " broken links and " + str(valid_links) + " valid links")
   
