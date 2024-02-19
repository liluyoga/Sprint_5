from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from data import UserData


class TestCrossing:
    def test_crossing_to_personal_account_after_authorization(self, driver):
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
            expected_conditions.visibility_of_element_located(TestLocators.PROFILE_IN_PERSONAL_ACCOUNT))

        url = driver.current_url

        assert '/account/profile' in url

    def test_crossing_to_constructor_from_personal_account_by_click_constructor(self, driver):
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
            expected_conditions.visibility_of_element_located(TestLocators.PROFILE_IN_PERSONAL_ACCOUNT))

        driver.find_element(*TestLocators.LINK_CONSTRUCTOR).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUILD_A_BURGER))

        element = driver.find_element(*TestLocators.BUILD_A_BURGER).text
        url = driver.current_url

        assert element == 'Соберите бургер' and url == 'https://stellarburgers.nomoreparties.site/'

    def test_crossing_to_constructor_from_personal_account_by_click_logo(self, driver):
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
            expected_conditions.visibility_of_element_located(TestLocators.PROFILE_IN_PERSONAL_ACCOUNT))

        driver.find_element(*TestLocators.LINK_LOGO).click()

        WebDriverWait(driver, 3).until(
            expected_conditions.visibility_of_element_located(TestLocators.BUILD_A_BURGER))

        element = driver.find_element(*TestLocators.BUILD_A_BURGER).text
        url = driver.current_url

        assert element == 'Соберите бургер' and url == 'https://stellarburgers.nomoreparties.site/'

