import time

import allure
import pytest
from selenium import webdriver
from Tests.PageObjects.loginPage import LoginPage
from Tests.PageObjects.dashboardPage import DashboardPage

# Assertions

@pytest.fixture()
def setup():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://app.vwo.com/#/login")
    return driver

@allure.epic("VWO login test")
@allure.feature("TC#0 - VWO app negative test")
@pytest.mark.negative
def test_vwo_login_negative(setup):
    driver = setup
    loginpage = LoginPage(driver)
    loginpage.login_to_vwo(usr="admin@gmail.com",pwd="admin@123")
    time.sleep(5)
    error_message = loginpage.get_error_msg_text()
    assert error_message == "Your email, password, IP address or location did not match"


@allure.epic("VWO login test")
@allure.feature("TC#1 - VWO app Positive test")
@pytest.mark.positive
def test_vwo_login_positive(setup):
    driver = setup
    loginpage = LoginPage(driver)
    loginpage.login_to_vwo(usr="abhijeet123@gmail.com",pwd="Abhijeet@0709")
    time.sleep(5)
    dashboard = DashboardPage(driver)
    assert "Dashboard" in driver.title
    assert "a" in dashboard.user_loggeedin_text()
    # assert  True == True