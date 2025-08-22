from waitress import serve

from flask import Flask, render_template

app = Flask(__name__)

@app.route("/task 1")
def task1():
    return render_template("index.html")

@app.route("/task 2")
def task2():
    return "task 2"

if __name__ == ("__main__"):
    serve(app, host='127.0.0.1', port=5000)