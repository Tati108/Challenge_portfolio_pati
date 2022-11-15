import time
from pages.base_page import BasePage


class Dashboard(BasePage):
    button_login_xpath = "//*[@id='login']"
    login_xpath = "//label[@id='login-label']"
    login_label_xpath = "//label[text()='Login']"
    button_password_xpath = "//*[@id='password']"
    password_xpath = "//label[@id='password-label']"
    password_label_xpath = "//label[text()='Password']"
    remind_password_hyperlink_xpath = "//*[@id='__next']/form/div/div[1]/a"
    remind_password_xpath = "//*[text()='Remind password']"
    sign_in_hyperlink_xpath = "//span[@class='MuiButton-label']"
    change_language_xpath = "//div[@role='button']"
    scouts_panel_xpath = "//h5[text()='Scouts Panel']"


