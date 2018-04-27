from pages.base_page import BasePage
from pages.phones_page import Phones


class SmartTvDevises(BasePage):
    telefony_link = None

    def __init__(self, _drv):
        super().__init__(_drv)
        self.telefony_link = self.w_xpath("//ul[@id='menu_categories_left']//a[@href='https://rozetka.com.ua/ua/telefony/c4627900/']")

    def open_phones(self):
        self.telefony_link.click()
        return Phones(self.drv)