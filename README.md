<h1 align="center">📧 EmailSender</h1>
<p align="center">
  Универсальный инструмент для отправки email-сообщений с поддержкой шаблонов и переменных через SMTP.
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/MuratOfficial/emailsender?style=flat-square" />
  <img src="https://img.shields.io/github/license/MuratOfficial/emailsender?style=flat-square" />
  <img src="https://img.shields.io/github/stars/MuratOfficial/emailsender?style=flat-square" />
</p>

---

## 🚀 О проекте

**EmailSender** — это легковесный Python-сервис для отправки email-сообщений через SMTP. Поддерживает HTML-шаблоны, переменные, вложения и гибкую конфигурацию. Может быть легко интегрирован в другие Python-приложения или использоваться как самостоятельный скрипт.

---

## 🧰 Стек технологий

- **Язык**: Python 3  
- **SMTP-библиотека**: `smtplib`  
- **Шаблонизация**: `Jinja2`  
- **Конфигурация**: `dotenv`, `configparser`  
- **Прочее**: `email`, `ssl`, `os`

---

## ⚙️ Функциональность

- ✅ Отправка писем через SMTP  
- ✅ Поддержка HTML и текстовых сообщений  
- ✅ Поддержка шаблонов (Jinja2)  
- ✅ Подстановка переменных в шаблоны  
- ✅ Вложения (attachments)  
- ✅ Конфигурация через `.env` и `config.ini`  
- ⏳ Планируется интеграция через API

---

## 📦 Установка и запуск

```bash
# 1. Клонируйте репозиторий
git clone https://github.com/MuratOfficial/emailsender.git
cd emailsender

# 2. Установите зависимости
pip install -r requirements.txt

# 3. Создайте .env файл (если необходимо)
cp .env.example .env

# 4. Отредактируйте конфигурацию в config.ini

# 5. Запустите отправку письма
python main.py

```

## 🛠️ Конфигурация окружения

Файл `.env`:

```env
EMAIL_USER=example@gmail.com
EMAIL_PASSWORD=your_app_password
```

Файл `.config.ini`:

```inv
[EMAIL]
subject = Пример письма
recipient = recipient@example.com
template = templates/email_template.html

[SMTP]
host = smtp.gmail.com
port = 465
use_tls = false
use_ssl = true
```

## 🧪 Пример шаблона (Jinja2)

```html
<h1>Привет, {{ username }}!</h1>
<p>Спасибо за использование нашего сервиса.</p>
```

## 📌 Планы на будущее

* Отправка через API
* Поддержка очередей (Celery / Redis)
* Веб-интерфейс (на Flask или FastAPI)
* Поддержка групповой рассылки

## 🤝 Вклад
Хочешь внести свой вклад? Добро пожаловать!

```bash
# Форкни репозиторий
# Создай новую ветку
git checkout -b feature/my-feature

# Внеси изменения и сделай коммит
git commit -m "Добавил новую фичу"

# Отправь изменения
git push origin feature/my-feature

# Создай Pull Request!
```

## 📄 Лицензия
Проект распространяется под лицензией MIT. Подробнее в LICENSE.

<p align="center"> <b>Сделано с ❤️ by <a href="https://github.com/MuratOfficial">MuratOfficial</a></b> </p>
