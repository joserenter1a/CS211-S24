"""
A simple GUI for a bank account
"""

import tkinter as tk
from bankacct_sol import BankAccount


class BankAccountUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Bank Account")
        
        self.account_number_label = tk.Label(self.root, text="Account Number:")
        self.account_number_label.pack()
        self.account_number_entry = tk.Entry(self.root)
        self.account_number_entry.pack()
        
        self.amount_label = tk.Label(self.root, text="Amount:")
        self.amount_label.pack()
        self.amount_entry = tk.Entry(self.root)
        self.amount_entry.pack()
        
        self.deposit_button = tk.Button(self.root, text="Deposit", command=self.deposit)
        self.deposit_button.pack()
        self.withdraw_button = tk.Button(self.root, text="Withdraw", command=self.withdraw)
        self.withdraw_button.pack()
        self.balance_button = tk.Button(self.root, text="Get Balance", command=self.get_balance)
        self.balance_button.pack()
        
        self.result_label = tk.Label(self.root)
        self.result_label.pack()
        
        self.account = None
    
    def deposit(self):
        if self.account:
            amount = int(self.amount_entry.get())
            self.account.deposit(amount)
            self.result_label.config(text=f"Deposit successful. New balance: {self.account.get_balance()}")
        else:
            self.create_account()
    
    def withdraw(self):
        if self.account:
            amount = int(self.amount_entry.get())
            if amount <= self.account.get_balance():
                self.account.withdraw(amount)
                self.result_label.config(text=f"Withdrawal successful. New balance: {self.account.get_balance()}")
            else:
                self.result_label.config(text=f"Insufficient funds. Balance: {self.account.get_balance()}")

        else:
            self.create_account()
    
    def get_balance(self):
        if self.account:
            balance = self.account.get_balance()
            self.result_label.config(text=f"Current balance: {balance}")
        else:
            self.create_account()
    
    def create_account(self):
        account_number = self.account_number_entry.get()
        balance = 0
        if account_number == "211":
            balance = 1000
        self.account = BankAccount(account_number, balance)
        self.result_label.config(text=f"Account created. Initial balance: {balance}")
        
root = tk.Tk()
bank_account_ui = BankAccountUI(root)
root.mainloop()
