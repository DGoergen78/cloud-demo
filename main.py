from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <html>
      <body style="
        height:100vh;
        margin:0;
        display:flex;
        align-items:center;
        justify-content:center;
        font-family:Arial, sans-serif;
        font-size:3rem;
        color:#2563eb;
        text-align:center;
      ">
        There is no cloud, just other peoples computers
      </body>
    </html>
    """

@app.route("/about")
def about():
    return "Simple Python app running on a PaaS platform"

@app.route("/cloud")
def cloud():
    return "Serverless does not mean no servers"
