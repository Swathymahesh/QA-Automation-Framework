import pytest
from playwright.sync_api import expect

from conftest import LOCKED_USER, STANDARD_USER
from pages.inventory_page import InventoryPage


@pytest.mark.smoke
def test_valid_login_shows_products(login_page):
    login_page.login(*STANDARD_USER)
    inventory = InventoryPage(login_page.page)
    inventory.expect_loaded()
    expect(inventory.items).to_have_count(6)


@pytest.mark.regression
@pytest.mark.parametrize(
    "username, password, expected_error",
    [
        ("standard_user", "wrong_password", "do not match"),
        ("", "secret_sauce", "Username is required"),
        ("standard_user", "", "Password is required"),
        (LOCKED_USER[0], LOCKED_USER[1], "locked out"),
    ],
    ids=["wrong-password", "no-username", "no-password", "locked-out-user"],
)
def test_invalid_login_shows_error(login_page, username, password, expected_error):
    login_page.login(username, password)
    expect(login_page.error).to_be_visible()
    expect(login_page.error).to_contain_text(expected_error)
