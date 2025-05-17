import csv
import os

FILENAME = "data.csv"

def save_transaction(type, category, amount, date):
    file_exists = os.path.isfile(FILENAME)
    with open(FILENAME, mode="a", newline="") as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["type", "category", "amount", "date"])
        writer.writerow([type, category, amount, date])
