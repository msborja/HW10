import allure
from selene import by, browser, be
from selene.support.shared.jquery_style import s


def test_decorator_steps():
    open_main_page()
    search_for_repository('eroshenkoam/allure-example')
    go_to_repository('eroshenkoam/allure-example')
    open_issue()
    should_see_issues_with_number('84')


@allure.step('Открываем главную страницу')
def open_main_page():
    browser.open('https://github.com/')


@allure.step('Ищем репозиторий {repo}')
def search_for_repository(repo):
    s('.header-search-button').click()
    s('#query-builder-test').type(repo)
    s('#query-builder-test').submit()


@allure.step('Переходим по ссылке репозитория {repo}')
def go_to_repository(repo):
    s(by.link_text(repo)).click()


@allure.step('Открываем вкладку Issues')
def open_issue():
    s('#issues-tab').click()


@allure.step('Проверяем наличие Issues #84')
def should_see_issues_with_number(number):
    s(by.partial_text('#' + number)).should(be.visible)
