from page.base_page import BasePage
from loguru import logger
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import UnexpectedAlertPresentException, NoAlertPresentException


class Alerts(BasePage):
    def result_alert(self):
        WebDriverWait(self.browser, 25).until(EC.alert_is_present())
        alert = self.browser.switch_to.alert
        alert_text = alert.text
        logger.debug(alert_text)
        alert.accept()
        return alert_text

        # try:
        #     alert.accept()
        # except NoAlertPresentException:
        #     pass

    def accept_alert(self):
        confirm_alert = self.browser.switch_to.alert
        confirm_alert.accept()



