

# Предективная аналитика больших данных

Вэб приложение для определения цены на квартиру в Москве используя модели машинного обучения

## Installation 

Клонирование репозитория, создание виртуального окружения, ативация и установка необходимых библиотек

```sh
git clone https://github.com/Nixelman/pabd24
cd pabd24
python -m venv venv

#source venv/bin/activate  # mac or linux
.\venv\Scripts\activate   # windows

pip install -r requirements.txt
```

## Использование

### 1. Сбор данных
<li><strong><a href="https://github.com/Nixelman/pabd24/blob/main/src/parse_cian.py">parse_cian.py</a></strong> Скрипт для парсинга квартир.</li> 

```sh
python src/parse_cian.py 
```  

### 2. Загрзка данных в S3 хранилище
<li><strong><a href="https://github.com/Nixelman/pabd24/blob/main/src/upload_to_s3.py">upload_to_s3.py</a></strong> Скрипт для загрзки данных в S3 хранилище.</li>  
Для доступа к хранилищу, скопировать файл `.env` в корень проекта

```sh
python src/upload_to_s3.py -i data/raw/file.csv
```
### 3.Скачевание данных на локальную машину
<li><strong><a href="https://github.com/Nixelman/pabd24/blob/main/src/download_from_s3.py">download_from_s3.py</a></strong> Скрипт для скачевания данных на локальную машину.</li> 

```sh
python src/download_from_s3.py
``` 
### 4. Препроцессинг данных 
<li><strong><a href="https://github.com/Nixelman/pabd24/blob/main/src/preprocess_data.py">preprocess_data.py</a></strong> Скрипт для препроцессинга.</li> 

### 5. Обучение модели
<li><strong><a href="https://github.com/Nixelman/pabd24/blob/main/src/train_model.py">train_model.py</a></strong> Скрипт для обучения модели.</li> 

### 6. Запуск Flask приложения

<li><strong><a href="https://github.com/Nixelman/pabd24/blob/main/src/predict_app.py">predict_app.py</a></strong> Скрипт для запуска приложения</li>

```sh
python src/predict_app.py
```

### 7. Использование сервиса через вэб интерфес

Для использования приложения через вэб интерфейс `web/index.html`.  

### 8. Приложение на продакшн сервере
Описание тестирования <strong><a href="https://github.com/Nixelman/pabd24/blob/main/docs/report_3.md">here.</a>

Адресс для сервиса прдесказаия цен

http://192.144.12.199:8000

Для запуска приложения через docker:

docker run nixelman/pabd24:best_model
