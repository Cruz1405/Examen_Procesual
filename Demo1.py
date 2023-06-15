from selenium import webdriver

from selenium.webdriver.chrome.service import  Service
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

ser_obj = Service("D:/Instalados/Chrome Driver/chromedriver.exe")
driver = webdriver.Chrome(service = ser_obj)

driver.get(" https://www.saucedemo.com/")

driver.maximize_window()

def Test_Login01 (self):
    driver = self.driver
    username_field = driver.find_element(By.ID, 'username')
    username_field.send_keys('standard_user')

    password_field = driver.find_element(By.ID, 'password')
    password_field.send_keys('secret_sauce')


driver.close()

