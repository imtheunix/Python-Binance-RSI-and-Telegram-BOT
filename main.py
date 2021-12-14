import websocket
import talib
import numpy
import json
import os
import requests
from binance import Client
from binance.enums import *

# Clear CMD
def clear():
    return os.system("cls")


# Client and Socket Parameters
cc = "nanousdt"
interval = "1m"
api_key = "Your api key"
api_secret = "Your api secret"
socket = f"wss://stream.binance.com:9443/ws/{cc}@kline_{interval}"  # Dont change this.

# Strategy
RSI_PERIOD = 1
RSI_OVERBOUGHT = 68
RSI_OVERSOLD = 32

# Declaring variables
closes = []
c = 0  # When c is different than 0 we are buying for c candles
v = 0  # When v is different than 0 we are selling for v candles


def comprar():
    global preco_compra
    preco_compra = price
    ordem = client.create_order(
        symbol="NANOUSDT",
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=buy,
        price=price,
    )


def vender():
    ordem = client.create_order(
        symbol="NANOUSDT",
        side=SIDE_SELL,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=sell,
        price=price,
    )
