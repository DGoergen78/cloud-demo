from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "There is no cloud, just other peoples computers"

@app.route("/about")
def about():
    return "Simple Python app running on a PaaS platform"

@app.route("/cloud")
def cloud():
    return "Serverless does not mean no servers"
