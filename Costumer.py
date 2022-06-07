class Costumer:
    def __init__(self, id: str, name: str, pin_code: str):
        self.id = id
        self.name = name
        self.password = pin_code
        # self.accounts_id = []

    # def add_account(self, account_id):
    #     self.accounts_id.append(account_id)
    #
    # def close_account(self, account_id):
    #     self.accounts_id.remove(account_id)

    def __eq__(self, other):
        return self.id == other.id


