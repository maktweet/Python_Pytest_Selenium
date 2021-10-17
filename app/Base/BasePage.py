from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import *


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def do_send_keys(self, by_locator, msg):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
        element = wait.until(EC.visibility_of_element_located(by_locator))
        return element.send_keys(msg)

    def do_click(self, by_locator):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
        element = wait.until(EC.presence_of_element_located(by_locator))
        element.click()

    def do_visibility_check(self, by_locator):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
        element = wait.until(EC.presence_of_element_located(by_locator))
        return element.is_displayed()

    def do_get_text(self, by_locator):
        wait = WebDriverWait(self.driver, timeout=30, poll_frequency=3,
                             ignored_exceptions=[NoSuchElementException, ElementNotVisibleException])
        element = wait.until(EC.presence_of_element_located(by_locator))
        return element.text()
