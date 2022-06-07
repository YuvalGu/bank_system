from Bank import *


def checking_account_query():
    """
    ask the type costumer and the monthly deposit
    :return: account type
    """
    print("Please answer")
    print("Are you:")
    ans = input("1. Private costumer\n2. Business costumer\n").strip()
    if ans == '1':
        return 'private'
    elif ans == '2':
        ans = input("Please enter your monthly deposit: ").strip()
        if not ans.isdigit():
            raise ValueError(f"{ans} is not a non-negative number.")
        ans = int(ans)
        if ans <= 25000:
            return 'private'
        elif 25000 < ans <= 100000:
            return 'business'
        elif ans > 100000:
            return 'premium'
    else:
        raise ValueError(f"{ans} is a bad input. the options are 1 or 2.")


def print_accounts_details(accounts):
    """
    :param accounts: list of accounts
    """
    if len(accounts) == 0:
        print("There are no accounts")
    else:
        for count, account in enumerate(accounts, 1):
            print(f"{count}) {account}")


def choose_account_id(accounts, operation):
    print_accounts_details(accounts)
    if len(accounts) == 0:
        return None
    elif len(accounts) == 1:
        account_id = accounts[0].account_id
        ans = input(f"Would you like to {operation} account {account_id}? Y/N: ")
        if ans.lower() == 'y':
            return account_id
        elif ans.lower() == 'n':
            return None
        else:
            raise Exception(f"{ans} is a bad input. The options are Y or N.")
    else:
        index = int(input(f"Please choose a number between 1 to {len(accounts)}\n")) - 1
        if 0 <= index < len(accounts):
            return accounts[index].account_id
        else:
            raise Exception(f"{index+1} is a bad input.")


