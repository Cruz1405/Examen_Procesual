from selenium.webdriver.common.by import By

from page_object.home_page import HomePage
from page_object import home_page
from selenium_wrapper.base import Base


class TestLogin(Base):

    def test_1_view_page(self):
        driver = self.driver
        driver.get(home_page.base_url)
        element = HomePage(driver).view_page()
        self.assertTrue(element, "not image")

    def test_2_login(self):
        driver = self.driver
        driver.get(home_page.base_url)
        HomePage(driver).send_text_user("standard_user")
        HomePage(driver).send_password("secret_sauce")

        #para enviar los datos del login
        button = HomePage(driver).get_button()
        button.click()
