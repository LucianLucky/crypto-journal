import sqlite3
from datetime import datetime

class Database:
    def __init__(self, db_path="trades.db"):
        self.db_path = db_path
        self.init_db()

    def init_db(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            CREATE TABLE IF NOT EXISTS trades (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                symbol TEXT NOT NULL,
                side TEXT NOT NULL,
                amount REAL NOT NULL,
                price REAL NOT NULL,
                exchange TEXT,
                timestamp TEXT NOT NULL
            )
        ''')
        conn.commit()
        conn.close()

    def add_trade(self, trade):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('''
            INSERT INTO trades (symbol, side, amount, price, exchange, timestamp)
            VALUES (?, ?, ?, ?, ?, ?)
        ''', (trade.symbol, trade.side, trade.amount, trade.price,
              trade.exchange, trade.timestamp.isoformat()))
        conn.commit()
        conn.close()

    def get_all_trades(self):
        conn = sqlite3.connect(self.db_path)
        c = conn.cursor()
        c.execute('SELECT * FROM trades ORDER BY timestamp DESC')
        rows = c.fetchall()
        conn.close()
        return rows