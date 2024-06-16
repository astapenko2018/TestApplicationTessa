import pytest
import allure
from allure_commons.types import AttachmentType
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager


@pytest.fixture(scope="function")
def browser():
    browser = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    print("\nstart chrome browser for tests..")
    yield browser
    allure.attach(browser.get_screenshot_as_png(), name="Скриншот при закрытии браузера",
                  attachment_type=AttachmentType.PNG)
    print("\nquit browser..")
    browser.quit()
