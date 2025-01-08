#!/bin/bash

echo "Запуск программы JarTool..."

if [ ! -d "venv" ]; then
    echo "Создаю виртуальное окружение..."
    python3 -m venv venv
fi

source venv/bin/activate

if [ -f "requirements.txt" ]; then
    echo "Устанавливаю зависимости..."
    pip install -r requirements.txt
fi

python3 main.py

deactivate