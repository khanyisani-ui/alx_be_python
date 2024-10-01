class BankAccount:
    def __init__(self, initial_balance=0):
        self.account_balance = initial_balance

    def deposit(self, amount):
        if amount > 0:
            self.account_balance += amount
            print(f"Deposited: ${amount:.2f}")
        else:
            print("Deposit amount must be positive.")

    def withdraw(self, amount):
        """Deducts the amount from the account balance if funds are sufficient.
        
        Returns True if withdrawal was successful, False otherwise.
        """
        if amount <= 0:
            print("Withdrawal amount must be positive.")
            return False
        if amount <= self.account_balance:
            self.account_balance -= amount
            print(f"Withdrew: ${amount:.2f}")
            return True
        else:
            print("Insufficient funds.")
            return False

    def display_balance(self):
        """Prints the current account balance in a user-friendly format."""
        print(f"Current balance: ${self.account_balance:.2f}")