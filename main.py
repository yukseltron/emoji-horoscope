from flask import Flask, render_template, request
import emoji

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/', methods=['POST'])
def result():
    sign = request.form['sign']
    emojiPrediction = emoji.analyzeScope(sign)
    return render_template("result.html", horoscope = emojiPrediction)
