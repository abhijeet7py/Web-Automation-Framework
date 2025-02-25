# Login page class
# respons -->
# get username and send keys - email
# get password and send keys - password
# click the submit button and navigate to dashboard
# Invalid--> error message
# Forget password

# Page Class

# Page locators
# Page Actions
# Webdriver init
# Custom functions
# No assertions (Page object class)

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LoginPage:
    def __init__(self,driver):
        self.driver = driver

    # Page locator
    username = (By.ID,"login-username")
    password = (By.NAME,"password")
    submit_button = (By.XPATH,"//button[@id='js-login-btn']")
    # forgot_pw_button = (By.XPATH,"//button[@class='btn btn--link btn--primary Td(u) Fz(12px)']")
    error_msg = (By.CSS_SELECTOR,"#js-notification-box-msg")
    # free_trial = (By.LINK_TEXT,"Start a free trial")
    # remember_checkbox = (By.XPATH,"//input[@id='checkbox-remember']")
    # sso_login  = (By.XPATH,"//button[normalize-space()='Sign in using SSO']")

    # Page Actions
    def get_username(self):
        return self.driver.find_element(*LoginPage.username)

    def get_password(self):
        return self.driver.find_element(*LoginPage.password)

    def get_submit_button(self):
        return self.driver.find_element(*LoginPage.submit_button)

    def get_error_msg(self):
        return self.driver.find_element(*LoginPage.error_msg)

    # def get_free_trial(self):
    #     return self.driver.find_element(*LoginPage.free_trial)

    def login_to_vwo(self,usr,pwd):
        self.get_username().send_keys(usr)
        self.get_password().send_keys(pwd)
        self.get_submit_button().click()

    def get_error_msg_text(self):
        return self.get_error_msg_text().text

    # def click_free_trial(self):
    #     return self.get_free_trail().click()

