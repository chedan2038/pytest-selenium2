from selenium.webdriver.common.by import By


class MainPageLocators:
    PROFILE_BUTTON = (By.XPATH, "//span[text()='Профиль']/parent::a")
    NOVELTIES = (By.XPATH, "//a[@href='/cat/c/1228/novinki']")


class LoginPageLocators:
    INPUT_NUMBER = (By.ID, "username")


class NoveltiesPageLocators:
    INPUT_PRICE_FROM = (By.CSS_SELECTOR, "input[aria-label='Минимальная цена']")
    INPUT_PRICE_TO = (By.CSS_SELECTOR, "input[aria-label='Максимальная цена']")
    INPUT_PRICE_TO_DEFAULT = (By.CSS_SELECTOR, "input[value='79']")
