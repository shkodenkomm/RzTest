import sys

import xmlrunner

import utils
from test1 import SmartphonesList
from paramcase.ParamsTestSuite import ParamsTestSuite
from test2 import PoroshkiDlyaStirkiList


def run():
    runner = xmlrunner.XMLTestRunner(output='test-reports',
                                     verbosity=3,
                                    stream= sys.stdout)
    suite = ParamsTestSuite()

    if sys.argv[1] == "test1":
        suite.addTest(SmartphonesList("test1_open_main_page"))
        suite.addTest(SmartphonesList("test2_open_phones_tv_other"))
        suite.addTest(SmartphonesList("test3_open_phones"))
        suite.addTest(SmartphonesList("test4_open_smartphones"))
        suite.addTest(SmartphonesList("test5_get_devises_names"))
        suite.addTest(SmartphonesList("test6_sand_emails"))

    elif sys.argv[1] == "test2":
        suite.addTest(PoroshkiDlyaStirkiList("test1_open_rozetka"))
        suite.addTest(PoroshkiDlyaStirkiList("test2_open_tovary_dlya_doma"))
        suite.addTest(PoroshkiDlyaStirkiList("test3_open_bytovaya_himiya"))
        suite.addTest(PoroshkiDlyaStirkiList("test4_open_sredstva_dlya_stirki"))
        suite.addTest(PoroshkiDlyaStirkiList("test5_open_poroshki_dlya_stirki"))
        suite.addTest(PoroshkiDlyaStirkiList("test6_get_poroshki_za_100_300"))
        suite.addTest(PoroshkiDlyaStirkiList("test7_save_to_db"))

    elif sys.argv[1] == "test3":
        suite.addTest(SmartphonesList("test1_open_main_page"))
        suite.addTest(SmartphonesList("test2_open_phones_tv_other"))
        suite.addTest(SmartphonesList("test3_open_phones"))
        suite.addTest(SmartphonesList("test4_open_smartphones"))
        suite.addTest(SmartphonesList("get_top_smart_title_price"))
        suite.addTest(SmartphonesList("get_smart_title_price_3000_6000"))
        suite.addTest(SmartphonesList("set_info_to_xlsm_mail"))


    runner.run(suite)

if __name__ =='__main__':
    utils.params = utils.get_params()
    run()