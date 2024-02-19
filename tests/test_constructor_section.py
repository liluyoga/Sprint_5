from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions
from locators import TestLocators


class TestConstructorSection:

    def test_crossing_to_sauces(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SECTION_SAUCES))

        driver.find_element(*TestLocators.SECTION_SAUCES).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.CURRENT_SECTION))

        element = driver.find_element(*TestLocators.CURRENT_SECTION).text

        assert element == 'Соусы'

    def test_crossing_to_stuffing(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SECTION_STUFFING))

        driver.find_element(*TestLocators.SECTION_STUFFING).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.CURRENT_SECTION))

        element = driver.find_element(*TestLocators.CURRENT_SECTION).text

        assert element == 'Начинки'

    def test_crossing_to_buns(self, driver):
        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SECTION_SAUCES))

        driver.find_element(*TestLocators.SECTION_SAUCES).click()

        WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located(TestLocators.SECTION_BUNS))

        driver.find_element(*TestLocators.SECTION_BUNS).click()

        WebDriverWait(driver, 3).until(expected_conditions.presence_of_element_located(TestLocators.CURRENT_SECTION))

        element = driver.find_element(*TestLocators.CURRENT_SECTION).text

        assert element == 'Булки'