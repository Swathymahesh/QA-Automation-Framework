import pytest
from playwright.sync_api import expect


@pytest.mark.regression
def test_sort_by_name_a_to_z(inventory_page):
    inventory_page.sort_by("az")
    names = inventory_page.product_names()
    assert names == sorted(names)


@pytest.mark.regression
def test_sort_by_price_low_to_high(inventory_page):
    inventory_page.sort_by("lohi")
    prices = inventory_page.product_prices()
    assert prices == sorted(prices)


@pytest.mark.smoke
def test_adding_items_updates_cart_badge(inventory_page):
    inventory_page.add_to_cart("Sauce Labs Backpack")
    expect(inventory_page.cart_badge).to_have_text("1")
    inventory_page.add_to_cart("Sauce Labs Bike Light")
    expect(inventory_page.cart_badge).to_have_text("2")
