from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, template_folder='.', static_folder='.')

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/<path:path>')
def static_proxy(path):
    # Исправленный return
    return send_from_directory('.', path)

# Это нужно для локального запуска
if __name__ == "__main__":
    app.run(debug=True)
