from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "HELLO WORLD"

#Test
@app.route("/test")
def home():
    return "TEST"