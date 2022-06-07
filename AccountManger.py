class AccountManager:
    def __init__(self):
        self.saving_accounts = []
        self.checking_accounts = []

    def add_saving_account(self, account):
        """
        if there are no checking accounts raise exception, ow - add saving account
        :param account: the saving account that needs to be added
        """
        if len(self.checking_accounts) > 0:
            self.saving_accounts.append(account)
        else:
            raise Exception(
                f"Error adding account {account.account_id}. Can't have saving account with zero checking accounts.")

    def close_saving_account(self, account_id):
        """
        search the saving account by id remove it from the list and return the balance
        :param account_id: the account id that needs to be removed
        :return: the removed account balance
        """
        for account in self.saving_accounts:
            if account.account_id == account_id:
                balance = account.balance
                self.saving_accounts.remove(account)
                return balance

    def add_checking_account(self, account):
        """
        :param account: the saving account that need to be added
        """
        self.checking_accounts.append(account)

    def close_checking_account(self, account_id):
        """
        if its the only checking account and there are saving account - raise exception
        o.w - search the checking account by id remove it from the list and return the balance
        :param account_id: the account id that needs to be removed
        :return: the removed account balance
        """
        if len(self.checking_accounts) == 1 and len(self.saving_accounts) > 0:
            raise Exception(
                f"Error closing account {account_id}. Can't have saving accounts with zero checking accounts.")
        for account in self.checking_accounts:
            if account == account_id:
                balance = account.balance
                self.checking_accounts.remove(account)
                return balance

    def withdraw(self, account_id, amount):
        """
        search the account by id from all account and withdraw
        :param account_id: the id account
        :param amount: amount of money we want to withdraw
        :return: raise exception if the account doesn't exist
        """
        for account in (self.checking_accounts + self.saving_accounts):
            if account.account_id == account_id:
                account.withdraw(amount)
                return
        raise Exception(f"No such account with id {account_id}")

    def deposit_to_saving_account(self, checking_account_id, saving_account_id, amount):
        """
        withdraw the money from checking account - if succeed  deposit it to the saving account
        :param checking_account_id: the checking account we deposit from
        :param saving_account_id: the saving account we deposit to
        :param amount: amount of money we want to deposit
        """
        self.withdraw(checking_account_id, amount)
        for account in self.saving_accounts:
            if account.account_id == saving_account_id:
                account.deposit(amount)
                break

    def deposit_to_checking_account(self, checking_account_id, amount):
        """
        search the checking account by id and deposit the money to the checking account
        :param checking_account_id: the checking account we deposit to
        :param amount: amount of money we want to deposit
        """
        for account in self.checking_accounts:
            if account.account_id == checking_account_id:
                account.deposit(amount)
                break
