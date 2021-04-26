from flask import Flask, render_template, request, flash, redirect
from decouple import config
from binance.client import Client
from binance.enums import *

app = Flask(__name__)
app.secret_key = b'ksjkjsdhflkjhasdflhlsakdfhdhfklsfkjef'

API_KEY = config("TEST_API_KEY")
SECRET_KEY = config("TEST_SECRET_KEY")
client = Client(API_KEY, SECRET_KEY)

# For paper trading
client.API_URL = "https://testnet.binance.vision/api"


@app.route("/")
def index():
    title = "CoinView"
    account = client.get_account()
    balances = account["balances"]

    exchange_info = client.get_exchange_info()

    symbols = exchange_info["symbols"]

    return render_template("index.html", title=title, my_balances=balances, symbols=symbols)


@app.route("/buy", methods=['POST'])
def buy():
    try:
        order = client.create_order(
        symbol=request.form['symbol'],
        side=SIDE_BUY,
        type=ORDER_TYPE_MARKET,
        quantity=request.form['quantity']
        )
    except Exception as error:
        flash(error.message, "error")

    return redirect('/')


@app.route("/sell")
def sell():
    return "sell"


@app.route("/settings")
def settings():
    return "settings"
