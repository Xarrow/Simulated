# -*-coding:utf-8 -*-

from flask import render_template
from flask import Flask

app = Flask(__name__)


@app.route("/fuck/<name>")
def fuck(name):
    return "fuck %s" % name


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == '__main__':
    app.run()
