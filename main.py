from time import sleep

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

        cookie_btn = "confirm-cookie-consent"
        go_buy_form_id = "goToBuyForm"

        name_id = 'name'
        email_id = 'email'
        licence_id = 'primaryLicensePlate'

        invoice_btn = 'wantsAnInvoice'
        personal_data_btn = "acceptsPersonalDataTerms"
        terms_btn = "terms"
        parking_terms_btn = "parkingTerms"

        company_name = "companyName"
        company_address = "companyAddress"
        tax_number = "taxNumber"

        buy_subscription_btn = "buySubscriptionButton"

        # confirms order
        buy_with_payment_obligation = "buyWithPaymentObligation"

        # option = webdriver.ChromeOptions()
        # option.add_argument('— incognito')

        # browser = webdriver.Chrome(executable_path='src/webdriver/chromedriver.exe',
        #                            chrome_options=option)

        self.chrome_browser.get("https://go.parkanizer.com/#/offers")

        while not self.check_if_loaded(self.parking_id_to_click, timeout=2):
            self.check_if_loaded(self.parking_id_to_click, timeout=2)

        # skip main page
        self.click_by_id(self.parking_id_to_click)
        self.click_by_id(cookie_btn)
        self.click_by_id(go_buy_form_id)

        # fill textboxes
        self.check_if_loaded(name_id, timeout=2)
        self.fill_element(name_id, 'Franek ma parking')
        self.fill_element(email_id, 'jakis@email.com')
        self.fill_element(licence_id, 'GA123RR')

        self.click_by_id(invoice_btn)
        self.click_by_id(personal_data_btn)
        self.click_by_id(terms_btn)
        self.click_by_id(parking_terms_btn)

        self.fill_element(company_name, 'Weltmeister')
        self.fill_element(company_address, 'Planet \nEarth')
        self.fill_element(tax_number, 10 * '6')

        self.click_by_id(buy_subscription_btn)

        # watch out for this
        if order:
            self.click_by_id(buy_with_payment_obligation)

        a = 5


if __name__ == '__main__':

    # expected value :p PRODUCTION
    parking_id_to_click = "offer-obc-f-2019-01"
    # park_my_car = ParkingALot(order=True, parking_id_to_click)

    # debug
    park_my_car = ParkingALot(order=False)
    park_my_car.main()
