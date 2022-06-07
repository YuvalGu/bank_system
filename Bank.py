from random import random

from Accounts import *
from Costumer import Costumer


class Bank:
    _instance = None

    # def __init__(self, count=0):
    #     self.costumers = {}
    #     self.accounts = {}
    #     self.count = count

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


class AccountManager:
    def __init__(self):
        self.saving_accounts = []
        self.checking_accounts = []

    def add_saving_account(self, account):
        if len(self.checking_accounts) > 0:
            self.saving_accounts.append(account)
        else:
            raise Exception(
                f"Error adding account {account.account_id}. Can't have saving account with zero checking accounts.")

    def close_saving_account(self, account_id):
        for account in self.saving_accounts:
            if account.account_id == account_id:
                balance = account.balance
                self.saving_accounts.remove(account)
                return balance

    def add_checking_account(self, account):
        self.checking_accounts.append(account)

    def close_checking_account(self, account_id):
        if len(self.checking_accounts) == 1 and len(self.saving_accounts) > 0:
            raise Exception(
                f"Error closing account {account_id}. Can't have saving accounts with zero checking accounts.")
        for account in self.checking_accounts:
            if account == account_id:
                balance = account.balance
                self.checking_accounts.remove(account)
                return balance

    def withdraw(self, account_id, amount):
        for account in (self.checking_accounts + self.saving_accounts):
            if account.account_id == account_id:
                account.withdraw(amount)
                return
        raise Exception(f"No such account with id {account_id}")

    def deposit_to_saving_account(self, checking_account_id, saving_account_id, amount):
        self.withdraw(checking_account_id, amount)
        for account in self.saving_accounts:
            if account.account_id == saving_account_id:
                account.deposit(amount)
                break

    def deposit_to_checking_account(self, checking_account_id, amount):
        for account in self.checking_accounts:
            if account.account_id == checking_account_id:
                account.deposit(amount)
                break
