# Twitch Clip Creator & Title Editor
_Automatic Twitch clip creation and title editing using the Helix API and Selenium._

English | [Русский ниже](#русский)

---

## 🇬🇧 English

### 📌 Description
This script allows you to automatically **create a clip on Twitch** using the official Helix API and then **change the clip title through Selenium automation**.  
Useful for automation tools, clip bots, or stream‑management scripts.

Supports both:
- **Selenium Grid**
- **Local Selenium WebDriver (Chrome)**

---

## ✨ Features
- Create a new clip using Twitch Helix API  
- Retrieve the edit URL for the new clip  
- Authenticate on Twitch through cookies  
- Automatically update the clip title via Selenium  
- Local Chrome WebDriver alternative to Selenium Grid  

---

## 🔧 Requirements

- Python 3.8+
- Twitch:
  - OAuth token  
  - Bearer token  
  - Client ID
- Selenium WebDriver or Selenium Grid
- Chrome + ChromeDriver (if running locally)

---



Create a `config.py` file:

```python
oauth = "<your Twitch OAuth token>"
scope_token = "<your Twitch bearer token>"
client_id = "<your Twitch client ID>"
```

---

## ⚙️ Configuration

In your script:

```python
BROADCASTER_ID = ""      # Twitch channel ID where the clip will be created
NEW_TITLE = ""           # New clip title
SELENIUM_GRID_URL = ""   # Selenium Grid URL (leave empty to use local Selenium)
```

---

## 🖥 Using Local Selenium Instead of Selenium Grid

Replace:

```python
driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, options=options)
```

with:

```python
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
```

And leave:

```python
SELENIUM_GRID_URL = ""
```

---

## ▶️ Run

```bash
python main.py
```

---

## ⚠️ Notes

- Twitch tokens must be valid  
- Cookies must belong to the logged‑in Twitch account  
- `stealth.min.js` helps bypass Twitch automation detection  
- Chrome and ChromeDriver versions must match for local use  

---

---

# 🇷🇺 Русский

### 📌 Описание
Скрипт автоматически **создаёт клип на Twitch** через Helix API и затем **меняет название клипа с помощью Selenium**.  
Подходит для автоматизации, ботов, инструментов стримеров и различных интеграций.

Поддерживает:
- **Selenium Grid**
- **Локальный Selenium WebDriver (Chrome)**

---

## ✨ Возможности
- Создание клипа через Twitch API  
- Получение ссылки `edit_url`  
- Авторизация с помощью cookies  
- Автоматическая смена названия клипа через Selenium  
- Возможность использовать локальный Selenium вместо Grid  

---

## 🔧 Требования

- Python 3.8+
- Twitch:
  - OAuth токен  
  - Bearer токен  
  - Client ID
- WebDriver или Selenium Grid
- Chrome + ChromeDriver (если запуск локально)

---



Создайте файл `config.py`:

```python
oauth = "<ваш Twitch OAuth токен>"
scope_token = "<ваш Twitch bearer токен>"
client_id = "<ваш Twitch client ID>"
```

---

## ⚙️ Настройка

В начале файла:

```python
BROADCASTER_ID = ""      # ID канала, на котором создаётся клип
NEW_TITLE = ""           # Новое название клипа
SELENIUM_GRID_URL = ""   # URL Selenium Grid (оставьте пустым для локального Selenium)
```

---

## 🖥 Использование локального Selenium вместо Selenium Grid

Замените:

```python
driver = webdriver.Remote(command_executor=SELENIUM_GRID_URL, options=options)
```

на:

```python
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
```

И оставьте:

```python
SELENIUM_GRID_URL = ""
```

---

## ▶️ Запуск

```bash
python main.py
```

---

## ⚠️ Важно

- Токены Twitch должны быть действительными  
- Cookies должны принадлежать авторизованному аккаунту Twitch  
- Рекомендуется использовать `stealth.min.js`  
- Версии Chrome и ChromeDriver должны совпадать при локальном запуске  

---

## 📄 License
MIT
