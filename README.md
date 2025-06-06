# Проект "Платформа для обмена вещами"
Для данного проекта был реализован бэкенд приложения, разработанный на языке Python с использованием фреймворка Django.  
Для расширения функционала приложения использовалась библиотека Django REST Framework.  
Веб-интерфейс был реализован через Django Templates.  



## Развертывание проекта

1. Клонирование репозитория в локальную папку:

    ```bash
    git clone https://github.com/TimurKhamidullin28/ExchangingPlatform.git
    ```

2. Установка зависимостей в виртуальное окружение

   ```bash
   pip install -r requirements.txt
   ```

3. Создайте базу данных проекта. Для этого перейдите в папку `myproject/` и выполните команду:

   ```bash
   python manage.py migrate
   ```

4. Запустите приложение командой 

    ```bash
   python manage.py runserver
   ```
   
5. Для запуска тестов примените команду 

    ```bash
   python manage.py test ads.tests
   ```
   
## Использование приложения
- В веб-браузере перейдите по ссылке http://localhost:8000/ads/api/ чтобы открыть стартовую страницу API приложения.
- Чтобы посмотреть работу приложения через HTML-интерфейс перейдите по ссылке http://localhost:8000/ads/list/ 
