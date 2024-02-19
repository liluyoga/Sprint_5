from selenium import webdriver
import pytest


@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()
    driver.get('https://stellarburgers.nomoreparties.site/')
    yield driver
    driver.quit()
