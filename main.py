from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


if __name__ == '__main__':

    option = webdriver.ChromeOptions()
    option.add_argument('— incognito')

    browser = webdriver.Chrome(executable_path='src/webdriver/chromedriver.exe',
                               chrome_options=option)

    browser.get("https://go.parkanizer.com/#/offers")