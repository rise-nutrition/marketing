import os

from flask import Flask, render_template, request, send_from_directory

BASE_DIR = os.path.dirname(os.path.realpath(__file__))

app = Flask(__name__, static_folder=os.path.join(BASE_DIR, 'assets'))


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/demo')
def demo():
    return render_template('demo.html')

@app.route('/robots.txt')
@app.route('/sitemap.xml')
def static_from_root():
    return send_from_directory(app.static_folder, request.path[1:])