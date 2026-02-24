from flask import Flask, render_template, send_from_directory
import os

# Настраиваем Flask так, чтобы он искал шаблоны и статику в корневой папке проекта
app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    # Ищет index.html прямо в корне
    return render_template('index.html')

@app.route('/about')
def about():
    # Ищет about.html прямо в корне
    return render_template('about.html')

# Дополнительный роут для статических файлов (картинки, стили), 
# так как на Vercel без папок они могут иногда капризничать
@app.route('/<path:path>')
def send_static(path):
    return send_from_directory('.', path)

# Это нужно для запуска локально или на некоторых хостингах
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)