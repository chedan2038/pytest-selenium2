from locators import MainPageLocators, LoginPageLocators
from pages.base_page import BasePage
from pages.config import BASE_LINK


class MainPage(BasePage):

    def login(self):
        self._open(BASE_LINK)

        self._click(MainPageLocators.PROFILE_BUTTON)
        self._click(self._element_by_text('Войти или создать X5ID'))

        self._send_text(LoginPageLocators.INPUT_NUMBER, '9999999999')
