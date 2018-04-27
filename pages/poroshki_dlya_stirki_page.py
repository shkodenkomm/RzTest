from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page_goods import BasePageGoods


class PoroshkiDlyaStirki(BasePageGoods):

    def __init__(self, _drv):
        super().__init__(_drv)
        self.catalog_title_block  = self.w_xpath('//div[@id="catalog_title_block"]')

    def get_poroshki_za_100_300(self):
        self.set_filter_price(100,300)
        self.close_popup()

        r=[]

        for pageN in range(1,6):

            WebDriverWait(self.drv, 10).until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, self.xpath_page.format(pageN)))).\
            click()

            sleep(3)
            q = self.w_xpathes(self.xpath_goods_names,10)
            r.extend(list(map(lambda e : e.text, q)))

        return  r


