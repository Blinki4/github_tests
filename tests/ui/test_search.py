import pytest
import allure


@pytest.mark.ui
@allure.title('Поиск репозитория linux')
def test_search_linux_repo(driver, main_page, search_page):
    main_page.open_search()
    main_page.enter_search_input('linux')
    main_page.search_input.submit()
    assert search_page.is_title_in_results('torvalds/linux')
