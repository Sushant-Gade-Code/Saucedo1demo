import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

from PageObjects.LogInPage import LogInPage
from Utilities.Readproperties import Readproperties
from Utilities.loggen import LoGenretor


class Test_Login:
    url=Readproperties.getUrl()
    username=Readproperties.getUsername()
    password=Readproperties.getPassword()
    log=LoGenretor.getLoggen()

    @pytest.mark.sanity()
    @pytest.mark.smoke()
    def test_HomePage_title__001(self,setup):
        self.log.info("Testcase test_HomePage_title__001")
        self.driver=setup
        self.driver.get(self.url)
        self.log.info("Initializing the driver Succesfully...!")
        act_title=self.driver.title
        exp_title="Swag Labs"
        self.log.info("Capturing Title is Succesfully...!")
        if act_title==exp_title:
            self.log.info("Testcase test_HomePage_title__001Passed...!")
            self.driver.save_screenshot(".\\Screenshts\\Testcase test_HomePage_title__001Passed.png")
            self.log.info("Capturing Title is Succesfully...!")
            assert True
            self.driver.close()
        else:
            self.log.info("Testcase test_HomePage_title__001Failed...!")
            self.driver.save_screenshot(".\\Screenshts\\Testcase test_HomePage_title__001Failed.png")
            self.log.info("Capturing Title is Succesfully...!")
            self.driver.close()
            assert False

    @pytest.mark.sanity()
    def test_Login__002(self,setup):
        self.log.info("Testcase test_Login__002")
        self.driver=setup
        self.log.info("Initializing the driver Succesfully...!")
        self.driver.get(self.url)
        self.lp=LogInPage(self.driver)
        self.lp.getUsername(self.username)
        self.log.info("Getting Username  is Succesfully...!")
        self.lp.getPassword(self.password)
        self.log.info("Getting Password  is Succesfully...!")
        self.lp.getLogInButton()
        self.log.info("Getting LogIn Button  is Succesfully...!")
        time.sleep(5)
        act_title=self.lp.getText()
        self.log.info("Capturing text  is Succesfully...!")
        exp_title="Products"
        if act_title==exp_title:
            self.log.info("Testcase test_Login__002Passed...!")
            self.driver.save_screenshot(".\\Screenshts\\Testcase test_Login__002pass.png")
            self.log.info("Capturing Title Is Successfully")
            assert True

        else:
            self.log.info("Testcase test_Login__002Failed...!")
            self.driver.save_screenshot(".\\Screenshts\\Testcase test_Login__002failed.png")
            self.log.info("Capturing Title Is Successfully")
            assert False
        self.lp.getMenuButton()
        self.log.info("Getting MenuButton  is Succesfully...!")
        time.sleep(5)
        self.lp.getLogout()
        self.log.info("Getting getLogout Button  is Succesfully...!")
        self.driver.close()

