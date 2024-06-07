import allure
from selene.support import by
from selene.support.shared import browser
from selene.support.conditions import be
from selene.support.shared.jquery_style import s


def test_with_allure_steps():
    with allure.step('Открываем главную страницу'):
        browser.open('https://github.com/')

    with allure.step('Ищем репозиторий'):
        s('.header-search-button').click()
        s('#query-builder-test').type('eroshenkoam/allure-example')
        s('#query-builder-test').submit()

    with allure.step('Переходим по ссылке репозитория'):
        s(by.link_text('eroshenkoam/allure-example')).click()

    with allure.step('Открываем вкладку Issues'):
        s('#issues-tab').click()

    with allure.step('Проверяем наличие Issues #84'):
        s(by.partial_text('#84')).should(be.visible)
