import sqlite3
import os

# Создаем подключение к базе данных и создаем файл school.db
conn = sqlite3.connect('school.db')
cursor = conn.cursor()

print("База данных school.db создана!")

# Закрываем соединение
conn.close()