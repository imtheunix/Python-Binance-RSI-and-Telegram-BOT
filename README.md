# Python Binance Bot TALIB & NUMPY

A trading bot using Python and its tools:
This is my Open source Trading Bot for Binance, feel free to use my code to do your on bot, it has a option to do a message on telegram

Disclaimer, don't do any trades with this bot running, the python-binance framework does not have a specific end-point to fetch the completed orders, so we must track the last order.

First step you must configure these variables:

cc = The pair you want to observe, in my example i will use NANOUSDT.

interval = The interval of the candle, i'm using 1m to do the example but more time more better.

api_key = You have to create a api key with rights to do orders.

api_secret = Here is the secret key.
