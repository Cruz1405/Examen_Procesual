import unittest

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

ser_obj = Service("D:/Instalados/Chrome Driver/chromedriver.exe")
class Base(unittest.TestCase):
    driver = webdriver.Chrome(service = ser_obj)

    @classmethod
    def setUpClass(cls):
        driver = cls.driver
        #driver.get("https://www.saucedemo.com/")
        driver.maximize_window()
        driver.implicitly_wait(10)

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()

