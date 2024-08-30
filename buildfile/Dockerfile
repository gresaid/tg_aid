# Установка базового образа с Python
FROM python:3.10-slim as python-base

# Установка переменных окружения
ENV PIP_CACHE_DIR=/opt/.cache

# Создание слоя для установки зависимостей
FROM python-base as dependencies

# Обновление pip и установка зависимостей из requirements.txt
RUN python3 -m venv /opt/venv \
    && /opt/venv/bin/pip install --upgrade pip setuptools \
    && /opt/venv/bin/pip install --no-cache-dir -r requirements.txt

# Создание финального слоя приложения
FROM python-base as app

# Копирование установленного виртуального окружения
COPY --from=dependencies /opt/venv /opt/venv

# Установка переменной PATH для использования виртуального окружения
ENV PATH="/opt/venv/bin:$PATH"

# Установка рабочей директории
WORKDIR /app

# Копирование всех файлов в рабочую директорию
COPY . .

# Запуск приложения
CMD ["python", "main.py"]
