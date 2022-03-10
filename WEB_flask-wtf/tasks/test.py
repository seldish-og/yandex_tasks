from flask import Flask, render_template

app = Flask(__name__)
title = "sad"


@app.route('/')
@app.route('/index')
def index():
    return render_template("profile.html", title=title)


@app.route('/training/<prof>')
def training(prof):
    return render_template("trains.html", title=title, prof=prof)


@app.route('/list_prof/<type>')
def list_prof(type):
    list_prof = [x for x in "sadasd"]
    return render_template("list_prof.html", title=title, type=type, list_prof=list_prof)


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
