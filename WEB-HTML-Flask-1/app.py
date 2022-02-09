from flask import Flask, url_for, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return "Миссия Колонизация Марса"


@app.route("/image_mars")
def image():
    return render_template("index.html")


@app.route('/index')
def index1():
    return "И на Марсе будут яблони цвести!"


@app.route('/promotion')
def promotion():
    return render_template("promotion.html")


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
