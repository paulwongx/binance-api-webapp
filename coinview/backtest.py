import datetime
import backtrader as bt
import pandas as pd

class RSIStrategy(bt.Strategy):
    def __init__(self):
        self.rsi = bt.indicators.RSI(self.data, period=14)

    def next(self):
        if self.rsi < 40 and not self.position:
            self.buy(size=1)
        if self.rsi > 70 and self.position:
            self.close()


cerebro = bt.Cerebro()

crypt_df = pd.read_csv(
    "./data/2021_15minutes.csv",
    header=None,
    names=[
        "timestamp",
        "open",
        "high",
        "low",
        "close",
        "volume",
        "close_time",
        "quote_asset_vol",
        "num_trades",
        "taker_buy_base_asset",
        "taker_buy_quote_asset",
        "ignore",
    ],
    parse_dates=True,
)

convert = lambda x: datetime.datetime.fromtimestamp(x / 1e3)
crypt_df["timestamp"] = crypt_df["timestamp"].apply(convert)

crypt_df.set_index('timestamp', inplace=True)

print(crypt_df.head())

fromdate = datetime.datetime.strptime('2021-01-01', '%Y-%m-%d')
todate = datetime.datetime.strptime('2021-03-01', '%Y-%m-%d')

data = bt.feeds.PandasDirectData(dataname=crypt_df, compression=15, timeframe=bt.TimeFrame.Minutes, fromdate=fromdate, todate=todate)

cerebro.adddata(data)

cerebro.addstrategy(RSIStrategy)
cerebro.run()

cerebro.plot()




