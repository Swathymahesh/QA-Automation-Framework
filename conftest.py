import pytest

from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

# Public demo credentials published on the practice site's login page.
STANDARD_USER = ("standard_user", "secret_sauce")
LOCKED_USER = ("locked_out_user", "secret_sauce")


@pytest.fixture
def login_page(page, base_url):
    """A browser page already opened on the login screen."""
    return LoginPage(page, base_url).open()


@pytest.fixture
def inventory_page(login_page):
    """Logs in as a standard user and returns the loaded product page."""
    login_page.login(*STANDARD_USER)
    inventory = InventoryPage(login_page.page)
    inventory.expect_loaded()
    return inventory
