from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

service = Service("C:\Drivers\chromedriver-win64\chromedriver.exe")
driver = webdriver.Chrome(service=service)
driver.get("https://www.facebook.com")
driver.find_element(By.ID, "email").send_keys("satendrajaiswal269@gmail.com")
driver.find_element(By.ID, "pass").send_keys("*********")
driver.find_element(By.NAME, "login").click()
time.sleep(5)
driver.quit()
