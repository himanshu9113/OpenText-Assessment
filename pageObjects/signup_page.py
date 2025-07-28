from playwright.sync_api import Page
import time

class SignupPage:
    def __init__(self, page: Page):
        self.page = page
        self.accept_cookies_btn = page.locator("#onetrust-accept-btn-handler")
        self.email_input = page.get_by_placeholder("Provide your email address")
        self.confirm_email_input = page.get_by_placeholder("Confirm your email")
        self.password_input = page.get_by_placeholder("Create a password")
        self.confirm_password_input = page.get_by_placeholder("Confirm your password")
        self.country_dropdown = page.get_by_role("button", name="form select button")
        self.country_input = page.get_by_placeholder("United States")
        self.canada_option = page.locator('button[aria-label="form select 2 button"]', has_text="Canada")
        self.submit_button = page.get_by_role("button", name="Claim Free Trial")
        self.recaptcha_frame = page.frame_locator("iframe[title='reCAPTCHA']")
        self.erroremail_message = page.get_by_text("Email must match confirm email")
        self.errorpassword_message = page.get_by_text("The Confirm password field must match the Password field.")
        self.errorPassReq_message = page.get_by_text("At least 8 characters are required for Password!")

    def open(self):
        self.page.goto("https://www.carbonite.com/backup-software/safe-personal-trial/")
        assert "Carbonite" in self.page.title()

    def accept_cookies(self):
        if self.accept_cookies_btn.is_visible():
            self.accept_cookies_btn.click()

    def fill_form(self, email, password, confirm_email = None, confirm_password = None):
        self.email_input.fill(email)
        if (confirm_email == None):
            self.confirm_email_input.fill(email)
        else:
            self.confirm_email_input.fill(confirm_email)
        self.password_input.fill(password)
        if (confirm_password == None):
            self.confirm_password_input.fill(password)
        else:
            self.confirm_password_input.fill(confirm_password)

    def select_country(self):
        self.country_dropdown.click()
        self.country_input.fill("Canada")
        self.canada_option.click()

    def mock_recaptcha(self):
        self.recaptcha_frame.locator("#recaptcha-token").evaluate("el => el.value = 'mock-valid-recaptcha-token'")
        self.recaptcha_frame.locator("#recaptcha-anchor").click()

    def submit(self):
        self.submit_button.click()
