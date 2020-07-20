from flask import Flask
from flask import render_template
from flask import request
import models
import chat

# -- Initialization section --
app = Flask(__name__)


# -- Routes section --


@app.route('/')
@app.route('/index.html', methods=["GET","POST"])
def index():
    responseTing = ""
    newsStuff = models.newsPieces()
    if request.method == "POST":
      userMsg = request.form["msg"].lower()
      print(userMsg)
      responseTing = chat.chatResponse(userMsg)
    return render_template('index.html', props = newsStuff, resp = responseTing )

@app.route('/fix.html')
def fix():
    return render_template('fix.html')

@app.route('/problem.html')
def problem():
    return render_template('problem.html')
