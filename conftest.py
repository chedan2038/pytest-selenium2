import pytest
from selenium import webdriver

from pages._page_instances import PageInstances


@pytest.fixture()
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver

    driver.quit()


@pytest.fixture()
def page(driver):
    return PageInstances(driver)
