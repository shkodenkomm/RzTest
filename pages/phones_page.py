from pages.base_page import BasePage
from pages.smartphones_page import Smartphones


class Phones(BasePage):
    portal_automatic = None
    smarts_link = None

    def __init__(self, _drv):
        super().__init__(_drv)
        self.portal_automatic = self.w_xpath('//div[@class="portal-automatic"]')
        self.smarts_link = self.w_xpath('//a[@href="https://rozetka.com.ua/ua/mobile-phones/c80003/filter/preset=smartfon/"]')

    def open_smarts(self):
        self.smarts_link.click()
        return Smartphones(self.drv)

