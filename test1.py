import logging
import os
import smtplib

from selenium import webdriver
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

import utils
from pages.rozetka_main import RozetkaMain
from paramcase.ParamsTestCase import ParamsTestCase


class SmartphonesList(ParamsTestCase):
    @classmethod
    def setUpClass(cls):

        cls.drv = webdriver.Chrome()
        cls.drv.set_window_size(1200, 700)
        cls.drv.set_window_position(0, 0)
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

    def test1_open_main_page(self):
        """зайти на сайт rozetka.com.ua"""
        rm =RozetkaMain(self.drv).load_page()
        self.assertIsNotNone(rm.m_main)
        self.parent_suite.params.update({"rm":rm})

    def test2_open_phones_tv_other(self):
        """перейти в раздел "Телефоны, ТВ и электроника"""
        self.assertTrue( "rm" in self.parent_suite.params)
        rm = self.parent_suite.params["rm"]

        tte = rm.open_smart_tv_devises()
        self.assertIsNotNone(tte.telefony_link)

        self.parent_suite.params.update({"tte": tte})

    def test3_open_phones(self):
        """перейти в раздел 'Телефоны' """
        self.assertTrue("tte" in self.parent_suite.params)
        tte = self.parent_suite.params["tte"]

        ph = tte.open_phones()
        self.assertIsNotNone(ph.portal_automatic)

        self.parent_suite.params.update({"ph": ph})

    def test4_open_smartphones(self):
        """перейти в раздел 'Смартфоны'"""
        self.assertTrue("ph" in self.parent_suite.params)
        ph = self.parent_suite.params["ph"]

        smarts = ph.open_smarts()
        self.assertIsNotNone(smarts.paginator)

        self.parent_suite.params.update({"smarts": smarts})

    def test5_get_devises_names(self):
        """ выбрать из первых трех страниц поисковой выдачи название всех девайсов
            записать полученные результаты в текстовый файл
        """
        self.assertTrue("smarts" in self.parent_suite.params)
        smarts = self.parent_suite.params["smarts"]

        devises_names = smarts.get_goods_names_on_page(3)

        self.assertGreater(len(devises_names),0)

        lenFile = 0
        file_path = "test-reports\\devises_names.txt"
        with open(file_path, encoding="utf-8", mode="w") as f :
            f.writelines(devises_names)


        if os.path.exists(file_path):
            lenFile = os.path.getsize(file_path)

        self.assertGreater(lenFile,0)

        self.parent_suite.params.update({"smart_file": file_path})

    def test6_sand_emails(self):
        """  отправить данный файл по списку рассылки (e-mails из отдельного файла) """
        self.assertTrue("smart_file" in self.parent_suite.params)
        file_path = self.parent_suite.params["smart_file"]

        with open(file_path, mode="r", encoding="utf8") as f :
            body_text = f.read()
            utils.send_mail(body_text)

    def get_top_smart_title_price(self):
        """ выбрать из первых трех страниц поисковой выдачи название и цены всех девайсов,
            обозначенных как “Топ продаж”
        """
        self.assertTrue("smarts" in self.parent_suite.params)
        smarts = self.parent_suite.params["smarts"]

        si = smarts.get_top_goods(3)
        self.assertGreater(len(si),0)

        self.parent_suite.params.update({"smart_top": si})

    def get_smart_title_price_3000_6000(self):
        """ выбрать из первых пяти страниц поисковой выдачи название и цены всех товаров в диапазоне от 3000 до 6000 гривен"""
        self.assertTrue("smarts" in self.parent_suite.params)
        smarts = self.parent_suite.params["smarts"]

        si = smarts.get_in_price(5)
        self.assertGreater(len(si),0)
        self.log.info(str(si))






