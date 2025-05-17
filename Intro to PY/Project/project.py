from tracker import add_transaction
from tracker import view_transactions
from tracker import view_summary

def main():

    while True:
        try:
            choice = int(input("Welcome to Smart Budget Tracker! \nWhat would you like to do? \n1. Add a transaction \n2. View all transactions \n3. View summary \n4. Exit \nEnter choice: "))

            if choice == 1:
                add_transaction()
            elif choice == 2:
                view_transactions()
            elif choice == 3:
                view_summary()
            elif choice == 4:
                break
            else:
                print("Please enter a valid choice")
        except ValueError:
            print("Please enter a number from 1 to 4")
if __name__ == "__main__":
    main()