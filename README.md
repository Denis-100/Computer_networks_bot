# 🌐 Computer Networks Bot

Небольшой **учебный проект** — Telegram-бот, который знакомит с основными видами компьютерных сетей.

Бот рассказывает о **LAN, WAN, MAN, PAN и VPN** и показывает иллюстрации к каждой теме. Навигация сделана с помощью кнопок.

**Технологии:** Python, aiogram 3.

## Как запустить

1. Склонируйте репозиторий:

   ```bash
   git clone https://github.com/Denis-100/Computer_networks_bot.git
   cd Computer_networks_bot
   ```

2. Установите библиотеку:

   ```bash
   python -m pip install aiogram
   ```

3. Создайте в корне файл `config.py`:

   ```python
   token = "ВАШ_ТОКЕН_БОТА"
   ```

   Токен можно получить у **@BotFather**. Файл `config.py` добавлен в `.gitignore` — не публикуйте его.

4. Запустите бота:

   ```bash
   python main.py
   ```

В Telegram отправьте боту команду **/menu**, чтобы открыть меню тем.
