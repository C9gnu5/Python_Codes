from datetime import datetime

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance
        self.interest = 0.03
        self.transaction_history = [(datetime.now().strftime("%Y-%m-%d %H:%M:%S"), f"Account Created for {self.owner}")]

    def deposit(self):
        amount = int(input("Enter amount to deposit: "))
        if amount > 0:
            self.balance += amount
            print(f"Deposited {amount} into {self.owner}'s account. New balance: {self.balance}")
            self.transaction_history.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Deposited: "+str(amount)))
        else:
            print("Error: Cannot Deposit Negative Amount.")

    def withdraw(self):
        amount = int(input("Enter amount to withdraw: "))
        if self.balance >= amount:
            if amount > 0:
                self.balance -= amount
                print(f"Withdrew {amount} from {self.owner}'s account. New balance: {self.balance}")
                self.transaction_history.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Withdrew: "+str(amount)))
            else:
                print("Error: Cannot Withdraw a Negative Amount.")
        else:
            print("Insufficient funds")

    def display_balance(self):
        print(f"{self.owner}'s account balance: {self.balance}")

    def apply_interest(self):
        interest = self.balance * self.interest
        self.balance += interest
        print(f"{100 * self.interest}% interest applied. New balance: {self.balance} ")
        self.transaction_history.append((datetime.now().strftime("%Y-%m-%d %H:%M:%S"), "Applied Interest: "+str(interest)))

    def show_history(self):
        print(self.transaction_history)


class Bank_book:
    def __init__(self):
        self.accounts = {}

    def create_account(self):
        owner = input("Enter Owner's Name: ").casefold()
        initial_balance = int(input("Enter initial balance: "))
        if owner not in self.accounts:
            account = BankAccount(owner, initial_balance)
            self.accounts[owner] = account
            print(f"Account created for {owner} with initial balance: {initial_balance}")
        else:
            print("Account already exists.")

    def delete_account(self):
        owner = input("Enter Owner's Name: ").casefold()
        if owner in self.accounts:
            del self.accounts[owner]
            print(f"Account for {owner} has been deleted.")
        else:
            print("Account does not exist.")

    def retrieve_account(self):
        owner = input("Enter Owner's Name: ").casefold()
        if owner in self.accounts:
            return self.accounts[owner]
        else:
            print("Account does not exist. Please create an account first!")


def main():
    try:
        c = int(input("""
[1]Create Account
[2]Delete Account
[3]Deposit
[4]Withdraw
[5]View Transaction History
[6]Exit
"""))
        if c == 1:
            acct_book.create_account()
            main()
        elif c == 2:
            acct_book.delete_account()
            main()
        elif c == 3:
            account = acct_book.retrieve_account()
            if account:
                account.deposit()
            main()
        elif c == 4:
            account = acct_book.retrieve_account()
            if account:
                account.withdraw()
            main()
        elif c == 5:
            account = acct_book.retrieve_account()
            if account:
                account.show_history()
            main()
        elif c == 6:
            exit()
    except ValueError:
        print("Somthing went wrong. Please try again!")
        main()

acct_book = Bank_book()
main()
