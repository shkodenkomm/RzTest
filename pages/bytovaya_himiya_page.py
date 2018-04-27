from pages.base_page import BasePage
from pages.sredstva_dlya_stirki_page import SredstvaDlyaStirki


class BytovayaHimiya(BasePage):
    portal_automatic = None
    sredstva_dlya_stirki_link = ""

    def __init__(self, _drv):
        super().__init__(_drv)
        self.portal_automatic = self.w_xpath('//div[@class="portal-automatic"]')
        self.sredstva_dlya_stirki_link = self.w_xpath('//a[@href="https://rozetka.com.ua/ua/sredstva-dlya-stirki/c4625084/"]')

    def open_sredstva_dlya_stirki(self):
        self.sredstva_dlya_stirki_link.click()
        return SredstvaDlyaStirki(self.drv)