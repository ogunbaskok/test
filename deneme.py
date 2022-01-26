from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time


PATH = "C:\Program Files\chromedriver\chromedriver1.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://google.com.tr")
time.sleep(5)
driver.maximize_window()
print("basari ile çalistirildi")
time.sleep(5)
    
   