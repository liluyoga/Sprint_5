from selenium.webdriver.common.by import By


class TestLocators:

    PERSONAL_ACCOUNT = [By.XPATH, ".//a[@href='/account']"] # Личный кабинет

    LINK_REGISTER = [By.XPATH, ".//a[@href='/register']"] # Зарегистрироваться

    LINK_RECOVERY_PASSWORD = [By.XPATH, ".//a[@href='/forgot-password']"]  # Восстановить пароль

    LINK_LOGIN = [By.XPATH, ".//a[@href='/login']"]  # Ссылка на Вход со страницы регистрации и восстановления пароля

    LINK_CONSTRUCTOR = [By.XPATH,
                        ".//a[contains(@class, 'AppHeader_header__link')][@href='/']"]  # Ссылка на Конструктор

    LINK_LOGO = [By.XPATH, ".//div[contains(@class, 'AppHeader_header__logo')]/a"]  # Ссылка на конструктор из логотипа

    INPUT_NAME = [By.XPATH, ".//label[text()='Имя']/following-sibling::input"] # Регистрация поле Имя

    INPUT_EMAIL = [By.XPATH, ".//label[text()='Email']/following-sibling::input"] # Регистрация поле Email

    INPUT_PASSWORD = [By.XPATH, ".//input[@type='password']"] # Регистрация поле Пароль

    INPUT_LOGIN = [By.XPATH, ".//label[text()='Email']/following-sibling::input"]  # Вход поле Email

    INPUT_LOGIN_PASSWORD = [By.XPATH, ".//label[text()='Пароль']/following-sibling::input"]  # Вход поле Пароль

    BUTTON_REGISTER = [By.XPATH, ".//button[text()='Зарегистрироваться']"] # Кнопка Зарегистрироваться

    BUTTON_LOGIN_ACCOUNT = [By.XPATH, ".//button[contains(@class, 'button_button_size_large') and text()='Войти в аккаунт']"] # Кнопка Войти в аккаунт на главной

    BUTTON_LOG_ON = [By.XPATH,
                     ".//button[contains(@class, 'button_button_size_medium') and text()='Войти']"]  # Вход кнопка Войти

    BUTTON_EXIT = [By.XPATH,
                   ".//button[contains(@class, 'Account_button')][text()='Выход']"]  # Кнопка Выход из личного кабинета

    BUTTON_PLACE_ORDER = [By.XPATH,
                          ".//button[contains(@class, 'button_button_size_large') and text()='Оформить заказ']"]  # Кнопка Оформить заказ на главной

    BUILD_A_BURGER = [By.XPATH, ".//h1[text()='Соберите бургер']"]  # Надпись Соберите бургер

    ERROR_INCORRECT_PASSWORD = [By.XPATH, ".//p[contains(@class, 'input__error text') and text()='Некорректный пароль']"] # Надпись некорректный пароль при регистрации

    PROFILE_IN_PERSONAL_ACCOUNT = [By.XPATH, ".//a[@href='/account/profile' and text()='Профиль']"] # Профиль в Личном кабинете

    SECTION_BUNS = [By.XPATH, ".//span[text()='Булки']/parent::div"] # Раздел Булки

    SECTION_SAUCES = [By.XPATH, ".//span[text()='Соусы']/parent::div"] # Раздел Соусы

    SECTION_STUFFING = [By.XPATH, ".//span[text()='Начинки']/parent::div"] # Раздел Начинки

    CURRENT_SECTION = [By.XPATH, ".//div[contains(@class, 'current')]/span"] # Текущий раздел





