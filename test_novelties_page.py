import allure


@allure.feature('feature2')
@allure.story('story1')
def test_price_filter(page):
    page.novelties.filter_by_cost()


@allure.feature('feature2')
@allure.story('story2')
def test_price_filter2222(page):
    page.novelties.filter_by_cost()
