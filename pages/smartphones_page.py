from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from pages.base_page_goods import BasePageGoods


class Smartphones(BasePageGoods):

    def __init__(self, _drv):
        super().__init__(_drv)


    def get_goods_names_on_page(self, pageN):
        self.close_rz()
        r =[]

        q = self.w_xpathes(self.xpath_goods_names, 10)
        r.extend(list(map(lambda e: e.text + "\n", q)))

        for N in range(2,6):
            self.w_xpath(self.xpath_page.format(N)).click()
            sleep(3)
            q = self.w_xpathes(self.xpath_goods_names,10)
            r.extend(list(map(lambda e : e.text+"\n", q)))
        return  r

    def get_top_goods(self, maxPage, By=None):
        self.close_rz()
        rt, rp  =[], []

        titles = "//div[@id='catalog_goods_block']//div[@class='g-i-tile-i-box']//i[@name='prices_active_element_original'][contains(@class, 'g-tag-icon-middle-popularity')]/../../..//div[@class='g-i-tile-i-title clearfix']"
        prises = "//div[@id='catalog_goods_block']//div[@class='g-i-tile-i-box']//i[@name='prices_active_element_original'][contains(@class, 'g-tag-icon-middle-popularity')]/../../..//div[contains(@class,'g-price-uah')]"

        qt = self.w_xpathes(titles, 2)
        qp = self.w_xpathes(prises, 2)

        if qt is not None:
            rt.extend(list(map(lambda e: e.text.encode("utf8"), qt)))
            rp.extend(list(map(lambda e: e.text, qp)))

        for N in range(2, maxPage+1):
            self.w_xpath(self.xpath_page.format(N)).click()
            sleep(3)
            qt = self.w_xpathes(titles, 2)
            qp = self.w_xpathes(prises, 2)

            if qt is not None :
                rt.extend(list(map(lambda e: e.text.encode("utf8"), qt)))
                rp.extend(list(map(lambda e: e.text, qp)))

        r=[]
        for i in range(len(rt)):
            r.append((rt[i],rp[i]))

        return r

    def get_in_price(self, maxPage):
        self.set_filter_price(3000, 6000)
        self.close_popup()
        rt, rp = [], []

        titles = "//div[@id='catalog_goods_block']//div[@class='g-i-tile-i-box']//div[@class='g-i-tile-i-title clearfix']"
        prises = "//div[@id='catalog_goods_block']//div[@class='g-i-tile-i-box']//div[contains(@class,'g-price-uah')]"

        qt = self.w_xpathes(titles, 2)
        qp = self.w_xpathes(prises, 2)

        rt.extend(list(map(lambda e: e.text, qt)))
        rp.extend(list(map(lambda e: e.text, qp)))

        for N in range(2, maxPage + 1):
            WebDriverWait(self.drv, 10).until(
                expected_conditions.element_to_be_clickable(
                    (By.XPATH, self.xpath_page.format(N)))). \
                click()
            sleep(4)
            qt = self.w_xpathes(titles, 2)
            qp = self.w_xpathes(prises, 2)

            if qt is not None:
                rt.extend(list(map(lambda e: e.text.encode("utf8"), qt)))
                rp.extend(list(map(lambda e: e.text, qp)))

        r = []
        for i in range(len(rt)):
            r.append((rt[i], rp[i]))

        return r


