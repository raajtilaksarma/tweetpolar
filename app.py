from flask import Flask, render_template, request
from tweet import Tweety

app = Flask(__name__)

def showTweets(word):
    ti = Tweety()
    ti.getTweets('Trump')
    res = ti.polarizedTweets()
    return res[0]
    
@app.route("/", methods=['POST','GET'])
def index():
    tweets = ''
    if request.method=='POST':
        word = request.form['word']
        tweets = showTweets(word)
        print(tweets)
    return render_template('index.html',tweets=tweets)
if __name__ == "__main__":
    app.run()