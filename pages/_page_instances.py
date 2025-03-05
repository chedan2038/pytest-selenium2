from pages.main_page import MainPage
from pages.novelties_page import NoveltiesPage


class PageInstances:
    page_instance = None

    def __new__(cls, *args, **kwargs):
        if not cls.page_instance:
            cls.page_instance = super().__new__(cls)
        return cls.page_instance

    def __init__(self, driver):
        self.main = MainPage(driver)
        self.novelties = NoveltiesPage(driver)
