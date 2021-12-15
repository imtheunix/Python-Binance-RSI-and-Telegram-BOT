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


def buy():
    order = client.create_order(
        symbol="NANOUSDT",
        side=SIDE_BUY,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=buy,
        price=price,
    )


def sell():
    order = client.create_order(
        symbol="NANOUSDT",
        side=SIDE_SELL,
        type=ORDER_TYPE_LIMIT,
        timeInForce=TIME_IN_FORCE_GTC,
        quantity=sell,
        price=price,
    )


"""'
Uncomment this if you want to send a telegram message
def send_msg(text):
    token = ""
    chat_id = ""
    url_req = "https://api.telegram.org/bot" + token + \
        "/sendMessage" + "?chat_id=" + chat_id + "&text=" + text
    results = requests.get(url_req)
"""


def on_message(ws, message):
    global closes, in_position, client, price, sell, buy, c, v
    client = Client(api_key, api_secret)
    json_message = json.loads(message)
    candle = json_message["k"]
    is_candle_closed = candle["x"]
    close = candle["c"]

    if is_candle_closed:
        closes.append(float(close))

        if len(closes) > RSI_PERIOD:
            clear()
            np_closes = numpy.array(closes)
            print(np_closes)
            rsi = talib.RSI(np_closes, RSI_PERIOD)
            last_rsi = rsi[-1]
            price = float(close)

            # Last price and Rsi span
            print(f"Last price: {price}" "\n")
            print(f"Last RSI: {last_rsi}" "\n")

            # Sell variables
            dict_pair = client.get_asset_balance(
                asset="NANO"
            )  # You have to the asset if you want another pair
            filter_pair = dict_pair.get("free")
            balance_pair = (
                float(filter_pair) - float(filter_pair) % 0.0001
            )  # This will do you balance - a percentage to always positionate a order
            sell = "{:.4f}".format(
                float(balance_pair)
            )  # Binance orders need to be formated, so we floated 4 digits to not have a problem with a discarted order like a 0.0000000000000000001 for example
            print(f"Avaible to sell: {sell}")
            sell_value = balance_pair * price
            print(f"Sell value in the other pair: {sell_value}" "\n")

            # Buy variables
            dict_buyer = client.get_asset_balance(
                asset="USDT"
            )  # You also have to change this if you want
            filter_buyer = dict_buyer.get("free")
            balance_buyer = (
                float(filter_buyer) - float(filter_buyer) % 0.0001
            )  # The same thing as above
            print(f"Avaible to buy: {balance_buyer}")
            buy_value = balance_buyer / price
            buy = "{:.4f}".format(float(buy_value))
            print(f"How much pair you can buy: {buy}" "\n")

            # Check if bought or selled
            orders = client.get_all_orders(
                symbol="NANOUSDT", limit=1
            )  # You also have to change this symbol
            orders_side = list(filter(lambda side: side["side"] == "BUY", orders))

            if orders_side:
                bought = 1
            else:
                bought = 0

            if bought == 1:
                c += 1
                v = 0
                print(f"Bought at {c} candles")
            else:
                v += 1
                c = 0
                print(f"Selled at {v} candles")

            if last_rsi < RSI_OVERSOLD:
                if bought == 1:
                    return on_message()
                else:
                    buy()

                    """''
                    send_msg(
                        f"Selled PAIR, graph {interval}, Price: {price} | Qtd: {buy} | @RSI: {last_rsi}")
                    """ ""

            if last_rsi > RSI_OVERBOUGHT:
                if bought == 0:
                    return on_message()
                else:
                    sell()

                    """''
                    send_msg(
                        f"Vendido BNB, graph {interval}, Price: {price} | Qtd:{sell} | @RSI: {last_rsi}")
                    """ ""


ws = websocket.WebSocketApp(socket, on_message=on_message)

ws.run_forever()
