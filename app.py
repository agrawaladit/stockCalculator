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
            change = stock.json()['c'] - stock.json()['pc']
            current = stock.json()['c']
            percent = (change/current) * 100

            if change > 0: change = '+'+str(round(change, 2))
            else: change = round(change, 2)
            if change > 0: percent = '+'+str(round(percent,2))
            else: percent = round(percent, 2)
            if profile.json() and stock.json():
                return render_template('details.html', date=datetime.datetime.now().strftime("%a %b %d %H:%M:%S PDT %Y"), name=profile.json()['name'],
                                       ticker=profile.json()['ticker'], current=round(current ,2),
                                       change=change, percent=percent)
            else:
                return render_template('error.html', message="Invalid Symbol")
        except:
            return render_template('error.html', message="Error Retrieving Data")
    else:
        return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
