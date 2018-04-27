from pages.base_page import BasePage
from pages.bytovaya_himiya_page import BytovayaHimiya


class GoodsHome(BasePage):
    portal_automatic = None
    bytovaya_himiya_link = None

    def __init__(self, _drv):
        super().__init__(_drv)
        self.portal_automatic = self.w_xpath('//div[@class="portal-automatic"]')
        self.bytovaya_himiya_link = self.w_xpath('//a[@href="https://rozetka.com.ua/ua/bytovaya-himiya/c4429255/"]')

    def open_bytovaya_himiya(self):
        self.close_popup()
        self.bytovaya_himiya_link.click()
        return BytovayaHimiya(self.drv)
