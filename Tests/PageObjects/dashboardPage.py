# Dashboard class
# Verify the username
# Page Class
# Page Actions

from selenium import webdriver
from selenium.webdriver.common.by import By
class DashboardPage:
    def __init__(self,driver):
        self.driver = driver

    #Page locator
    user_logged_in = (By.XPATH,"//span[@data-qa='lufexuloga']")

    #Page Action
    def get_user_logged_in(self):
        return self.driver.find_element(*DashboardPage.user_logged_in)

    def user_loggeedin_text(self):
        return self.get_user_logged_in().text


