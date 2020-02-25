from flask import Flask, render_template, request
import twitter2
import lab3
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'
app = Flask(__name__)
app.config["DEBUG"] = True
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

@app.route("/", methods = ['GET', 'POST'])
def index():
    return render_template("index.html")

@app.route("/results", methods = ['POST', 'GET'])
def show_map():
    variable = request.form['acc']
    file = twitter2.get_input(variable)

    contex = {"m": lab3.get_started(file)}
    return render_template("Map.html", **contex)

if __name__ == "__main__":
    app.run(debug=True)
