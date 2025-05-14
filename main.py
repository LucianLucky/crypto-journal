import argparse
from datetime import datetime
from trade import Trade
from database import Database
from stats import Stats

def main():
    parser = argparse.ArgumentParser(description='Crypto Trading Journal')
    parser.add_argument('action', choices=['add', 'list', 'stats'], help='Action to perform')
    parser.add_argument('--symbol', help='Trading symbol (e.g. BTC/USDT)')
    parser.add_argument('--side', choices=['buy', 'sell'], help='Trade side')
    parser.add_argument('--amount', type=float, help='Trade amount')
    parser.add_argument('--price', type=float, help='Trade price')
    parser.add_argument('--exchange', default='binance', help='Exchange name')

    args = parser.parse_args()
    db = Database()

    if args.action == 'add':
        if not all([args.symbol, args.side, args.amount, args.price]):
            print("Error: add requires --symbol, --side, --amount, --price")
            return

        trade = Trade(args.symbol, args.side, args.amount, args.price, args.exchange)
        db.add_trade(trade)
        print(f"Trade added: {trade}")

    elif args.action == 'list':
        trades = db.get_all_trades()
        if not trades:
            print("No trades found")
        else:
            for t in trades:
                print(f"ID: {t[0]} | {t[1]} | {t[2]} | Amount: {t[3]} | Price: {t[4]} | Exchange: {t[5]} | {t[6]}")

    elif args.action == 'stats':
        trades = db.get_all_trades()
        if not trades:
            print("No trades to analyze")
            return

        stats = Stats(trades)
        print(f"Total trades: {stats.total_trades()}")
        print(f"Total volume: ${stats.total_volume():.2f}")
        print(f"Buy/Sell ratio: {stats.buy_sell_ratio()}")
        print(f"Trades by symbol: {stats.trades_by_symbol()}")
        print(f"Volume by exchange: {stats.volume_by_exchange()}")

if __name__ == '__main__':
    main()