from flask import Flask, render_template, request
import requests
import datetime

app = Flask(__name__)


@app.route('/', methods=["POST", "GET"])
def index():
    if request.method == 'POST':
        try:
            symbol = request.form['symbol']
            profile = requests.get(
                f'https://finnhub.io/api/v1/stock/profile2?symbol={symbol}&token=butkvvv48v6qj1ddtp10')
            stock = requests.get(f'https://finnhub.io/api/v1/quote?symbol={symbol}&token=butkvvv48v6qj1ddtp10')
            if profile.json() and stock.json():
                return render_template('details.html', date=datetime.datetime.now(), name=profile.json()['name'],
                                       ticker=profile.json()['ticker'], current=stock.json()['c'],
                                       change=stock.json()['c'] - stock.json()['pc'])
            else:
                return render_template('error.html', message="Invalid Symbol")
        except:
            return render_template('error.html', message="Error Retrieving Data")
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
