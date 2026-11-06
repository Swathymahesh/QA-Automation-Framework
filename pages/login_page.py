from playwright.sync_api import Page


class LoginPage:
    """Page object for the login screen."""

    def __init__(self, page: Page, base_url: str):
        self.page = page
        self.base_url = base_url
        self.username = page.locator("#user-name")
        self.password = page.locator("#password")
        self.submit = page.locator("#login-button")
        self.error = page.locator('[data-test="error"]')

    def open(self):
        self.page.goto(self.base_url)
        return self

    def login(self, username: str, password: str):
        self.username.fill(username)
        self.password.fill(password)
        self.submit.click()
