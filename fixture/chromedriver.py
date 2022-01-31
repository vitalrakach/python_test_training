# -*- coding: utf-8 -*-
from selenium import webdriver
import time

url = "https://instagram.com"
driver = webdriver.Chrome(executable_path="C:\\Projects\\chromedriver.exe")

try:
    driver.get(url=url)
    time.sleep(3)
    driver.save_screenshot("screenshot1.png")

except Exception as ex:
    print(ex)
finally:
    driver.close()
    driver.quit()
