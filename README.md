# Django-stripe

stripe + django
## Описание
Приложние для оплаты товаров и оплаты списка товаров Есть возможность создавать и просматривать следующие модели:

- Товары
- Списки товаров (возможно добавить скидку и налог)
- Скидки
- Налоги
При создании товаров, скидок и налогов создаются соответствующие модели в Stipe.

## Запуск приложения
1. Откройте консоль

2. Перейдите в папку, в которой будет храниться проект
cd <путь до папки>

3. Создайте папку для проекта и перейдите в нее

mkdir django_stripe cd django_stripe

4. Склонируйте проект

git clone https://github.com/SimonaSoloduha/django_stripe.git

5. Перейдите в папку проекта


cd django_stripe

6. Создайте виртуальное окружение venv


python -m venv venv

7. Активируйте виртуальное окружение venv


source venv/bin/activate

8. Установите необходимые пакеты:

pip install -r requirements.txt (Все используемые библиотеки представлены в файле requirements.txt)

9. При необходимости обновите pip и отдельно установить следующие пакеы:


python3-m pip install django 


pip install django-environ 

pip install stripe

10. Создайте в проекте файл .env

cd page

touch .env

11. Добавтьте в него следующие данные, где STRIPE_API_KEY - ваш Secret key доступный по следующей ссылке после регистрации в stripe
https://dashboard.stripe.com/test/apikeys


SECRET_KEY=re7ucstw$wpu8x-6cdh2-$2gs1@svb)i_n@ci&j-=o=tp%gxq STRIPE_API_KEY=sk_test...LjV

12. Создате админа

cd .. python manage.py migrate

python manage.py createsuperuser

13. Запустите миграции

python manage.py makemigrations 

python manage.py migrate

14. Запустите проект через консоль

python manage.py runserver

15. Перейдите на сайт:
http://127.0.0.1:8000 или в админ панель: http://127.0.0.1:8000/admin

16. API 

- Для получения session.id выбранного товара: 


bay/id_товара/?currency=rub/discount_id=3_11302022102200

- Для получения session.id выбранного заказа: 

bay_order/id_заказа/?currency=rub/discount_id=3_11302022102200

По умолчанию применяется валюта usd, цена в usd, скидка отсутствует 
При выборе currency=rub применяется цена товара в рублях 



Для завершения работы ввеите в консоли "Contril + C"
