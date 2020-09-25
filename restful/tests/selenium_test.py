from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import json, base64

webdriver_options = Options()
webdriver_options.add_argument('--headless')
webdriver_options.add_argument('--disable-gpu')
#Bajar chromedriver para su SO y poner la ruta
driver = webdriver.Chrome(executable_path='../chromedriver', options=webdriver_options)
driver.get('http://127.0.0.1:5000/')
driver.find_element_by_id('boton').click()

lement = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.ID, "span1"))
        )

driver.close()