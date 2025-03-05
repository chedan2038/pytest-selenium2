import allure

from locators import MainPageLocators, NoveltiesPageLocators
from pages.base_page import BasePage
from pages.config import BASE_LINK


class NoveltiesPage(BasePage):

    @allure.step("Надеюсь никто это не увидит")
    def filter_by_cost(self):
        self._open(BASE_LINK)
        self._click(MainPageLocators.NOVELTIES)

        self._element_is_visible(NoveltiesPageLocators.INPUT_PRICE_TO_DEFAULT)

        self._send_text(NoveltiesPageLocators.INPUT_PRICE_FROM, '500', True)
        self._send_text(NoveltiesPageLocators.INPUT_PRICE_TO, '1000', True)
        self._send_keys(NoveltiesPageLocators.INPUT_PRICE_TO, "ENTER")
        self._element_is_visible(self._element_by_text('от 500₽ до 1000₽', 'span'))
