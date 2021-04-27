from flask import Flask, render_template, request, flash, redirect, jsonify
from flask_cors import CORS, cross_origin
from decouple import config
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
app.secret_key = b"ksjkjsdhflkjhasdflhlsakdfhdhfklsfkjef"

FLASK_ENV = config("FLASK_ENV")
print(FLASK_ENV)

if config("FLASK_ENV") == "production":
    print("using production keys")
    API_KEY = config("REAL_API_KEY")
    SECRET_KEY = config("REAL_SECRET_KEY")
else:
    print("using development keys")
    API_KEY = config("TEST_API_KEY")
    SECRET_KEY = config("TEST_SECRET_KEY")

client = Client(API_KEY, SECRET_KEY)

cors = CORS(app)
# app.config['CORS_HEADERS'] = 'Content-Type'

# For paper trading
if config("FLASK_ENV") == "development":
    print("using development url")
    client.API_URL = "https://testnet.binance.vision/api"


@app.route("/")
def index():
    title = "CoinView"
    account = client.get_account()
    balances = account["balances"]

    exchange_info = client.get_exchange_info()

    symbols = exchange_info["symbols"]

    return render_template("index.html", title=title, my_balances=balances, symbols=symbols)


@app.route("/buy", methods=["POST"])
def buy():
    try:
        order = client.create_order(
            symbol=request.form["symbol"], side=SIDE_BUY, type=ORDER_TYPE_MARKET, quantity=request.form["quantity"]
        )
    except Exception as error:
        flash(error, "error")

    return redirect("/")


@app.route("/sell")
def sell():
    return "sell"


@app.route("/settings")
def settings():
    return "settings"


@app.route("/history")
@cross_origin()
def history():
    candlesticks = client.get_historical_klines(
        "BTCBUSD", Client.KLINE_INTERVAL_15MINUTE, "2021-26-01 06:15:11", "2021-26-04 06:15:11"
    )
    print("length of data", len(candlesticks))
    processed_candlesticks = []

    for data in candlesticks:
        candlestick = {"time": data[0] / 1000, "open": data[1], "high": data[2], "low": data[3], "close": data[4]}
        processed_candlesticks.append(candlestick)

    return jsonify(processed_candlesticks)