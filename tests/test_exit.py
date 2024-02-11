from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from data import UserData


class TestExitFromPersonalAccount:

    def test_exit_from_personal_account_by_click_exit_button(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOG_ON))

        driver.find_element(*TestLocators.INPUT_LOGIN).send_keys(UserData.user.get('email'))
        driver.find_element(*TestLocators.INPUT_LOGIN_PASSWORD).send_keys(UserData.user.get('password'))
        driver.find_element(*TestLocators.BUTTON_LOG_ON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_PLACE_ORDER))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_EXIT))

        driver.find_element(*TestLocators.BUTTON_EXIT).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOG_ON))

        url = driver.current_url

        assert '/login' in url
