import allure


@allure.feature('feature1')
@allure.story('story3')
def test_login(page):
    page.main.login()


@allure.feature('feature1')
@allure.story('story4')
def test_login222(page):
    page.main.login()
