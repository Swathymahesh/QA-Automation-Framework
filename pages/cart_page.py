from playwright.sync_api import Page


class CartPage:
    """Page object for the shopping cart."""

    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator(".cart_item")
        self.item_names = page.locator(".inventory_item_name")
        self.checkout_button = page.locator('[data-test="checkout"]')

    def start_checkout(self):
        self.checkout_button.click()
