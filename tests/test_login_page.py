from pages.login_pages import LoginPage
from data.login_data import LOGIN_DATA
from utils.config import *

def test_login_using_valid_data(page):
    login_page = LoginPage(page)
    page.goto("https://nusacodes.com/")
    login_page.click_button_login_member()
    login_page.fill_email("trifofroujepra-1723@warlus.asso.st")
    login_page.fill_password("123456789")
    login_page.click_button_login()
    login_page.click_button_ok()
    success_login = login_page.validate_name()
    assert success_login == "Rizki Nusacode"

def test_login_using_valid_dataIMPORT(page):
    login_page = LoginPage(page)
    page.goto(URL_PROD)
    login_page.click_button_login_member()
    login_page.fill_email(LOGIN_DATA["valid_user"]["email"])
    login_page.fill_password(LOGIN_DATA["valid_user"]["password"])
    login_page.click_button_login()
    login_page.click_button_ok()
    success_login = login_page.validate_name()
    assert success_login == (LOGIN_DATA["valid_user"]["name"])