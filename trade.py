from datetime import datetime

class Trade:
    def __init__(self, symbol, side, amount, price, exchange="binance", timestamp=None):
        self.symbol = symbol
        self.side = side  # buy or sell
        self.amount = amount
        self.price = price
        self.exchange = exchange
        self.timestamp = timestamp or datetime.now()

    def get_value(self):
        return self.amount * self.price

    def __repr__(self):
        return f"Trade({self.symbol}, {self.side}, {self.amount}@{self.price})"