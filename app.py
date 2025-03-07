from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)
app.config['DATABASE'] = "reviews.db"  # Указываем базу данных

import os
print(f"Используется база данных: {os.path.abspath(app.config['DATABASE'])}")


# Функция для инициализации базы данных
def init_db():
    with sqlite3.connect(app.config['DATABASE']) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS reviews (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT,
                specialist TEXT,
                city TEXT,
                rating INTEGER,
                review TEXT
            )
        ''')
        conn.commit()

# Главная страница
@app.route('/')
def index():
    return render_template('index.html')

# Обработчик формы для добавления отзыва
@app.route('/submit_review', methods=['POST'])
def submit_review():
    name = request.form.get('name')
    specialist = request.form.get('specialist')
    city = request.form.get('city')
    rating = request.form.get('rating')
    review = request.form.get('review')

    print(f"Полученные данные: {name}, {specialist}, {city}, {rating}, {review}")  # Отладка

    if name and review:  # Проверка обязательных полей
        try:
            with sqlite3.connect(app.config['DATABASE']) as conn:
                cursor = conn.cursor()
                cursor.execute("INSERT INTO reviews (name, specialist, city, rating, review) VALUES (?, ?, ?, ?, ?)",
                               (name, specialist, city, rating, review))
                conn.commit()
                print("Отзыв успешно добавлен!")  # Отладка
        except Exception as e:
            with open("error_log.txt", "a", encoding="utf-8") as log:
                log.write(f"Ошибка при сохранении отзыва: {e}\n")
            print(f"Ошибка при сохранении отзыва: {e}")  # Вывод ошибки в консоль

    return redirect(url_for('index'))

if __name__ == '__main__':
    init_db()  # Запускаем инициализацию базы при старте
    app.run(debug=True)
