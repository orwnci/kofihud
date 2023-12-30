import re

class Transaction:
    def __init__(self, date, amount, category):
        self.date = date
        self.amount = amount
        self.category = category

class Account:
    def __init__(self):
        self.transactions = []

    def add_transaction(self, transaction):
        self.transactions.append(transaction)

    def get_balance(self):
        balance = 0
        for transaction in self.transactions:
            balance += transaction.amount
        return balance

    def filter_transactions(self, start_date, end_date, category=None):
        filtered_transactions = []
        for transaction in self.transactions:
            if start_date <= transaction.date <= end_date:
                if category is None or transaction.category == category:
                    filtered_transactions.append(transaction)
        return filtered_transactions

if object is not None:
    result=object.groups()
else:
    result = None

    def main(self):
        account = Account()

        while True:
            print("1. Add transaction")
            print("2. Get balance")
            print("3. Filter transactions")
            print("4. Exit")

            choice = input("Select an action: ")

            if choice == "1":
                date = input("Enter the transaction date: ")
                amount = float(input("Enter the transaction amount: "))
                category = input("Enter the transaction category: ")

                transaction = Transaction(date, amount, category)
                account.add_transaction(transaction)
                print("Transaction added")

            elif choice == "2":
                balance = account.get_balance()
                print("Current balance: ", balance)

            elif choice == "3":
                start_date = input("Enter start date: ")
                end_date = input("Enter end date: ")
                category = input("Enter category (or press Enter to display all categories): ")

                filtered_transactions = account.filter_transactions(start_date, end_date, category)
                print("Filtered transactions:")
                for transaction in filtered_transactions:
                    print(transaction.date, transaction.amount, transaction.category)

            elif choice == "4":
                break
            else:
                print("Invalid input. Try again.")

if __name__ == "__main__":
    account = Account()
    account.main()
