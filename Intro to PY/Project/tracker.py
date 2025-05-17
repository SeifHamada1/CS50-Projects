from datetime import datetime
from storage import save_transaction
import csv
import os
from collections import defaultdict



#add_transaction function
def get_valid_amount():
    while True:
        try:
            amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be a positive number.")
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")

def get_valid_amount(input_value=None):
    while True:
        try:
            if input_value is not None:
                amount = float(input_value)
            else:
                amount = float(input("Enter amount: "))
            if amount <= 0:
                print("Amount must be a positive number.")
                if input_value is not None:
                    return None
            else:
                return amount
        except ValueError:
            print("Please enter a valid number.")
            if input_value is not None:
                return None
        if input_value is not None:
            break
        
def get_valid_date(input_value=None):
    from datetime import datetime
    while True:
        if input_value is not None:
            date_str = input_value.strip()
        else:
            date_str = input("Enter date (YYYY-MM-DD) or press Enter for today: ").strip()
        if date_str == "":
            return datetime.today().strftime("%Y-%m-%d")
        try:
            datetime.strptime(date_str, "%Y-%m-%d")
            return date_str
        except ValueError:
            print("Date format is incorrect. Please use YYYY-MM-DD.")
            if input_value is not None:
                return None
        if input_value is not None:
            break

def add_transaction():
    type = input("Income or Expense? ").lower().strip()
    if type == "income":
        category = "Income"
        amount = get_valid_amount()
        date = get_valid_date()
    elif type == "expense":
        category = input("Which category? \nfood, \nrent, \nbills, \nother.\nType your category: ").lower().strip()
        amount = get_valid_amount()
        date = get_valid_date()
    else:
        print("Please enter a valid choice ('income' or 'expense')")
        return

    print(f"Type: {type}, Category: {category}, Amount: {amount}, Date: {date}")
    save_transaction(type, category, amount, date)
    print("✅ Transaction saved successfully.")




#view_transactions function

FILENAME = "data.csv"

def view_transactions():
    if not os.path.isfile(FILENAME):
        print("No transactions found yet.")
        return

    with open(FILENAME, mode="r") as file:
        reader = csv.reader(file)
        transactions = list(reader)

        if len(transactions) <= 1:
            print("No transactions recorded yet.")
            return

        transactions[1:] = sorted(transactions[1:], key=lambda x: x[3])

        print("\n--- All Transactions ---")
        print(f"{'Type':<10} | {'Category':<15} | {'Amount':<10} | {'Date':<12}")
        print("-" * 55)

        for row in transactions[1:]:
            print(f"{row[0]:<10} | {row[1]:<15} | {row[2]:<10} | {row[3]:<12}")
        print()



#view_summary function

def view_summary():
    try:
        with open("data.csv", mode="r") as file:
            reader = csv.DictReader(file)
            total_income = 0
            total_expense = 0
            category_totals = defaultdict(float)

            for row in reader:
                amount = float(row["amount"])
                if row["type"] == "income":
                    total_income += amount
                elif row["type"] == "expense":
                    total_expense += amount
                    category_totals[row["category"]] += amount

            balance = total_income - total_expense

            print("\n------ Budget Summary ------")
            print(f"Total Income:     {total_income:.2f}")
            print(f"Total Expenses:   {total_expense:.2f}")
            print(f"Balance:          {balance:.2f}")
            print("\nExpenses by Category:")
            for category, total in category_totals.items():
                print(f"  {category}:      {total:.2f}")
            print("-----------------------------\n")

    except FileNotFoundError:
        print("No transactions found. Add some transactions first.")





