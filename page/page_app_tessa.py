import time

from selenium.webdriver.common.by import By
from page.base_page import BasePage


class ApplicationTessa(BasePage):
    BTN_ADD_DOC = (By.CSS_SELECTOR, ".add-task-button")
    BTN_ADD = (By.CSS_SELECTOR, ".document-window-add-button")
    INPUT_TEXT = (By.CSS_SELECTOR, "input")
    CREATE_DOC = (By.CSS_SELECTOR, ".create-document-button > .button-style")
    BTN_PERFOM = (By.XPATH, "//button[contains(.,'Выполнить')]")
    BTN_CANCEL = (By.XPATH, "//button[contains(.,'Отменить')]")
    BTN_DELETE = (By.XPATH, "//button[contains(.,'Удалить документ')]")

    # Добавить документ
    def create_doc(self, name_task):
        self.find_element(*ApplicationTessa.BTN_ADD_DOC).click()
        self.find_element(*ApplicationTessa.BTN_ADD).click()
        self.find_element(*ApplicationTessa.INPUT_TEXT).send_keys(name_task)
        self.find_element(*ApplicationTessa.CREATE_DOC).click()

    # Выполнить задачу
    def complete_the_task(self):
        self.find_element(*ApplicationTessa.BTN_PERFOM).click()

    # Отменить задачу
    def cancel_task(self):
        self.find_element(*ApplicationTessa.BTN_CANCEL).click()

    # Удалить задачу
    def delete_task(self):
        self.find_element(*ApplicationTessa.BTN_DELETE).click()
