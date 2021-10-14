
from flask import Flask
import requests
import time

app = Flask(__name__)


@app.route('/BitcoinPrice')
def BitcoinPrice():
    timeout = time.time() + 60
    sumPrice = 0
    count=0
    while time.time() < timeout:
        count = count+1
        # request's response
        response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        # get the http request's response as a json object
        data = response.json()
        USDprice = (data["bpi"]["USD"]["rate"])
        CurrentPrice = USDprice.replace("$", "").replace(",", "")
        sumPrice = sumPrice + float(CurrentPrice)

    AvgPrice = sumPrice / count
    return "Average USD Bitcoin Price: " + str(AvgPrice)+"$<br/>"+" Current USD Bitcoin Price: " + CurrentPrice+"$"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
