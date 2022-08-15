# 8. Access the mobile screen when accessing the website with selenium
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

mobile_emulation = {
   "deviceMetrics": { "width": 375, "height": 812, "pixelRatio": 3.0 } 
}

options = Options()

options.add_experimental_option("mobileEmulation", mobile_emulation)
driver = webdriver.Chrome(options = options)

driver.set_window_size(400, 900)

driver.get('https://www.tvo.org/series-docs')