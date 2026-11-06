import pytest
from playwright.sync_api import expect

from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage


@pytest.mark.smoke
def test_end_to_end_purchase(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()

    cart = CartPage(inventory_page.page)
    expect(cart.items).to_have_count(1)
    expect(cart.item_names).to_have_text("Sauce Labs Backpack")
    cart.start_checkout()

    checkout = CheckoutPage(inventory_page.page)
    checkout.fill_details("Swathy", "Shenoy", "6152")
    checkout.finish()
    expect(checkout.confirmation).to_have_text("Thank you for your order!")


@pytest.mark.regression
def test_checkout_requires_first_name(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    inventory_page.open_cart()
    CartPage(inventory_page.page).start_checkout()

    checkout = CheckoutPage(inventory_page.page)
    checkout.fill_details("", "Shenoy", "6152")
    expect(checkout.error).to_contain_text("First Name is required")
