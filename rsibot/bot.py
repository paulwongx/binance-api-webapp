import websocket, json, pprint, talib, numpy
from binance.client import Client
from binance.enums import *
from decouple import config

SOCKET = "wss://stream.binance.com:9443/ws/ethusdt@kline_1m"

closes = []

RSI_PERIOD = 14
RSI_OVERBOUGHT = 70
RSI_OVERSOLD = 30
TRADE_SYMBOL = "ETHUSD"
TRADE_QUANTITY = 0.05

closes = []
in_position = False

API_KEY = config("TEST_API_KEY")
SECRET_KEY = config("TEST_SECRET_KEY")
client = Client(API_KEY, SECRET_KEY)


def order(side, quantity, symbol, order_type=ORDER_TYPE_MARKET):
    try:
        print('sending order')
        order = client.create_order(symbol=symbol, side=side, type=order_type, quantity=quantity)
        print(order)
    except Exception as e:
        print('error',e)
        return False

    return True


def on_open(ws):
    print("opened connection")


def on_close(ws):
    print("closed connection")


def on_message(ws, message):
    global closes
    global in_position
    json_message = json.loads(message)
    # pprint.pprint(json_message)

    candle = json_message["k"]
    is_candle_closed = candle["x"]
    close = candle["c"]

    if is_candle_closed:
        print("candle closed at {}".format(close))
        closes.append(float(close))
        print("closes")
        print(closes)

        if len(closes) > RSI_PERIOD:
            np_closes = numpy.array(closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            print("all rsis calculated so far")
            print(rsi)
            last_rsi = rsi[-1]
            print("the current rsi is {}".format(last_rsi))

            if last_rsi > RSI_OVERBOUGHT:
                if in_position:
                    print("Overbought!! Sell sell sell")
                    # put binance sell logic here
                    order_succeeded = order(SIDE_SELL, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = False
                else:
                    print("It is overbought, but we don't own any. Nothing to do.")

            if last_rsi < RSI_OVERSOLD:
                if in_position:
                    print("it is oversold, but you already own it, nothing to do.")
                else:
                    print("buy buy buy")
                    # put binance buy order logic here
                    order_succeeded = order(SIDE_BUY, TRADE_QUANTITY, TRADE_SYMBOL)
                    if order_succeeded:
                        in_position = True


ws = websocket.WebSocketApp(SOCKET, on_open=on_open, on_close=on_close, on_message=on_message)
ws.run_forever()