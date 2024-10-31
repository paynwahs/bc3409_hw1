from flask import Flask, render_template, request
import textblob


app = Flask(__name__)

@app.route("/",methods=["GET","POST"])
def sentiment_analysis():
    return(render_template("transfer_money.html"))

if __name__ == "__main__":
    app.run(debug=True)