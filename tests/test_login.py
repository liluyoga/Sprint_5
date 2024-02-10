from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from data import UserData


class TestLogin:

    def test_login_by_button_on_main_page(self, driver):
        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOGIN_ACCOUNT))

        driver.find_element(*TestLocators.BUTTON_LOGIN_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOG_ON))

        driver.find_element(*TestLocators.INPUT_LOGIN).send_keys(UserData.user.get('email'))
        driver.find_element(*TestLocators.INPUT_LOGIN_PASSWORD).send_keys(UserData.user.get('password'))
        driver.find_element(*TestLocators.BUTTON_LOG_ON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_PLACE_ORDER))

        url = driver.current_url

        driver.quit()

        assert url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_by_button_in_personal_account(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOG_ON))

        driver.find_element(*TestLocators.INPUT_LOGIN).send_keys(UserData.user.get('email'))
        driver.find_element(*TestLocators.INPUT_LOGIN_PASSWORD).send_keys(UserData.user.get('password'))
        driver.find_element(*TestLocators.BUTTON_LOG_ON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_PLACE_ORDER))

        url = driver.current_url

        driver.quit()

        assert url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_by_button_on_registration_form(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LINK_REGISTER))

        driver.find_element(*TestLocators.LINK_REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LINK_LOGIN))

        driver.find_element(*TestLocators.LINK_LOGIN).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOG_ON))

        driver.find_element(*TestLocators.INPUT_LOGIN).send_keys(UserData.user.get('email'))
        driver.find_element(*TestLocators.INPUT_LOGIN_PASSWORD).send_keys(UserData.user.get('password'))
        driver.find_element(*TestLocators.BUTTON_LOG_ON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_PLACE_ORDER))

        url = driver.current_url

        driver.quit()

        assert url == 'https://stellarburgers.nomoreparties.site/'

    def test_login_by_button_on_password_recovery_page(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.LINK_RECOVERY_PASSWORD))

        driver.find_element(*TestLocators.LINK_RECOVERY_PASSWORD).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LINK_LOGIN))

        driver.find_element(*TestLocators.LINK_LOGIN).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOG_ON))

        driver.find_element(*TestLocators.INPUT_LOGIN).send_keys(UserData.user.get('email'))
        driver.find_element(*TestLocators.INPUT_LOGIN_PASSWORD).send_keys(UserData.user.get('password'))
        driver.find_element(*TestLocators.BUTTON_LOG_ON).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUTTON_PLACE_ORDER))

        url = driver.current_url

        driver.quit()

        assert url == 'https://stellarburgers.nomoreparties.site/'
