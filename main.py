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
      ">
        <div style="text-align:center">
          <button id="btn" onclick="showText()"
            style="font-size:1.2rem;padding:10px 20px;">
            Show message
          </button>

          <div id="msg" style="
            display:none;
            margin-top:20px;
            font-size:3rem;
            color:#2563eb;">
            There is no cloud, just other peoples computers.
          </div>
        </div>

        <script>
          function showText() {
            document.getElementById("msg").style.display = "block";
            document.getElementById("btn").style.display = "none";
          }
        </script>
      </body>
    </html>
    """


@app.route("/about")
def about():
    return "Simple Python app running on a PaaS platform"

@app.route("/cloud")
def cloud():
    return "Serverless does not mean no servers"


