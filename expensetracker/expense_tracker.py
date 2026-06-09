from database import Database
from models import Transaction
from utils import export_to_csv
from datetime import datetime

db = Database()

def add_income():

    date = input("Date (YYYY-MM-DD): ")

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    amount = float(input("Income Amount: "))

    t = Transaction(date, "Income", amount, "income")

    if t.validate():
        db.add_transaction(
            date,
            "Income",
            amount,
            "income"
        )

        print("✓ Income Added")

def add_expense():

    date = input("Date (YYYY-MM-DD): ")

    if not date:
        date = datetime.now().strftime("%Y-%m-%d")

    category = input("Category: ")

    amount = float(input("Expense Amount: "))

    t = Transaction(
        date,
        category,
        amount,
        "expense"
    )

    if t.validate():
        db.add_transaction(
            date,
            category,
            amount,
            "expense"
        )

        print("✓ Expense Added")

def view_transactions():

    data = db.get_all_transactions()

    print("\nALL TRANSACTIONS")

    print("-"*70)

    for row in data:
        print(row)

def monthly_summary():

    year = int(input("Year: "))
    month = int(input("Month: "))

    result = db.get_monthly_summary(
        year,
        month
    )

    print("\nMONTHLY SUMMARY")

    print(
        f"Income  : ${result['income']:.2f}"
    )

    print(
        f"Expense : ${result['expense']:.2f}"
    )

    print(
        f"Balance : ${result['balance']:.2f}"
    )

def export_data():

    data = db.get_all_transactions()

    filename = "expenses.csv"

    export_to_csv(
        data,
        filename
    )

while True:

    print("\n" + "="*40)
    print("EXPENSE TRACKER CLI")
    print("="*40)

    print("1. Add Income")
    print("2. Add Expense")
    print("3. View Transactions")
    print("4. Monthly Summary")
    print("5. Export CSV")
    print("6. Exit")

    choice = input("\nChoice: ")

    if choice == "1":
        add_income()

    elif choice == "2":
        add_expense()

    elif choice == "3":
        view_transactions()

    elif choice == "4":
        monthly_summary()

    elif choice == "5":
        export_data()

    elif choice == "6":
        db.close()
        break

    else:
        print("Invalid Choice")