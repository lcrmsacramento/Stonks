from flask import Flask, render_template, url_for,abort, Response
from flask_bootstrap import Bootstrap
from flask import Flask, request, render_template
import yfinance as yf

app = Flask(__name__)
Bootstrap(app)

@app.route("/")
def home():
    return render_template("index.html",title="stonks")


@app.route("/teste")
def test():
    return render_template("index.html")


@app.route("/stonks")
def stonks():
    return render_template("index.html")

# API Route for pulling the stock quote
@app.route("/quote")
def display_quote():
	# get a stock ticker symbol from the query string
	# default to AAPL
	symbol = request.args.get('symbol', default="AAPL")

	# pull the stock quote
	quote = yf.Ticker(symbol)

	#return the object via the HTTP Response
	return quote.info

# API route for pulling the stock history
@app.route("/history")
def display_history():
	#get the query string parameters
	symbol = request.args.get('symbol', default="AAPL")
	period = request.args.get('period', default="1y")
	interval = request.args.get('interval', default="1mo")

	#pull the quote
	quote = yf.Ticker(symbol)	
	#use the quote to pull the historical data from Yahoo finance
	hist = quote.history(period=period, interval=interval)
	#convert the historical data to JSON
	data = hist.to_json()
	#return the JSON in the HTTP response
	return data


if __name__=='__main__':
    
    app.run(debug=True)