from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators
from data import UserData


class TestRegistration:
    def test_registration_success(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LINK_REGISTER))

        driver.find_element(*TestLocators.LINK_REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))

        driver.find_element(*TestLocators.INPUT_NAME).send_keys(UserData.new_user.get('name'))
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(UserData.new_user.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(UserData.new_user.get('password'))
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_LOG_ON))

        url = driver.current_url

        driver.quit()

        assert '/login' in url

    def test_registration_with_incorrect_password(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.PERSONAL_ACCOUNT))

        driver.find_element(*TestLocators.PERSONAL_ACCOUNT).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.LINK_REGISTER))

        driver.find_element(*TestLocators.LINK_REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.BUTTON_REGISTER))

        driver.find_element(*TestLocators.INPUT_NAME).send_keys(UserData.new_user_short_password.get('name'))
        driver.find_element(*TestLocators.INPUT_EMAIL).send_keys(UserData.new_user_short_password.get('email'))
        driver.find_element(*TestLocators.INPUT_PASSWORD).send_keys(UserData.new_user_short_password.get('password'))
        driver.find_element(*TestLocators.BUTTON_REGISTER).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.ERROR_INCORRECT_PASSWORD))

        element = driver.find_element(*TestLocators.ERROR_INCORRECT_PASSWORD).text
        url = driver.current_url

        driver.quit()

        assert element == 'Некорректный пароль' and '/register' in url






