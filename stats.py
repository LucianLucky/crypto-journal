from collections import defaultdict

class Stats:
    def __init__(self, trades):
        self.trades = trades

    def total_trades(self):
        return len(self.trades)

    def trades_by_symbol(self):
        by_symbol = defaultdict(int)
        for trade in self.trades:
            by_symbol[trade[1]] += 1
        return dict(by_symbol)

    def volume_by_exchange(self):
        by_exchange = defaultdict(float)
        for trade in self.trades:
            symbol, side, amount, price, exchange = trade[1], trade[2], trade[3], trade[4], trade[5]
            by_exchange[exchange] += amount * price
        return dict(by_exchange)

    def buy_sell_ratio(self):
        buys = sum(1 for t in self.trades if t[2] == 'buy')
        sells = sum(1 for t in self.trades if t[2] == 'sell')
        return {'buy': buys, 'sell': sells}

    def total_volume(self):
        return sum(t[3] * t[4] for t in self.trades)