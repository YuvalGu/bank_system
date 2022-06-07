import json
import pathlib

from Bank import Bank
from Costumer import Costumer
from Accounts import *


def convert_to_bank(dict):
    count = -1
    bank = Bank()
    for data in dict.values():
        # create costumer:
        c_dict = data['costumer']
        c = Costumer(c_dict['id'], c_dict['name'], c_dict['password'])
        bank.add_costumer(c)
        # create his accounts
        accounts_dict = data['accounts']
        savings = []
        checkings = []
        for account in accounts_dict.values():
            count = max(count, account['account id'])
            if account['type'] == 'saving':
                s = SavingAccount(c_dict['id'], account['account id'], account['balance'])
                savings.append(s)
            elif account['type'] == 'private':
                p = Private(c_dict['id'], account['account id'], account['balance'])
                checkings.append(p)
            elif account['type'] == 'business':
                p = Business(c_dict['id'], account['account id'], account['balance'])
                checkings.append(p)
            else:
                p = Premium(c_dict['id'], account['account id'], account['balance'])
                checkings.append(p)
        bank.accounts[c_dict['id']].checking_accounts = checkings
        bank.accounts[c_dict['id']].saving_accounts = savings
    bank.count = count + 1
    return bank


def convert_to_dict(bank):
    dict = {}
    for index, (c_id, c) in enumerate(bank.costumers.items()):
        accounts = bank.get_all_accounts(c_id)
        accounts_dict = {}
        for i, account in enumerate(accounts):
            accounts_dict[i] = account.as_dict()
        dict[index] = {'costumer': c.__dict__, 'accounts': accounts_dict}
    return dict


class BankDB:
    def __init__(self, path):
        self.path = path
        if not pathlib.Path(self.path).exists():
            self.write(Bank())

    def read(self):
        with open(self.path, "r") as file:
            try:
                data = json.loads(file.read())
                return data
            except Exception:
                return {}

    def create_bank(self):
        data = self.read()
        return convert_to_bank(data)

    def write(self, bank):
        j_object = convert_to_dict(bank)
        with open(self.path, "w") as file:
            json.dump(j_object, file, indent=4)
