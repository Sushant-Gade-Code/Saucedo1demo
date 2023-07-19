from selenium.webdriver.common.by import By


class GetorderPage:
    btn_checkout_by_XPATH='//button[text()="Checkout"]'
    input_First_Name_by_XPATH='//input[@id="first-name"]'
    input_LAst_Name_By_XPATH='//input[@id="last-name"]'
    input_zip_code_XPATH='//input[@id="postal-code"]'
    btn_get_conti_XPATH='//input[@id="continue"]'
    btn_Finsh_By_XPATH='//button[@class="btn btn_action btn_medium cart_button"]'
    title_by_XPATH='//div[@class="checkout_complete_container"]//h2'

    def __init__(self,setup):
        self.driver=setup

    def getcheckoutbtn(self):
        self.driver.find_element(By.XPATH,self.btn_checkout_by_XPATH).click()

    def getFistname(self,name):
        self.driver.find_element(By.XPATH, self.input_First_Name_by_XPATH).clear()
        self.driver.find_element(By.XPATH, self.input_First_Name_by_XPATH).send_keys(name)

    def getLastName(self,LastName):
        self.driver.find_element(By.XPATH, self.input_LAst_Name_By_XPATH).clear()
        self.driver.find_element(By.XPATH, self.input_LAst_Name_By_XPATH).send_keys(LastName)

    def getzipcode(self,code):
        self.driver.find_element(By.XPATH, self.input_zip_code_XPATH).clear()
        self.driver.find_element(By.XPATH, self.input_zip_code_XPATH).send_keys(code)

    def getContinueBtn(self):
        self.driver.find_element(By.XPATH, self.btn_get_conti_XPATH).click()


    def getFinshbtn(self):
        self.driver.find_element(By.XPATH, self.btn_Finsh_By_XPATH).click()

    def get_title(self):
       act_title=self.driver.find_element(By.XPATH, self.title_by_XPATH).text
       return act_title







