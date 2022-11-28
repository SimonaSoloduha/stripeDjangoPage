# Django-stripe

stripe + django
Описание
Приложние для оплаты товаров и оплаты списка товаров Есть возможность создавать и просматривать следующие модели:

Товары
Списки товаров (возможно добавить скидку и налог)
Скидки
Налоги
При создании товаров, скидок и налогов создаются соответствующие модели в Stipe.

Запуск приложения
Откройте консоль

Перейдите в папку, в которой будет храниться проект
cd <путь до папки>

Создайте папку для проекта и перейдите в нее
mkdir django_stripe cd django_stripe

Склонируйте проект
git clone https://github.com/SimonaSoloduha/django_stripe.git

Перейдите в папку проекта
cd django_stripe

Создайте виртуальное окружение venv
python3 -m venv venv

Активируйте виртуальное окружение venv
source venv/bin/activate

Установите необходимые пакеты:

pip install -r requirements.txt (Все используемые библиотеки представлены в файле requirements.txt)

При необходимости обновите pip и отдельно установить следующие пакеы:
python3 -m pip install django pip install django-environ pip install stripe

Создайте в проекте файл .env
cd page

touch .env

Добавтьте в него следующие данные, где STRIPE_API_KEY - ваш Secret key доступный по следующей ссылке после регистрации в stripe
https://dashboard.stripe.com/test/apikeys

SECRET_KEY=re7ucstw$wpu8x-6cdh2-$2gs1@svb)i_n@ci&j-=o=tp%gxq STRIPE_API_KEY=sk_test...LjV

Создате админа
cd .. python manage.py migrate
python manage.py createsuperuser

Запустите миграции
python manage.py makemigrations 

python manage.py migrate

Запустите проект через консоль
python manage.py runserver

Перейдите на сайт:
http://127.0.0.1:8000 или в админ панель: http://127.0.0.1:8000/admin

Для завершения работы ввеите в консоли "Contril + C"
