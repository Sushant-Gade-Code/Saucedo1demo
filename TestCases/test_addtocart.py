import time

import pytest

from PageObjects.LogInPage import LogInPage
from PageObjects.addtocartpage import AddToCartPage
from Utilities.Readproperties import Readproperties
from Utilities.loggen import LoGenretor


class Test_add_To_cart:
    url = Readproperties.getUrl()
    username = Readproperties.getUsername()
    password = Readproperties.getPassword()
    log = LoGenretor.getLoggen()
    aList=["Sauce Labs Backpack","Sauce Labs Bike Light","Sauce Labs Bolt T-Shirt","Sauce Labs Fleece Jacket","Sauce Labs Onesie","Test.allTheThings() T-Shirt (Red)"]
    # aList=Readproperties.getList()
    @pytest.mark.regression()
    def test_add_to_cart_003(self,setup):
        self.log.info("TestCase test_add_to_cart_003 Started...!")
        self.driver=setup
        self.driver.get(self.url)
        self.log.info("Initializing the driver is Done...!")
        self.lp=LogInPage(self.driver)
        self.driver.implicitly_wait(10)
        self.lp.getUsername(self.username)
        self.log.info("Getting user name is sucessfully!...!")
        self.lp.getPassword(self.password)
        self.log.info("Getting user Password is sucessfully!...!")
        self.lp.getLogInButton()
        self.log.info("Getting Login Button is sucessfully!...!")
        self.lp2=AddToCartPage(self.driver)
        try:
            self.lp2.geteProductName(self.aList[5])
            self.log.info("Passing Product name is sucessfully!...!")

        except:
            None
        self.lp2.getBntaddCard()
        self.log.info("Getting BntaddCard is sucessfully!...!")
        self.lp2.getlinkShoppingCard()
        self.log.info("Getting linkShoppingCard is sucessfully!...!")
        time.sleep(5)
        self.act_title=self.lp2.gettitleofproductadd()
        self.log.info("Capturing Title of the page is sucessfully!...!")
        self.exp_title=self.aList[5]
        self.log.info("Capturing expected Title of the page is sucessfully!...!")
        if self.act_title==self.exp_title:
            self.log.info("TestCase test_add_to_cart_003 Passs...!")
            self.driver.save_screenshot(".\\Screenshts\\test_add_to_cart_003_Passs.png")
            self.log.info("Capturing Screenshots is sucessfully...!")
            assert True
            self.driver.close()

        else:
            self.log.info("TestCase test_add_to_cart_003 Passs...!")
            self.driver.save_screenshot(".\\Screenshts\\test_add_to_cart_003_Failed.png")
            self.log.info("Capturing Screenshots is sucessfully...!")
            self.driver.close()
            assert False



