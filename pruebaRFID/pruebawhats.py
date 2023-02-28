from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

os.environ["PATH"] += os.pathsep + "/home/chava/Descargas/chromedriver_linux64/chromedriver"


options = webdriver.ChromeOptions()
options.binary_location = "/usr/bin/brave-browser-stable" # Ruta de la instalación de Brave
driver_path = "/home/chava/Descargas/chromedriver_linux64/chromedriver" # Ruta donde se encuentra el controlador descargado

driver = webdriver.Chrome(options=options, executable_path=driver_path)
driver.get('https://web.whatsapp.com/')

wait = WebDriverWait(driver, 10)
search_box = wait.until(EC.presence_of_element_located((By.XPATH, '//div[@contenteditable="true"][@data-tab="3"]')))


name = input('Enter the name of user or group: ')
msg = input('Enter your message: ')
count = int(input('Enter the count: '))

input('Enter anything after scanning QR code')

search_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="3"]')
search_box.send_keys(name + Keys.ENTER)

input_box = driver.find_element_by_xpath('//div[@contenteditable="true"][@data-tab="1"]')

for i in range(count):
    input_box.send_keys(msg + Keys.ENTER)
    time.sleep(1)

driver.quit()
