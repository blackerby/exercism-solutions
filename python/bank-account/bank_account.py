import threading

class BankAccount:

    def __init__(self):
        self.opened = False
        self.balance = 0
        self._lock = threading.Lock()

    def get_balance(self):
        if self.opened:
            return self.balance
        else:
            raise ValueError('account is closed')

    def open(self):
        if not self.opened:
            self.opened = True
        else:
            raise ValueError('account already opened')

    def deposit(self, amount):
        if self.opened and amount > 0:
            with self._lock:
                self.balance += amount
        else:
            raise ValueError('amount must be greater than 0')

    def withdraw(self, amount):
        if self.opened and amount > 0 and amount <= self.balance:
            with self._lock:
                self.balance -= amount
        else:
            raise ValueError('invalid deposit amount')

    def close(self):
        if self.opened:
            self.opened = False
            self.balance = 0
        else:
            raise ValueError('account already closed')
