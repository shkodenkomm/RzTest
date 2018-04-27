from selenium.webdriver.chrome import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage():
    #drv = webdriver.Chrome()

    def w_xpathes(self, xpath, timeout=5):
        try:
            elements = WebDriverWait(self.drv, timeout).until(
                expected_conditions.presence_of_all_elements_located(
                    (By.XPATH, xpath)))
            return elements
        except:
            return  None


    def w_xpath(self, xpath, timeout=5):
        try:
            element = WebDriverWait(self.drv, timeout).until(
                expected_conditions.presence_of_element_located(
                    (By.XPATH, xpath)))
            return element
        except:
            return  None

    def w_id(self, id, timeout=5):
        try:
            element = WebDriverWait(self.drv, timeout).until(
                expected_conditions.presence_of_element_located(
                    (By.ID, id)))
            return element
        except:
            return None

    def close_popup(self):
        self.close_rz()
        try:
            WebDriverWait(self.drv, 0.5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='popup-css lang-switcher-popup sprite-side']")))

            close_button = WebDriverWait(self.drv, 0.2).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[@name='close']")))

            close_button.click()

            WebDriverWait(self.drv, 0.2).until(
                expected_conditions.invisibility_of_element_located((By.XPATH, "//div[@class='popup-css lang-switcher-popup sprite-side']")))
        except:
            pass

    def close_rz(self):
        try:
            WebDriverWait(self.drv, 0.5).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//div[@class='rz-bg-main']")))

            close_button = WebDriverWait(self.drv, 0.2).until(
                expected_conditions.visibility_of_element_located((By.XPATH, "//a[@name='close']")))

            close_button.click()

            WebDriverWait(self.drv, 0.2).until(
                expected_conditions.invisibility_of_element_located((By.XPATH, "//div[@class='rz-bg-main']")))
        except:
            pass

    def __init__(self, _drv):
        self.drv = _drv