class CRM:
    def __init__(self, bank: Bank):
        self.bank = bank
        self.costumer = None

    def start(self):
        """
        Starts the conversation with the user.
        The users option: sign up, login and exit.
        If the user insert a wrong input - start function is running again.
        """
        print("Welcome to our bank")
        print("Please choose one of the following options:")
        user_ans = input("1) Sign Up\n2) Login\n3) Exit\n")
        # Remove spaces at the beginning and at the end of the string
        user_ans = user_ans.strip()
        if user_ans == '1':
            self.register()
        elif user_ans == '2':
            self.login()
        elif user_ans == '3':
            print("Bye!")
            return
        else:
            # If the input is not 1, 2 or 3
            print("Wrong Input! Please try again")
            self.start()

    def register(self):
        """
        get username, id and password.
        if costumer exists - send to start() for login or for sign up with different id
        o.w - add new costumer to the bank
        """
        user_name = input("Enter your username: ").strip()
        user_id = input("Enter your id: ").strip()
        # Check if costumer already exist
        if self.bank.costumer_exist(user_id):
            print("Costumer already exists. Please login or sign up with different id")
            self.start()
        else:
            password = input("Choose your password: ").strip()
            # Create costumer
            self.costumer = Costumer(user_id, user_name, password)
            # add it to the bank
            self.bank.add_costumer(self.costumer)
            self.costumer_menu()

    def login(self):
        """
        get id and password
        if costumer exists - go to costumer menu
        o.w - go back to start
        """
        id = input("Enter your id: ").strip()
        password = input("Enter your password: ").strip()
        self.costumer = self.bank.get_costumer_by_id(id)
        if self.costumer is None:
            print("The id or password is incorrect! Please try again")
            self.start()
        else:
            if self.costumer.password == password:
                self.costumer_menu()
            else:
                print("username or password is incorrect! Please try again")
                self.start()

    def costumer_menu(self):
        """
        menu of all costumer options
        """
        while True:
            print(f"\nHello {self.costumer.name}, please choose one of the following options:")
            print("1) Add checking account")
            print("2) Add saving account")
            print("3) Get my accounts details")
            print("4) Delete account")
            print("5) Withdraw")
            print("6) Deposit")
            print("7) Exit")
            ans = input().strip()
            if ans == '1':
                self.add_checking_account()
            elif ans == '2':
                self.add_saving_account()
            elif ans == '3':
                accounts = self.bank.get_all_accounts(self.costumer.id)
                print_accounts_details(accounts)
            elif ans == '4':
                self.close_account()
            elif ans == '5':
                self.withdraw()
            # Accounts.withdraw()
            elif ans == '6':
                self.deposit()
            # Accounts.deposit()
            elif ans == '7':
                print("Thank you and goodbye!")
                break
            else:
                print("Wrong Input! Please try again")

    def add_checking_account(self):
        """
        check the account type, and call the right function
        if the costumer insert bad input in account query - prints the error message
        """
        try:
            account_type = checking_account_query()
            if account_type == 'private':
                self.add_private_account()
            elif account_type == 'business':
                self.add_business_account()
            else:
                self.add_premium_account()
        except ValueError as e:
            print(e)

    def add_private_account(self):
        """
        tells the costumer the account details (interest of x actions)
        if costumer is interesting - call the bank to create private account
        if costumer not interesting or insert bad input - return without calling the bank
        """
        ans = input(
            "You are eligible for a private account with 5% interest every 5 actions.\nInterested? Y/N ").strip()
        if ans.lower() == 'y':
            self.bank.add_private_account(self.costumer.id)
            print("A private account has been created")
        elif ans.lower() == 'n':
            return
        else:
            print(f"{ans} is a bad input. the options are Y or N.")

    def add_business_account(self):
        """
        tells the costumer the account details (interest of x actions)
        if costumer is interesting - call the bank to create business account
        if costumer not interesting or insert bad input - return without calling the bank
        """
        ans = input(
            "You are eligible for a business account with 5% interest every 10 actions.\nInterested? Y/N ").strip()
        if ans.lower() == 'y':
            self.bank.add_business_account(self.costumer.id)
            print("A business account has been created")
        elif ans.lower() == 'n':
            return
        else:
            print(f"{ans} is a bad input. the options are Y or N.")

    def add_premium_account(self):
        """
        tells the costumer the account details (interest of x actions)
        if costumer is interesting - call the bank to create premium account
        if costumer not interesting or insert bad input - return without calling the bank
        """
        ans = input(
            "You are eligible for a premium account with 2.5% interest every 10 actions.\nInterested? Y/N ").strip()
        if ans.lower() == 'y':
            self.bank.add_premium_account(self.costumer.id)
            print("A business account has been created")
        elif ans.lower() == 'n':
            return
        else:
            print(f"{ans} is a bad input. the options are Y or N.")

    def add_saving_account(self):
        """
        check if there checking account, if not - not possible to create saving account
        if there is at least one checking account - call the bank to add saving account
        """
        checking_accounts = self.bank.get_all_checking_accounts(self.costumer.id)
        if len(checking_accounts) == 0:
            print("There are no checking account, please add checking account first")
        else:
            self.bank.add_saving_account(self.costumer.id)
            print("A saving account has been created")

    def close_account(self):
        """
        ask the type of account the costumer wants to close
        """
        print("Would you like to close:")
        ans = input("1) Checking account\n2) Saving account\n")
        if ans == '1':
            self.close_checking_account()
        elif ans == '2':
            self.close_saving_account()
        else:
            print("Wrong Input! The options are 1 or 2")

    def close_checking_account(self):
        """
        close the chosen checking account and print the balance
        if costumer inserts wrong input - print the error message
        """
        try:
            accounts = self.bank.get_all_checking_accounts(self.costumer.id)
            account_id = choose_account_id(accounts, "close")
            if account_id is not None:
                balance = self.bank.close_checking_account(self.costumer.id, account_id)
                print(f"Account {account_id} has been successfully closed, your balance is: {balance}")
        except Exception as e:
            print(e)

    def close_saving_account(self):
        """
        close the chosen saving account and print the balance
        if costumer inserts wrong input - print the error message
        """
        try:
            accounts = self.bank.get_all_saving_accounts(self.costumer.id)
            account_id = choose_account_id(accounts, "close")
            if account_id is not None:
                balance = self.bank.close_saving_account(self.costumer.id, account_id)
                print(f"Account {account_id} has been successfully closed, your balance is: {balance}")
        except Exception as e:
            print(e)

    def withdraw(self):
        """
        withdraw from the chosen account
        if not possible or costumer inserts wrong input print message error
        """
        try:
            accounts = self.bank.get_all_checking_accounts(self.costumer.id)
            account_id = choose_account_id(accounts, "withdraw from")
            if account_id is not None:
                amount = input("Input the amount of money you want to withdraw: ")
                if amount.isdigit():
                    self.bank.withdraw(self.costumer.id, account_id, int(amount))
                else:
                    print(f"{amount} is not a non-negative number.")
        except Exception as e:
            print(e)

    def deposit(self):
        """
        ask the type of account the costumer wants to deposit
        """
        print("Would you like to deposit to:")
        ans = input("1) Checking account\n2) Saving account\n")
        if ans == '1':
            self.deposit_checking_account()
        elif ans == '2':
            self.deposit_saving_account()
        else:
            print("Wrong Input! The options are 1 or 2")

    def deposit_checking_account(self):
        """
        deposit the chosen checking account and print the balance
        if costumer inserts wrong input - print the error message
        """
        try:
            accounts = self.bank.get_all_checking_accounts(self.costumer.id)
            account_id = choose_account_id(accounts, "deposit to")
            if account_id is not None:
                amount = input("Input the amount of money you want to deposit: ")
                if amount.isdigit():
                    self.bank.deposit_to_checking_account(self.costumer.id, account_id, int(amount))
                else:
                    print(f"{amount} is not a non-negative number.")
        except Exception as e:
            print(e)

    def deposit_saving_account(self):
        try:
            print("Deposit from:")
            checking_accounts = self.bank.get_all_checking_accounts(self.costumer.id)
            from_account_id = choose_account_id(checking_accounts, "deposit from")
            if from_account_id is None:
                return
            print("Deposit To:")
            saving_accounts = self.bank.get_all_saving_accounts(self.costumer.id)
            to_account_id = choose_account_id(saving_accounts, "deposit to")
            if to_account_id:
                amount = input("Input the amount of money you want to deposit: ")
                if amount.isdigit():
                    self.bank.deposit_to_saving_account(self.costumer.id, from_account_id, to_account_id, int(amount))
                else:
                    print(f"{amount} is not a non-negative number.")
        except Exception as e:
            print(e)
