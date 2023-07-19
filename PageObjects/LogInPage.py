from selenium import webdriver
from selenium.webdriver.common.by import By


class LogInPage:
    text_Username_ID="user-name"
    text_Password_ID="password"
    button_Login_id="login-button"
    menu_button_id="react-burger-menu-btn"
    button_Login_XPATH='//a[text()="Logout"]'
    span_product_text='//span[@class="title"]'

    def __init__(self,driver):
        self.driver=driver

    def getUsername(self,Username):
        self.driver.find_element(By.ID, self.text_Username_ID).clear()
        self.driver.find_element(By.ID,self.text_Username_ID).send_keys(Username)

    def getPassword(self,Password):
        self.driver.find_element(By.ID, self.text_Password_ID).clear()
        self.driver.find_element(By.ID, self.text_Password_ID).send_keys(Password)

    def getLogInButton(self):
        self.driver.find_element(By.ID, self.button_Login_id).click()

    def getMenuButton(self):
        self.driver.find_element(By.ID, self.menu_button_id).click()

    def getLogout(self):
        self.driver.find_element(By.XPATH, self.button_Login_XPATH).click()

    def getText(self):
        act_title=self.driver.find_element(By.XPATH, self.span_product_text).text
        return act_title



