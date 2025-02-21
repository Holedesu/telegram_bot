# Telegram Bot with Django Integration

## Описание
Этот проект представляет собой Telegram-бота, который:
- Отвечает на команды `/start`, `/help` и `/info`.
- Возвращает случайное сообщение из базы данных через команду `/info`.
- Позволяет добавлять сообщения и отслеживать пользователей через Django-админку.

Проект написан на Python с использованием библиотек:
- **Django** — для работы с базой данных и админкой.
- **python-telegram-bot** — для взаимодействия с Telegram API.

---

## Требования

Перед началом работы убедитесь, что у вас установлены:
- **Python** 3.8 или выше
- **PostgreSQL**
- **pip** (менеджер пакетов Python)

---

## Установка

1. **Клонируйте репозиторий:**

2. Создайте виртуальное окружение и активируйте его:
```commandline
python3 -m venv .venv
source .venv/bin/activate
```

3. Установите зависимости:
```commandline
pip install -r requirements.txt
```

4. Настройте PostgreSQL(Если вы используете SQLite, пропустите этот шаг):

   4.1 Закомментируйте данные строчки:
   ```commandline
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.sqlite3',
           'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
       }
   }
   ```

   4.2 Создайте базу данных и пользователя в PostgreSQL.

   4.3 Раскоментируйте Настройте соединение в файле settings.py в разделе DATABASES:

   ```commandline
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.postgresql',
           'NAME': 'database_name',
           'USER': 'database_user',
           'PASSWORD': 'password',
           'HOST': 'localhost',
           'PORT': '5432',
       }
   }
   ```
5. Выполните миграции:
```commandline
python manage.py makemigrations
python manage.py migrate
```
6. Создайте суперпользователя для доступа в админку и запустите Django:
```commandline
python manage.py createsuperuser
python manage.py runserver
```
7. Настройте Telegram-бота:
Зайдите в телеграм и в поиске найдите @BotFather.
Создайте бота и получите токен
Укажите его в 'main.py'
```commandline
application = (
        ApplicationBuilder()
        .token("INSERT_YOUR_TOKEN_INSTEAD_OF_THIS_TEXT")
        .build()
    )
```
8. Запустите бота:
```commandline
python main.py
```

## Мои данные для теста:

### Telegram token
```commandline
7764254536:AAHP_CN3cyh7utv7oY4W1DPWpkMNOSOIwcQ
```

### Добавить данные моей бд и админки
python manage.py loaddata data.json

### Данные от админки

1. Login : admin
2. Password: qwerty123

### ID моего бота
```commandline
@MyFeatureTestingBot
```

