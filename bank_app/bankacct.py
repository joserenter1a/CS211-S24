"""
Bank Account Class

- Encapsulates the data and methods related to a bank acct.
- This class has two private attributes, account_number and balance
    these are hidden from the user and can only be accessed through the public
    methods of the class. i.e. deposit(), withdraw(), and get_balance()
     HINT: Specify private members with __ before the variable names.

    self.__private_member
"""


class BankAccount:
    def __init__(self, account_number, balance):
        """
        Class constructor
        initializes the private attributes with values passed as arguments
        Should have an account number and balance
        """
        # TODO

 
    def set_balance(self, set_new):
        """
        Sets a new balance, allows for hiding of private member
        """

    def get_balance(self):
        """
        returns the current balance in the account
        """
        # TODO

    def deposit(self, amount):
        """
        Adds the specified amount to the account balance
        """
        # TODO

    def withdraw(self, amount):
        """
        Subtracts the specified amount from the balance, given that there 
        are sufficient funds available
        """
        # TODO
