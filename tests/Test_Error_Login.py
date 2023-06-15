from page_object.home_page import HomePage
from page_object import home_page
from selenium_wrapper.base import Base


class TestLogin(Base):

    def test_error_login(self):
        driver = self.driver
        driver.get(home_page.base_url)
        HomePage(driver).send_text_user("user_test")
        HomePage(driver).send_password("test_user")

        #para enviar los datos del login
        button = HomePage(driver).get_button()
        button.click()
