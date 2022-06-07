from AccountManger import AccountManager
from Accounts import *
from Costumer import Costumer


class Bank:
    _instance = None

    def __new__(self, count=0):
        if not self._instance:
            self._instance = super(Bank, self).__new__(self)
            self.costumers = {}
            self.accounts = {}
            self.count = count
        return self._instance

    def get_costumer_by_id(self, costumer_id):
        if self.costumer_exist(costumer_id):
            return self.costumers[costumer_id]
        return None

    def costumer_exist(self, costumer_id):
        return costumer_id in self.costumers

    def add_costumer(self, costumer: Costumer):
        self.costumers[costumer.id] = costumer
        self.accounts[costumer.id] = AccountManager()

    def add_private_account(self, costumer_id):
        account = Private(costumer_id, self.count)
        self.accounts[costumer_id].add_checking_account(account)
        self.count += 1

    def add_business_account(self, costumer_id):
        account = Business(costumer_id, self.count)
        self.accounts[costumer_id].add_checking_account(account)
        self.count += 1

    def add_premium_account(self, costumer_id):
        account = Premium(costumer_id, self.count)
        self.accounts[costumer_id].add_checking_account(account)
        self.count += 1

    def add_saving_account(self, costumer_id):
        account = SavingAccount(costumer_id, self.count)
        self.accounts[costumer_id].add_saving_account(account)
        self.count += 1

    def get_all_checking_accounts(self, costumer_id):
        return self.accounts[costumer_id].checking_accounts

    def get_all_saving_accounts(self, costumer_id):
        return self.accounts[costumer_id].saving_accounts

    def get_all_accounts(self, c_id):
        return self.get_all_checking_accounts(c_id) + self.get_all_saving_accounts(c_id)

    def close_saving_account(self, c_id, account_id):
        return self.accounts[c_id].close_saving_account(account_id)

    def close_checking_account(self, c_id, account_id):
        return self.accounts[c_id].close_checking_account(account_id)

    def withdraw(self, c_id, account_id, amount):
        self.accounts[c_id].withdraw(account_id, amount)

    def deposit_to_checking_account(self, c_id, account_id, amount):
        self.accounts[c_id].deposit_to_checking_account(account_id, amount)

    def deposit_to_saving_account(self, c_id, from_account_id, to_account_id, amount):
        self.accounts[c_id].deposit_to_saving_account(from_account_id, to_account_id, amount)
