# Sprint_5
Проект содержит  
5 файлов в тестами  
conftest.py - файл с фикстурой  
data.py - файл с данными для регистрации и авторизации  
locators.py - файл с локаторами  

Файлы с тестами  

### test_registration.py
содержит тесты регистрации нового пользователя  
для регистрации каждый раз используются новые email и пароль
#### test_registration_success
тест успешной регистрации  
#### test_registration_with_incorrect_password
тест получения ошибки при вводе пароля менее 6 символов  

### test_login.py
содержит тесты входа в аккаунт из разных разделов  
для входа используется зарегистрированный пользователь  
#### test_login_by_button_on_main_page
тест входа после клика по кнопке Войти в аккаунт на главной странице  
#### test_login_by_button_in_personal_account  
тест входа после клика по кнопке Личный Кабинет  
#### test_login_by_button_on_registration_form  
тест входа после кликов на Личный кабинет > Зарегистрироваться > Войти  
#### test_login_by_button_on_password_recovery_page 
тест входа после кликов на Личный кабинет > Восстановить пароль > Войти

### test_exit.py
содержит тест выхода из аккаунта  
для входа используется зарегистрированный пользователь  
#### test_exit_from_personal_account_by_click_exit_button
тест выхода из аккаунта после авторизации и перехода в Личный кабинет

### test_crossing.py
содержит тесты переходов в разделы  
для входа используется зарегистрированный пользователь
#### test_crossing_to_personal_account_after_authorization
тест перехода в личный кабинет после авторизации
#### test_crossing_to_constructor_from_personal_account_by_click_constructor
тест перехода в Конструктор из личного кабинета по клику на "Конструктор"
#### test_crossing_to_constructor_from_personal_account_by_click_logo
тест перехода в Конструктор из личного кабинета по клику на логотип  

### test_construction_section.py
содержит тесты перехода к разделам конструктора с ингредиентами  
#### test_crossing_to_sauces
тест перехода в раздел Соусы  
#### test_crossing_to_stuffing
тест перехода в раздел Начинки  
#### test_crossing_to_buns
тест перехода в раздел Булки  
для перехода в раздел Булки предварительно выполняется переход в раздел Соусы  

