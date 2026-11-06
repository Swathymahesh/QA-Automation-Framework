from playwright.sync_api import Page


class CheckoutPage:
    """Page object covering the three checkout steps."""

    def __init__(self, page: Page):
        self.page = page
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.postal_code = page.locator('[data-test="postalCode"]')
        self.continue_button = page.locator('[data-test="continue"]')
        self.finish_button = page.locator('[data-test="finish"]')
        self.confirmation = page.locator(".complete-header")
        self.error = page.locator('[data-test="error"]')

    def fill_details(self, first: str, last: str, postcode: str):
        self.first_name.fill(first)
        self.last_name.fill(last)
        self.postal_code.fill(postcode)
        self.continue_button.click()

    def finish(self):
        self.finish_button.click()
