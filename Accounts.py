class Account:
    def __init__(self, costumer_id: str, account_id: int, balance: int):
        self.account_id = account_id
        self.costumer_id = costumer_id
        self.balance = balance

    def withdraw(self, amount):
        """
        :param amount: the amount of money the costumer wants to withdraw
        :return: raise exception if amount > balance
        """
        if self.balance >= amount:
            self.balance = self.balance - amount
            return amount
        raise Exception('Your Balance is not enough')

    def deposit(self, amount):
        """
        add the amount to the balance
        :param amount: the amount of money the costumer wants to deposit
        """
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
        """
        every num of actions we take commission from the current balance
        :return:  interest from the balance or 0 if not num_action % round
        """
        if self.num_action % self.round == 0:
            return self.balance * self.interest
        return 0

    def withdraw(self, amount):
        """
        counts the num of actions, and call super.withdraw with the right commission
        :param amount: the amount of money the costumer wants to withdraw
        """
        self.num_action += 1
        commission = self.get_commission()
        amount += commission
        super().withdraw(amount)

    def deposit(self, amount):
        """
        counts the num of actions, and call super.deposit with the right commission
        :param amount: the amount of money the costumer wants to deposit
        """
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
