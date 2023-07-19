import time

from selenium.webdriver.common.by import By


class AddToCartPage:
    product_common_XPATH='//div[@class="inventory_list"]/div/div[2]/div/a'
    button_add_to_Card_XPATH='//button[@class="btn btn_primary btn_small btn_inventory"]'
    link_Shopping_Card_XPATH='//a[@class="shopping_cart_link"]'
    text_Inventory_item_XPATH='//div[@class="inventory_item_name"]'

    def __init__(self,driver):
        self.driver=driver

    def geteProductName(self,productname):
        all_product=self.driver.find_elements(By.XPATH,self.product_common_XPATH)
        for product in all_product:
            time.sleep(2)
            if product.text==productname:
                time.sleep(2)
                product.click()

    def getBntaddCard(self):
        self.driver.find_element(By.XPATH,self.button_add_to_Card_XPATH).click()

    def getlinkShoppingCard(self):
        self.driver.find_element(By.XPATH, self.link_Shopping_Card_XPATH).click()

    def gettitleofproductadd(self):
        product_text=self.driver.find_element(By.XPATH, self.text_Inventory_item_XPATH).text
        return product_text



