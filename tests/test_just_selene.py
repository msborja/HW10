from selene import by, browser, be
from selene.support.shared.jquery_style import s


def test_github():
    browser.open('https://github.com/')

    s('.header-search-button').click()
    s('#query-builder-test').type('eroshenkoam/allure-example')
    s('#query-builder-test').submit()

    s(by.link_text('eroshenkoam/allure-example')).click()

    s('#issues-tab').click()

    s(by.partial_text('#84')).should(be.visible)
