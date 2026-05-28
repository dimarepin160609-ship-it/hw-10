from flask import Flask, render_template

app = Flask(__name__)

# --- Завдання 1: Маршрути без шаблонів ---

@app.route('/')
def home():
    return "<h1>Вітаємо на головній сторінці!</h1><a href='/about/'>Про нас</a> | <a href='/services/'>Послуги</a> | <a href='/contact/'>Контакти</a> | <a href='/portfolio/'>Портфоліо</a>"

@app.route('/about/')
def about():
    return "<h1>Про нас</h1><p>Ми команда професіоналів, що створює круті веб-сайти.</p><a href='/'>На головну</a>"

@app.route('/services/')
def services():
    return "<h1>Наші послуги</h1><ul><li>Розробка сайтів</li><li>Дизайн інтерфейсів</li><li>SEO-оптимізація</li></ul><a href='/'>На головну</a>"

@app.route('/contact/')
def contact():
    return "<h1>Контакти</h1><p>Пишіть нам на email: support@example.com</p><a href='/'>На головну</a>"

# --- Завдання 2: Маршрут для Портфоліо (використовує шаблон) ---

@app.route('/portfolio/')
def portfolio():
    # Файл portfolio.html має лежати в папці /templates
    return render_template('portfolio.html')

if __name__ == '__main__':
    app.run(debug=True)