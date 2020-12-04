from flask import Flask
import json
from flask import render_template

app = Flask[__name__]
names = [
    "Kuba", "Michal", "Cezary", "Karol", "Tomek"
]

@app.route('/')
def hello_world():
    return 'Hello, world!'

@app.route('/api/sample')
def sample_api_hello():
    return json.dumps(names)

@app.route('/index')
def sample_html_page():
    return render_template("hello.html", names=names)

