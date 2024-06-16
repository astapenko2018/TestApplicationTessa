import allure
from allure_commons.types import AttachmentType
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.remote.webdriver import WebElement


TIMEOUT = 25
URL = "https://localhost:7141/"


class BasePage:

    def __init__(self, browser):
        self.browser = browser
        self.base_url = URL

    def open_page(self):
        return self.browser.get(self.base_url)

    def get_element_text(self, how, what, timeout=TIMEOUT):
        return self.find_element(how, what, timeout).text

    def find_element(self, how, what, timeout=TIMEOUT) -> WebElement:
        return WebDriverWait(self.browser, timeout).until(EC.visibility_of_element_located((how, what)),
                                                          message=f"Can't find element by locator {how, what}")

    def screenshot_page(self):
        allure.attach(self.browser.get_screenshot_as_png(), name="Скриншот",
                      attachment_type=AttachmentType.PNG)
