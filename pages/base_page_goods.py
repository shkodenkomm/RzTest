from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage


class BasePageGoods(BasePage):
    paginator = None
    xpath_goods_names = ""
    xpath_page = ""

    def __init__(self, _drv):
        super().__init__(_drv)
        self.paginator = self.w_xpath('//ul[@name="paginator"]')
        self.xpath_goods_names = '//div[@id="catalog_goods_block"]/div//div[@class="g-i-tile-i-title clearfix"]/a'
        self.xpath_page = '//li[@id="page{0}"]'


    def set_filter_price(self, min,max):
        inpmin = self.w_xpath("//input[@id='price[min]']")
        inpmax = self.w_xpath("//input[@id='price[max]']")
        button =self.w_id("submitprice")


        inpmin.send_keys(str(min))
        inpmax.click()

        inpmax.send_keys(Keys.END)
        for i in range(10):
            inpmax.send_keys(Keys.BACKSPACE)
        inpmax.send_keys(str(max))

        button.click()

        self.w_id("reset_filterprice",10)



