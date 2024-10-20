from flask import Flask, render_template, request
import textblob


app = Flask(__name__)

# @app.route('/')
# def hello_world():
#     return 'Hello, World! This is the first Flask app!'

@app.route("/",methods=["GET","POST"])
def sentiment_analysis():
    return(render_template("sentiment_analysis.html"))

@app.route("/sentiment_analysis_result",methods=["GET","POST"])
def sentiment_analysis_result():
    q = request.form.get("q")
    r=textblob.TextBlob(q).sentiment
    return(render_template("sentiment_analysis_result.html",r=r))

if __name__ == "__main__":
    app.run(debug=True)