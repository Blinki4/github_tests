import time

import pytest
import allure

from pages.search_page import SearchPage


@pytest.mark.ui
@allure.title('Поиск репозитория linux')
def test_search_linux_repo(driver, main_page):
    main_page.open_search()
    main_page.enter_search_input('linux')
    main_page.search_input.submit()
    search_page = SearchPage(driver)


    time.sleep(2)
    for title in search_page.results_titles:
        if title.text == 'torvalds/linux':
            assert True
            break
