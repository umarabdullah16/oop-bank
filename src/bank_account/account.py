"""
Docstring
"""


class BankAccount:
    """Represents a simple bank account"""

    def __init__(self, owner: str, balance: float = 0.0):
        """
        Docstring for __init__

        :param self: Description
        :param owner: Description
        :type owner: str
        :param balance: Description
        :type balance: float
        """
        self.owner = owner
        self.balance = balance

    def deposit(self, amount: float) -> None:
        """
        Docstring for deposit

        :param self: Description
        :param amount: Description
        :type amount: float
        """
        if amount <= 0:
            raise ValueError("Deposit amount must be positive")
        self.balance += amount

    def withdraw(self, amount: float) -> None:
        """
        Docstring for withdraw

        :param self: Description
        :param amount: Description
        :type amount: float
        """
        if amount <= 0:
            raise ValueError("Withdrawal amount must be positive")
        if amount > self.balance:
            raise ValueError("Insufficient balance")
        self.balance -= amount

    def get_balance(self) -> float:
        """
        Docstring for get_balance

        :param self: Description
        :return: Description
        :rtype: float
        """
        return self.balance
