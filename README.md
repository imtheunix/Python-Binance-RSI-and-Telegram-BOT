# Python Binance Bot TALIB & NUMPY

A trading bot using Python and its tools:
This is my Open source Trading Bot for Binance, feel free to use my code to do your on bot, it has a option to do a message on telegram

Disclaimer, don't do any trades with this bot running, the python-binance framework does not have a specific end-point to fetch the completed orders, so we must track the last order.

The bot will start work when it passes the rsi period, so if you place a long period it would take the size of the candle \* rsi period to start his job.

First step you must configure these variables:

cc = The pair you want to observe, in my example i will use NANOUSDT.

interval = The interval of the candle, i'm using 1m to do the example but more time more better.

api_key = You have to create a api key with rights to do orders.

api_secret = Here is the secret key.

assets = You must change the assets values if you want to trade another pair

Basicaly, follow the comments of the code and you will run the bot.

Second step you must start the bot python main.py:

If you see only the price on your screen you didn't configured the API correctly

It's not my responsibility if you lose or win money with this, this is just a example.
