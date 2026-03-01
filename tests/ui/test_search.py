import pytest
import allure


@pytest.mark.ui
@allure.title('Поиск репозитория linux')
def test_search_linux_repo(main_page, search_page):
    main_page.search('linux')
    assert search_page.is_title_in_results('torvalds/linux')


@pytest.mark.ui
@allure.title('Поиск профиля')
def test_search_user_repo(main_page, search_page):
    main_page.search('Blinki4')
    assert search_page.is_title_in_results('Blinki4/Blinki4')


@pytest.mark.ui
@allure.title('Открытие поиска хоткеем "/"')
def test_open_search_with_hotkey(main_page):
    main_page.open_search_input_with_hotkey()
    assert main_page.search_input_is_displayed



@pytest.mark.ui
@allure.title('Поиск несуществующего объекта')
def test_empty_results(main_page, search_page):
    main_page.search('khskhdsjhfsdkjhfshjdf')
    assert search_page.no_results_search_image_is_displayed


@pytest.mark.ui
@allure.title('Поиск с пустой строкой поиска')
def test_empty_search_query(main_page, search_page):
    main_page.search('')
    assert search_page.empty_search_image_is_displayed