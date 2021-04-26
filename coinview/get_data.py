from decouple import config
from binance.client import Client
import csv

API_KEY = config('TEST_API_KEY')
SECRET_KEY = config('TEST_SECRET_KEY')
client = Client(API_KEY, SECRET_KEY)

prices = client.get_all_tickers()

# for price in prices:
#     print(price)

candles = client.get_klines(symbol='ETHUSDT', interval=Client.KLINE_INTERVAL_15MINUTE)

csvfile = open('2012-2021.csv', 'w', newline='')
candlestick_writer = csv.writer(csvfile, delimiter=',')

# for candlestick in candles:
#     candlestick_writer.writerow(candlestick)

# print(len(candles))

candlesticks = client.get_historical_klines("ETHUSDT", Client.KLINE_INTERVAL_5MINUTE, "1 Jan, 2012", "1 Apr, 2021")

for candlestick in candlesticks:
    candlestick_writer.writerow(candlestick)

csvfile.close()