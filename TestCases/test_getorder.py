import time
import random
import string

import pytest

from PageObjects.GetorderPage import GetorderPage
from PageObjects.LogInPage import LogInPage
from PageObjects.addtocartpage import AddToCartPage
from Utilities.Readproperties import Readproperties
from Utilities.loggen import LoGenretor

class Test_GetOrder:
    url = Readproperties.getUrl()
    username = Readproperties.getUsername()
    password = Readproperties.getPassword()
    log = LoGenretor.getLoggen()
    aList = ["Sauce Labs Backpack", "Sauce Labs Bike Light", "Sauce Labs Bolt T-Shirt", "Sauce Labs Fleece Jacket",
             "Sauce Labs Onesie", "Test.allTheThings() T-Shirt (Red)"]


    @pytest.mark.regression()
    def test_get_order__005(self,setup):
        self.log.info("Testcase test_get_order__005 is Started...!")
        self.driver = setup
        self.driver.get(self.url)
        self.log.info("Getting the Url Is sucessfully...!")
        self.lp = LogInPage(self.driver)
        self.driver.implicitly_wait(10)
        self.lp.getUsername(self.username)
        self.log.info("Getting the Username Is sucessfully...!")
        self.lp.getPassword(self.password)
        self.log.info("Getting the Password Is sucessfully...!")
        self.lp.getLogInButton()
        self.log.info("Getting the LagButoon Is sucessfully...!")
        self.lp2 = AddToCartPage(self.driver)
        try:
            self.lp2.geteProductName(self.aList[5])
            self.log.info("Passing the product name Is sucessfully...!")

        except:
            None
        self.lp2.getBntaddCard()
        self.log.info("Getting the BntaddCard Is sucessfully...!")
        self.lp2.getlinkShoppingCard()
        self.log.info("Getting the linkShoppingCard Is sucessfully...!")
        time.sleep(5)
        self.lp3=GetorderPage(self.driver)
        self.lp3.getcheckoutbtn()
        self.log.info("Getting the Checkoutbtn Is sucessfully...!")
        self.name = random_generator()+"abcd"
        self.lp3.getFistname(self.name)
        self.log.info("Getting the Firstname randomly Is sucessfully...!")
        self.lastname = random_generator()+"fgdjsks"
        self.lp3.getLastName(self.lastname)
        self.log.info("Getting the LastName Firstname randomly Is sucessfully...!")
        self.zipcd = random_generator()+"24363882"
        self.lp3.getzipcode( self.zipcd )
        self.log.info("Getting the Zipcode randomly Is sucessfully...!")
        self.lp3.getContinueBtn()
        self.log.info("Getting the ContinueBtn Is sucessfully...!")
        self.lp3.getFinshbtn()
        self.log.info("Getting the Finshbtn Is sucessfully...!")
        act_title=self.lp3.get_title()
        self.log.info("Getting the act_title Is sucessfully...!")
        exp_title='Thank you for your order!'
        if act_title==exp_title:
            self.log.info("Testcase test_get_order__005 Passed")
            self.driver.save_screenshot(".\\Screenshts\\test_get_order__005_passed.png")
            self.log.info("Getting the screenshots Is sucessfully...!")
            assert True
            self.driver.close()
        else:
            self.log.info("Testcase test_get_order__005 Failed")
            self.driver.save_screenshot(".\\Screenshts\\test_get_order__005_failed.png")
            self.log.info("Getting the screenshots Is sucessfully...!")
            self.driver.close()
            assert False


def random_generator(size=8, chars=string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for x in range(size))

