# TestApplicationTessa
Для запуска теста необходмио установить библиотки, запустить команду из корневого каталога: pip install -r requirements.txt
Запуск теста(результат тестов можно увидеть в логах): pytest -s -v test/ 
Запуск с отчетом allure(требуется установка allure): pytest -s -v test/ --alluredir=result
Запуск отчета allure: allure serve result
