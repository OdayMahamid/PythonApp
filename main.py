from flask import Flask
import requests


app = Flask(__name__)


@app.route('/BitcoinPrice')
def BitcoinPrice():
    SumPrices = 0
    # request's response
    response = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
    # get the http request's response as a json object
    data = response.json()
    CurrentPrice = data["bpi"]["USD"]["rate"]
    # request's response
    response2 = requests.get('https://min-api.cryptocompare.com/data/v2/histominute?fsym=BTC&tsym=USD&limit=10')
    # get the http request's response as a json object
    DataLast10minutes = response2.json()
    for i in range(10):
        # sum the prices in approximately in one minute
        SumPrices = SumPrices + (DataLast10minutes['Data']["Data"][i]['close'])
    # average in last 10 minutes
    AvgPrice = SumPrices / 10

    return "Average USD Bitcoin Price: " + '{:,.2f}'.format(AvgPrice)+ "$<br/>" + " Current USD Bitcoin Price: " + CurrentPrice + "$"


if __name__ == '__main__':
    app.run(host="0.0.0.0", debug=True)
