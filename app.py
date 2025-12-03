from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

# Counter to track visits
counter = 0

cards = [
    {"question": "Hola", "answer": "Hello"},
    {"question": "Merci", "answer": "Thanks"},
    {"question": "Ciao", "answer": "Bye"}
]

@app.route("/")
def home():
    return render_template("home.html", cards=cards)

@app.route("/about")
def about():
    return "This is a simple mini project using Flask basics."

@app.route("/date")
def date():
    return "Current server time: " + str(datetime.now())

@app.route("/count_views")
def count_views():
    global counter
    counter += 1
    return f"This page was viewed {counter} times."

@app.route("/hello/<name>")
def name(name):
    return f"Hello {name}!"

if __name__ == "__main__":
    app.run(debug=True)
