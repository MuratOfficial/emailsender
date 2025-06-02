<h1 align="center">📧 EmailSender</h1>
<p align="center">
  Универсальный инструмент для отправки писем с кастомным содержимым и шаблонами через SMTP.
</p>

<p align="center">
  <img src="https://img.shields.io/github/languages/top/MuratOfficial/emailsender?style=flat-square" />
  <img src="https://img.shields.io/github/license/MuratOfficial/emailsender?style=flat-square" />
  <img src="https://img.shields.io/github/stars/MuratOfficial/emailsender?style=flat-square" />
</p>

---

## 🚀 О проекте

**EmailSender** — это простой и надежный сервис отправки email-сообщений с возможностью интеграции в любые Node.js-приложения. Поддерживает динамические шаблоны, переменные, HTML и текстовые письма.

---

## 🧰 Стек технологий

- **Язык**: TypeScript / JavaScript  
- **Сервер**: Node.js  
- **Транспорт**: Nodemailer  
- **Дополнительно**: dotenv, ejs / pug / handlebars (если используются шаблоны)

---

## ⚙️ Функциональность

- ✅ Отправка писем через SMTP  
- ✅ Поддержка HTML и текстовых сообщений  
- ✅ Использование шаблонов  
- ✅ Подстановка переменных в шаблоны  
- ✅ Конфигурация через `.env`  
- ⏳ Поддержка очередей (в будущем)

---

## 📦 Установка

```bash
# 1. Клонировать репозиторий
git clone https://github.com/MuratOfficial/emailsender.git

# 2. Установить зависимости
cd emailsender
npm install

# 3. Создать .env файл
cp .env.example .env

# 4. Запустить
npm start
```

## 🛠️ Конфигурация окружения

Пример `.env`:

```env
DATABASE_URL=mongodb://localhost:27017/calorie-tracker
NEXT_PUBLIC_API_URL=http://localhost:3000/api
JWT_SECRET=your_jwt_secret
```

## 📌 Планы на будущее

* Поддержка сканирования штрих-кодов
* Рекомендации по питанию на основе ИИ
* Синхронизация с фитнес-браслетами
* Поддержка оффлайн-режима
* Мобильное приложение (React Native)

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
