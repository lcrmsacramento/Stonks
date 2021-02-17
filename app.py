from flask import Flask, render_template, url_for
from flask_bootstrap import Bootstrap
import json
app = Flask(__name__)
Bootstrap(app)

# define variables for data retrieval


@app.route("/")
def home():
    return render_template("index.html",title="stonks")


def retrieve_data():
    # create dictionary for saving current prices
    current_prices = {}
    for currency in currencies:
        current_prices[currency] = []
    # append new time to list of times
    times.append(time.strftime('%H:%M:%S'))

    # make request to API and get response as object
    api_url = "https://min-api.cryptocompare.com/data/pricemulti?fsyms={}&tsyms=USD".format(",".join(currencies))
    response = json.loads(requests.get(api_url).content)

    # append new price to list of prices for graph
    # and set current price for bar chart
    for currency in currencies:
        price = response[currency]['USD']
        current_prices[currency] = price
        prices[currency].append(price)

    # create an array of traces for graph data
    graph_data = [go.Scatter(
        x=times,
        y=prices.get(currency),
        name="{} Prices".format(currency)
    ) for currency in currencies]

    # create an array of traces for bar chart data
    bar_chart_data = [go.Bar(
        x=currencies,
        y=list(current_prices.values())
    )]

    data = {
        'graph': json.dumps(list(graph_data), cls=plotly.utils.PlotlyJSONEncoder),
        'bar_chart': json.dumps(list(bar_chart_data), cls=plotly.utils.PlotlyJSONEncoder)
    }

    # trigger event
    pusher.trigger("crypto", "data-updated", data)


if __name__=='__main__':
    times = []
    currencies = ["BTC"]
    prices = {"BTC": []}
    app.run(debug=True)