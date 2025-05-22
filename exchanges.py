# exchange api wrappers
# currently just placeholders for future implementation

class BinanceAPI:
    def __init__(self, api_key=None, secret=None):
        self.api_key = api_key
        self.secret = secret

    def get_price(self, symbol):
        # TODO: implement actual api call
        raise NotImplementedError("Binance API not implemented yet")

    def get_balance(self):
        # TODO: implement
        raise NotImplementedError("Binance API not implemented yet")


class CoinbaseAPI:
    def __init__(self, api_key=None, secret=None):
        self.api_key = api_key
        self.secret = secret

    def get_price(self, symbol):
        # TODO: implement actual api call
        raise NotImplementedError("Coinbase API not implemented yet")

    def get_balance(self):
        # TODO: implement
        raise NotImplementedError("Coinbase API not implemented yet")