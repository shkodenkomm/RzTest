from pages.base_page import BasePage
from pages.poroshki_dlya_stirki_page import PoroshkiDlyaStirki


class SredstvaDlyaStirki(BasePage):
    portal_automatic = None
    poroshki_dlya_stirki_link = ""

    def __init__(self, _drv):
        super().__init__(_drv)
        self.catalog_title_block = self.w_xpath('//div[@id="catalog_title_block"]')
        self.poroshki_dlya_stirki_link = self.w_xpath('//a[@href="https://rozetka.com.ua/ua/sredstva-dlya-stirki4632103/c4632103/"]')

    def open_poroshki_dlya_stirki(self):
        self.poroshki_dlya_stirki_link.click()
        return PoroshkiDlyaStirki(self.drv)