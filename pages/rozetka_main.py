from selenium.webdriver.remote.webelement import WebElement

from pages.base_page import BasePage
from pages.goods_home_page import GoodsHome
from pages.smart_tv_devises_link_page import  SmartTvDevises


class RozetkaMain(BasePage):


    m_main = None
    smart_tv_devises_link = ""
    goods_home_link = ""

    def __init__(self, _drv):
        super().__init__(_drv)
        self.__url__ = "https://rozetka.com.ua"


    def load_page(self):
        self.drv.get(self.__url__)
        self.m_main = self.w_xpath("//nav[@class='m-main']", timeout=10)
        self.smart_tv_devises_link =  self.w_xpath("//a[contains(@href,'telefony-tv-i-ehlektronika')][@name='fat_menu_link']", timeout=10)
        self.goods_home_link =  self.w_xpath("//a[contains(@href,'tovary-dlya-doma')][@name='fat_menu_link']", timeout=10)

        return self


    def open_smart_tv_devises(self):
        self.smart_tv_devises_link.click()
        self.close_popup()
        return SmartTvDevises(self.drv)

    def open_tovary_dlya_doma(self):
        self.goods_home_link.click()
        self.close_popup()
        return GoodsHome(self.drv)
