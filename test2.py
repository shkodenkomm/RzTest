
from datetime import datetime

from selenium import webdriver

import utils
from pages.rozetka_main import RozetkaMain
from paramcase.ParamsTestCase import ParamsTestCase
import logging


class PoroshkiDlyaStirkiList(ParamsTestCase):
    @classmethod
    def setUpClass(cls):

        cls.drv = webdriver.Chrome()
        cls.drv.set_window_size(1900, 1050)
        cls.drv.set_window_position(-1900, 0)
        cls.drv.implicitly_wait(2)

        cls.log = logging.getLogger('messages')
        cls.log.setLevel(logging.DEBUG)
        cls.ch = logging.FileHandler("messages.log", mode='w')
        cls.ch.setLevel(logging.DEBUG)
        formatter = logging.Formatter('[%(asctime)s-%(name)s-%(levelname)s]: %(message)s')
        cls.ch.setFormatter(formatter)
        cls.log.addHandler(cls.ch)

    @classmethod
    def tearDownClass(cls):
        cls.drv.close()

    def test1_open_rozetka(self):
        """зайти на сайт rozetka.com.ua """
        rm = RozetkaMain(self.drv).load_page()
        self.assertIsNotNone(rm.m_main)
        self.parent_suite.params.update({"rm": rm})

    def test2_open_tovary_dlya_doma(self):
        """перейти в раздел 'Товары для дома'"""
        self.assertTrue("rm" in self.parent_suite.params)
        rm = self.parent_suite.params["rm"]

        tdm = rm.open_tovary_dlya_doma()
        self.assertIsNotNone(tdm.portal_automatic)

        self.parent_suite.params.update({"tdm": tdm})

    def test3_open_bytovaya_himiya(self):
        """перейти в раздел 'Бытовая химия'"""
        self.assertTrue("tdm" in self.parent_suite.params)
        tdm = self.parent_suite.params["tdm"]

        bhm = tdm.open_bytovaya_himiya()
        self.assertIsNotNone(bhm.portal_automatic)

        self.parent_suite.params.update({"bhm": bhm})

    def test4_open_sredstva_dlya_stirki(self):
        """перейти в раздел 'Для стирки'"""
        self.assertTrue("bhm" in self.parent_suite.params)
        bhm = self.parent_suite.params["bhm"]

        sds = bhm.open_sredstva_dlya_stirki()
        self.assertIsNotNone(sds.catalog_title_block)

        self.parent_suite.params.update({"sds": sds})

    def test5_open_poroshki_dlya_stirki(self):
        """перейти в раздел 'Порошки для стирки'"""
        self.assertTrue("sds" in self.parent_suite.params)
        sds = self.parent_suite.params["sds"]

        pds = sds.open_poroshki_dlya_stirki()
        self.assertIsNotNone(pds.catalog_title_block)

        self.parent_suite.params.update({"pds": pds})

    def test6_get_poroshki_za_100_300(self):
        """выбрать из первых пяти страниц поисковой выдачи название и цены всех товаров в диапазоне от 100 до 300 гривен"""
        self.assertTrue("pds" in self.parent_suite.params)
        pds = self.parent_suite.params["pds"]

        r = pds.get_poroshki_za_100_300()
        self.assertGreater(len(r),0)

        self.parent_suite.params.update({"rlist": r})

    def test7_save_to_db(self):
        """записать полученные результаты в базу данных"""
        self.assertTrue("rlist" in self.parent_suite.params)

        id = None

        id = utils.save_to_db({"date": datetime.now(),
                               "results":self.parent_suite.params["rlist"]
                               })

        self.assertIsNotNone(id)
        self.log.info(str(id.inserted_id))









