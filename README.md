# Binance API Webapp

## Notes

Binance websocket stream
wss://stream.binance.com:9443
wss://stream.binance.com:9443/ws/ethusdt@trade
wss://stream.binance.com:9443/ws/ethusdt@kline_5m

```py
# pipe data to file
# $ wscat -c wss://stream.binance.com:9443/ws/ethusdt@kline_5m | tee dataset.txt

# @trade
{"e":"trade","E":1619385423298,"s":"ETHUSDT","t":376891502,"p":"2238.42000000","q":"0.00565000","b":3753381752,"a":3753381874,"T":1619385423297,"m":true,"M":true}

# @kline_5m
{"e":"kline","E":1619385700342,"s":"ETHUSDT","k":{
    "t":1619385600000,"T":1619385899999,"s":"ETHUSDT","i":"5m","f":376896116,"L":376899041,"o":"2233.37000000","c":"2220.51000000","h":"2235.04000000","l":"2220.36000000","v":"1668.28293000","n":2926,"x":false,"q":"3716272.52683850","V":"825.55535000","Q":"1838869.04378320","B":"0"}
}

# python-binance kline response
[
    [
        1499040000000,      # Open time
        "0.01634790",       # Open
        "0.80000000",       # High
        "0.01575800",       # Low
        "0.01577100",       # Close
        "148976.11427815",  # Volume
        1499644799999,      # Close time
        "2434.19055334",    # Quote asset volume
        308,                # Number of trades
        "1756.87402397",    # Taker buy base asset volume
        "28.46694368",      # Taker buy quote asset volume
        "17928899.62484339" # Can be ignored
    ]
]
```
Current video
https://www.youtube.com/watch?v=EeT3Ore4Sao
## Reference

[Tutorial Link](https://www.youtube.com/watch?v=rvhnz1yBHgQ)
[Binance Websocket API Documentation](https://github.com/binance/binance-spot-api-docs/blob/master/web-socket-streams.md)
[Binance Docs](https://binance-docs.github.io/apidocs/spot/en/#compressed-aggregate-trades-list)
[Python Binance Read The Docs](https://python-binance.readthedocs.io/en/latest/market_data.html#id6)
[JavaScript Technical Indicators](https://github.com/anandanand84/technicalindicators)
[CryptoSignal](https://github.com/CryptoSignal/Crypto-Signal)