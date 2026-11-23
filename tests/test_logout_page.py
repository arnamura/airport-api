from pages.global_pages import globalPage
from pages.login_pages import LoginPage
from playwright.sync_api import expect


def test_logout_normal(login):
    global_page = globalPage(login)
    login_page = LoginPage(login)  # 1. Buat instance objeknya terlebih dahulu

    #global_page.click_button_sidebar()
    global_page.click_button_sidebar_logout()

    # 2. Panggil method validasi dari objek login_page (bukan click_button_login_member)
    assert login.url == "https://nusacodes.com/login"