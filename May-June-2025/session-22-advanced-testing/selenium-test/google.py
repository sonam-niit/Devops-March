from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
#step 1 set up driver
driver = webdriver.Chrome()
# Open a web page
driver.get('https://www.google.com/')
print('Page Title',driver.title)
#find the search Box
search_box = driver.find_element(By.NAME,'q')
# type in the query field
search_box.send_keys("Selenium Python")
search_box.send_keys(Keys.ENTER)
#wait for 3 seconds
time.sleep(3)
print('Page Title',driver.title)
driver.close()