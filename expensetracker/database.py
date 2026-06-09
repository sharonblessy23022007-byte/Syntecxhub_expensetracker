import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect("expenses.db")
        self.cursor = self.conn.cursor()

        self.cursor.execute("""
        CREATE TABLE IF NOT EXISTS transactions(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            date TEXT,
            category TEXT,
            amount REAL,
            type TEXT
        )
        """)

        self.conn.commit()

    def add_transaction(self, date, category, amount, trans_type):
        self.cursor.execute("""
        INSERT INTO transactions(date, category, amount, type)
        VALUES (?, ?, ?, ?)
        """, (date, category, amount, trans_type))

        self.conn.commit()

    def get_all_transactions(self):
        self.cursor.execute("SELECT * FROM transactions")
        return self.cursor.fetchall()

    def get_monthly_summary(self, year, month):

        pattern = f"{year}-{month:02d}%"

        self.cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE type='income' AND date LIKE ?
        """, (pattern,))
        income = self.cursor.fetchone()[0] or 0

        self.cursor.execute("""
        SELECT SUM(amount)
        FROM transactions
        WHERE type='expense' AND date LIKE ?
        """, (pattern,))
        expense = self.cursor.fetchone()[0] or 0

        return {
            "income": income,
            "expense": expense,
            "balance": income - expense
        }

    def close(self):
        self.conn.close()