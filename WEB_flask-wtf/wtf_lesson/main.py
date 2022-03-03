import imp
import re
from flask import Flask, render_template, redirect
from loginform import LoginForm


app = Flask(__name__)
app.config['SECRET_KEY'] = 'yandexlyceum_secret_key'
title = "sad"


@app.route('/')
@app.route('/index')
def index():
    return render_template("profile.html", title=title)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect('/success')
    return render_template('login.html', title='Авторизация', form=form)


@app.route("/success")
def success():
    return "Ok"


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
