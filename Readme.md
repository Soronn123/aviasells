# ✈️ SkyTravel – система бронирования авиабилетов  

![SkyTravel Preview](https://github.com/Soronn123/static/favicon.svg)  

**Современная платформа для поиска и бронирования авиабилетов**  
Разработана на Python 3.13.3 с использованием Django и Tailwind CSS  

---

## 🛠 Технологии  
- **Backend**: Python 3.13.3 + Django  
- **Frontend**: Tailwind CSS, HTML5  

---

## 🚀 Быстрый старт

### 1. Клонирование репозитория
```bash
git clone https://github.com/ваш-username/SkyJourney.git
cd SkyJourney
```

### 2. Создание и активация виртуального окружения
#### Windows
```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Установка зависимостей
```bash
pip install -r requirements.txt
```

### 4. Настройка окружения (.env)
Создайте файл `.env` в корне проекта и заполните его по примеру:
```ini
SECRET_KEY=ваш_секретный_ключ
DEBUG=True  # или False для продакшена
```
> 🔑 **Где взять `SECRET_KEY`?**  
> Можно сгенерировать [здесь](https://djecrety.ir/) или использовать команду:  
> ```bash
> python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
> ```

### 5. Применение миграций
```bash
python manage.py migrate
```

### 6. Запуск сервера
```bash
python manage.py runserver
```
Откройте в браузере: [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## ⚙️ Дополнительные команды

### Создание суперпользователя (админка)
```bash
python manage.py createsuperuser
```

### Загрузка тестовых данных
```bash
python manage.py loaddata фикстура.json
```

---

## 📁 Структура проекта
```
SkyJourney/
├── avisells/           # Основное приложение
├── ways/               # Данные рейсов
├── users/              # Данные пользователей
├── cities/             # Данные о городов и стран
├── airplanes/          # Данные а самолетов и аэропортов
├── carts/              # Данные рейсов клиентов
├── theme/              # Стили TailwindCss
├── manage.py
└── requirements.txt
```

---


Разработано с ❤️ для авиапутешествий!  
2026 | lieQueen
```