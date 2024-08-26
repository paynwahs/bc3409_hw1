from flask import Flask, render_template

app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World! This is the first Flask app!'

@app.route("/",methods=["GET","POST"])
def index():
    return(render_template("index.html"))