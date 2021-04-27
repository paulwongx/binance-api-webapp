import datetime
import backtrader as bt
import pandas as pd

class RSIStrategy(bt.Strategy):
    def __init__(self)


cerebro = bt.Cerebro()

crypt_df = pd.read_csv(
    "./data/daily.csv",
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

data = bt.feeds.PandasDirectData(dataname=crypt_df)

cerebro.adddata(data)

cerebro.run()

cerebro.plot()




