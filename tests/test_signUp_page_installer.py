import time
from pageObjects.signup_page import SignupPage

email = f"E2E_test+{int(time.time())}@gmail.com"
password = f"E2E_test+{int(time.time())}"

def test_download_installer(page):
    signup = SignupPage(page)
    signup.open()
    signup.accept_cookies()
    signup.fill_form(email, password)
    signup.select_country()
    # ReCAPTCHA CANNOT BE CLICKED - JUST A WORKAROUND SOLUTION IF WE HAVE THE TOKEN
    signup.mock_recaptcha()
    signup.submit()
    # After clicking submit button the down load should start

def test_confirm_email_incorrect(page):
    signup = SignupPage(page)
    signup.open()
    signup.accept_cookies()
    signup.fill_form(email, password, 'XYZ', None)
    signup.select_country()
    signup.submit()
    assert signup.erroremail_message.inner_text() == "Email must match confirm email"

def test_confirm_password_incorrect(page):
    signup = SignupPage(page)
    signup.open()
    signup.accept_cookies()
    signup.fill_form(email, password, None, 'ABCD')
    signup.select_country()
    signup.submit()
    assert signup.errorpassword_message.inner_text() == "The Confirm password field must match the Password field."

def test_password_requirement_not_fulfilled(page):
    signup = SignupPage(page)
    signup.open()
    signup.accept_cookies()
    signup.fill_form(email, "1234")
    signup.select_country()
    signup.submit()
    assert signup.errorPassReq_message.inner_text() == "At least 8 characters are required for Password!"
    
