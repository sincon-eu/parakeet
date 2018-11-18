import os
from configparser import ConfigParser
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class ParkingALot():

    def __init__(self, order: bool=False, parking_id_to_click: str="offer-obc-parking-pkp-2018-12"):
        self.order = order
        self.chrome_browser = webdriver.Chrome(executable_path='src/webdriver/chromedriver.exe',
                                               chrome_options=None)
        self.parking_id_to_click = parking_id_to_click

    def click_by_id(self, elem_id: str) -> None:
        element_to_click = self.chrome_browser.find_elements_by_id(elem_id)
        element_to_click[0].click()

    def fill_element(self, elem_id: str, text: str) -> None:
        input_element = self.chrome_browser.find_element_by_id(elem_id)
        input_element.send_keys(text)

    def check_if_loaded(self, elem_id: str, timeout: int = 2) -> bool:
        try:
            WebDriverWait(self.chrome_browser, timeout).until(EC.visibility_of_element_located((By.ID, elem_id)))
            return True
        except TimeoutException:
            print(f'Unable to find, {elem_id}')
        except Exception as e:
            print({e})
        return False

    def main(self, order=False, *args, **kwargs):

        # tile_id_to_click = "offer-obc-parking-pkp-2018-12"
        cfg_ = ConfigParser()
        cfg_.optionxform = str
        # todo join it with os.path
        cfg_.read(os.path.join(os.path.dirname(__file__), 'src/config/main_conf.ini'))

        personal = dict(cfg_.items('Personal'))
        invoice = dict(cfg_.items('Invoice'))
        clickables = dict(cfg_.items('Clickables'))

        self.chrome_browser.get("https://go.parkanizer.com/#/offers")

        while not self.check_if_loaded(self.parking_id_to_click, timeout=2):
            self.check_if_loaded(self.parking_id_to_click, timeout=2)

        # skip main page
        self.click_by_id(self.parking_id_to_click)
        self.click_by_id(clickables['cookie_btn'])
        self.click_by_id(clickables['go_buy_form_id'])

        # fill textboxes
        self.check_if_loaded(personal['name'], timeout=2)

        for k, v in personal.items():
            self.fill_element(k, v)

        self.click_by_id(clickables['invoice_btn'])
        self.click_by_id(clickables['personal_data_btn'])
        self.click_by_id(clickables['terms_btn'])
        self.click_by_id(clickables['parking_terms_btn'])

        for k, v in invoice.items():
            self.fill_element(k, v)

        self.click_by_id(clickables['buy_subscription_btn'])

        # watch out for this
        if order:
            self.click_by_id(clickables['buy_with_payment_obligation'])

if __name__ == '__main__':

    # expected value :p PRODUCTION
    # parking_id_to_click = "offer-obc-f-2019-01"
    # park_my_car = ParkingALot(order=True, parking_id_to_click)

    # debug
    park_my_car = ParkingALot(order=False)
    park_my_car.main()
