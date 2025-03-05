from typing import Callable

from selenium.common import TimeoutException
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.ie.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as ec, expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.config import IMPLICITLY_WAIT_TIME


class BasePage:

    def __init__(self, driver: WebDriver):
        self._driver = driver
        self._driver.implicitly_wait(IMPLICITLY_WAIT_TIME)

    def _open(self, link: str):
        """
        Перейти по ссылке

        :param link: ссылка
        """
        self._driver.get(link)

    def _click(self, element: tuple):
        """
        Клик по элементу

        :param element: (By... , locator)
        """
        self._driver.find_element(*element).click()

    def _send_text(self, element: tuple[str, str], text: str, clear: bool = False):
        """
        Отправить текст в указанный элемент

        :param element: (By... , locator)
        :param text:
        :param clear: очистить поле перед вводом
        """

        if clear:
            self._send_keys(element, "CONTROL", "a")

        self._driver.find_element(*element).send_keys(text)

    def _check_attribute_value(self, element: tuple[str, str], attribute: str, expected_value: str):
        """
        Проверка значения атрибута/свойства

        :param element: (By... , locator)
        :param attribute:
        :param expected_value:
        """
        current_value = self._driver.find_element(*element).get_attribute(attribute)
        assert current_value == expected_value, f"Текущее значение атрибута {attribute} \
        у элемента {element} не соответсвует ожидаемому. Текущее: {current_value} Ожидаемое: {expected_value}"

    def _send_keys(self, element: tuple[str, str], *keys: str):
        """
        Использовать комбинацию клавиш

        :param element: (By... , locator)
        :param keys:
        """
        self._driver.find_element(*element).send_keys(*(getattr(Keys, k, k) for k in keys))

    @staticmethod
    def _element_by_text(text: str, tag='*') -> tuple[str, str]:
        """
        Возвращает локатор по тексту

        :param text:
        :param tag:
        :return: Локатор формата (By.XPATH, '//*[text() ='abc'])
        """
        return By.XPATH, f'//{tag}[text()="{text}"]'

    def _element_is_clickable(self, element: tuple[str, str], time: int = 5):
        """
        Проверка кликабельности элемента

        :param element: (By... , locator)
        :param time: время на проверку
        """
        self.__base_element_is(True, ec.element_to_be_clickable,
                               f"Элемент {element} не кликабелен", element, time)

    def _element_is_visible(self, element: tuple[str, str], time: int = 5):
        """
        Проверка видимости элемента

        :param element: (By... , locator)
        :param time: время на проверку
        """
        self.__base_element_is(True, ec.visibility_of_element_located,
                               f"Элемент {element} не отображен на странице", element, time)

    def _element_is_not_visible(self, element: tuple[str, str], time: int = 5):
        """
        Проверка на отсутствие видимости элемента

        :param element: (By... , locator)
        :param time: время на проверку
        """
        self.__base_element_is(False, ec.visibility_of_element_located,
                               f"Ожидается что элемент {element} не будет отображен", element, time)

    def __base_element_is(self, until: bool, expected_condition: Callable[..., expected_conditions], error_msg: str,
                          element: tuple[str, str],
                          time: int):
        """

        :param until: Проверка [until | until_not]
        :param expected_condition: Функция модуля expected_conditions
        :param error_msg: Сообщение при возникновении ошибки
        :param element: (By... , locator)
        :param time: время на проверку
        """
        wait = WebDriverWait(self._driver, time)
        wait_until = wait.until if until else wait.until_not

        try:
            wait_until(expected_condition(element))
        except TimeoutException:
            raise AssertionError(error_msg)
