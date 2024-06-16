from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest
import allure
from page.page_app_tessa import ApplicationTessa as AppTessa
from page.alerts import Alerts
from loguru import logger


@allure.title("Авто-тест 'СЭД Tessa'")
@allure.description(""" 
ТЕСТ ПЛАН:
    - Добавление нового документа 
    - Установление активной задачи документа как выполненной
    - Отмена активной задачи документа
    - Удаление документа
""")
@allure.severity('CRITICAL')
def test_tessa(browser):
    page_tessa = AppTessa(browser)
    page_tessa.open_page()
    answer_alert = Alerts(browser)

    with allure.step("Добавление нового документа"):
        page_tessa.create_doc("test1")
        assert answer_alert.result_alert() == "Документ успешно добавлен", logger.error("Документ не добавлен")
        with allure.step("Документ успешно добавлен"):
            page_tessa.screenshot_page()

    logger.info("Установление активной задачи документа как выполненной")
    with allure.step("Установление активной задачи документа как выполненной"):
        page_tessa.complete_the_task()
        assert answer_alert.result_alert() == "Задача выполнена"
        with allure.step("Задача выполнена"):
            page_tessa.screenshot_page()

    logger.info("Отмена активной задачи документа")
    with allure.step("Отмена активной задачи документа"):
        page_tessa.create_doc("test2")
        answer_alert.result_alert()
        page_tessa.cancel_task()
        assert answer_alert.result_alert() == "Задача отменена", logger.error(f'Задача не отменена')
        with allure.step("Задача отменена"):
            page_tessa.screenshot_page()

    logger.info("Удалить задачу")
    with allure.step("Удалить задачу"):
        page_tessa.delete_task()
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        confirm = browser.switch_to.alert
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        confirm.accept()
        WebDriverWait(browser, 3).until(EC.alert_is_present())
        with allure.step("Документ успешно удален"):
            assert confirm.text == "Документ успешно удален", logger.error('документ не удален')
            confirm.accept()
            logger.debug("Документ успешно удален")


