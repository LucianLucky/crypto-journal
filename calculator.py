class PnLCalculator:
    def __init__(self):
        self.positions = {}

    def process_trade(self, trade):
        symbol = trade.symbol
        if symbol not in self.positions:
            self.positions[symbol] = {
                'amount': 0,
                'avg_price': 0,
                'total_cost': 0
            }

        pos = self.positions[symbol]

        if trade.side == 'buy':
            new_amount = pos['amount'] + trade.amount
            new_cost = pos['total_cost'] + (trade.amount * trade.price)
            pos['amount'] = new_amount
            pos['total_cost'] = new_cost
            pos['avg_price'] = new_cost / new_amount if new_amount > 0 else 0
        elif trade.side == 'sell':
            if pos['amount'] >= trade.amount:
                pos['amount'] -= trade.amount
                pos['total_cost'] -= (trade.amount * pos['avg_price'])

    def get_pnl(self, symbol, current_price):
        if symbol not in self.positions:
            return 0

        pos = self.positions[symbol]
        if pos['amount'] == 0:
            return 0

        current_value = pos['amount'] * current_price
        return current_value - pos['total_cost']

    def get_position(self, symbol):
        return self.positions.get(symbol, None)