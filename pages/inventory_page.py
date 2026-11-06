import re
from playwright.sync_api import Page, expect


class InventoryPage:
    """Page object for the product listing."""

    def __init__(self, page: Page):
        self.page = page
        self.items = page.locator(".inventory_item")
        self.names = page.locator(".inventory_item_name")
        self.prices = page.locator(".inventory_item_price")
        self.sort_dropdown = page.locator('[data-test="product-sort-container"]')
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def expect_loaded(self):
        expect(self.page).to_have_url(re.compile(r"inventory\.html"))
        expect(self.items.first).to_be_visible()

    def sort_by(self, value: str):
        """value: 'az', 'za', 'lohi' or 'hilo'."""
        self.sort_dropdown.select_option(value)

    def product_names(self) -> list[str]:
        return self.names.all_inner_texts()

    def product_prices(self) -> list[float]:
        return [float(t.replace("$", "")) for t in self.prices.all_inner_texts()]

    def add_to_cart(self, product_name: str):
        self.items.filter(has_text=product_name).get_by_role("button", name="Add to cart").click()

    def open_cart(self):
        self.cart_link.click()
