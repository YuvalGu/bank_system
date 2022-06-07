class Account:
    def __init__(self, costumer_id: str, account_id: int, balance: int):
        self.account_id = account_id
        self.costumer_id = costumer_id
        self.balance = balance

    def get_balance(self):
        return self.balance

    def withdraw(self, amount):
        if self.balance >= amount:
            self.balance = self.balance - amount
            return amount
        raise Exception('Your Balance is not enough')

    def deposit(self, amount):
        self.balance = self.balance + amount

    def __str__(self):
        return f"id: {self.account_id}, current balance: {self.balance}"

    def __eq__(self, id):
        return self.account_id == id


class CheckingAccount(Account):
    def __init__(self, costumer_id: str, account_id: int, balance: int, round: int, interest: float):
        super().__init__(costumer_id, account_id, balance)
        self.num_action = 0
        self.round = round
        self.interest = interest
        self.saving = []

    def get_commission(self):
        if self.num_action % self.round == 0:
            return self.balance * self.interest
        return 0

    def withdraw(self, amount):
        self.num_action += 1
        commission = self.get_commission()
        amount += commission
        super().withdraw(amount)

    def deposit(self, amount):
        self.num_action += 1
        commission = self.get_commission()
        amount -= commission
        super().deposit(amount)


class Private(CheckingAccount):
    def __init__(self, costumer_id: str, account_id: int, balance=0):
        super().__init__(costumer_id, account_id, balance, 5, 0.05)

    def as_dict(self):
        return {'type': 'private', 'account id': self.account_id, 'balance': self.balance}

    def __str__(self):
        return "type: private, " + super().__str__()


class Business(CheckingAccount):
    def __init__(self, costumer_id: str, account_id: int, balance=0):
        super().__init__(costumer_id, account_id, balance, 10, 0.05)

    def as_dict(self):
        return {'type': 'business', 'account id': self.account_id, 'balance': self.balance}

    def __str__(self):
        return "type: business, " + super().__str__()


class Premium(CheckingAccount):
    def __init__(self, costumer_id: str, account_id: int, balance=0):
        super().__init__(costumer_id, account_id, balance, 10, 0.025)

    def as_dict(self):
        return {'type': 'premium', 'account id': self.account_id, 'balance': self.balance}

    def __str__(self):
        return "type: premium, " + super().__str__()


class SavingAccount(Account):
    def __init__(self, costumer_id: str, account_id: int, balance=0):
        super().__init__(costumer_id, account_id, balance)

    def as_dict(self):
        return {'type': 'saving', 'account id': self.account_id, 'balance': self.balance}

    def __str__(self):
        return "type: saving, " + super().__str__()
