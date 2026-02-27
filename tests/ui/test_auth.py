import credentials



def test_redirect_to_main_page_after_sign_in(authorized_page):
    assert authorized_page.home_title_is_displayed


def test_sign_in(authorized_page):
    assert authorized_page.navigation_menu_username_text == credentials.valid_login