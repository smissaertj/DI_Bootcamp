import sys


class BankAccount():
    def __init__(self, balance, username, password, authenticated=False):
        self.balance = balance
        self.username = username
        self.password = password
        self.authenticated = authenticated

    def show_balance(self):
        try:
            if self.authenticated:
                print(f'Current balance: {self.balance}')
            else:
                raise Exception('You need to be authenticated first!')
        except Exception as e:
            print(e)

    def deposit(self, amount):
        try:
            if self.authenticated:
                if not int(amount) or not int(amount) > 0:
                    raise Exception('Deposit amount needs to be greater than 0.')
                else:
                    self.balance += int(amount)
                    print(f'{amount} deposited. New account balance: {self.balance}')
            else:
                raise Exception('You need to be authenticated first!')
        except Exception as e:
            print(e)

    def withdraw(self, amount):
        try:
            if self.authenticated:
                if not int(amount) or not int(amount) > 0:
                    raise Exception('Withdrawal amount needs to be greater than 0.')
                else:
                    self.balance -= int(amount)
                    print(f'{amount} withdrawn. New account balance: {self.balance}')
            else:
                raise Exception('You need to be authenticated first!')
        except Exception as e:
            print(e)

    def authenticate(self, username, password):
        self.authenticated = True if username == self.username and password == self.password else False
        return self.authenticated


class MinimumBalanceAccount(BankAccount):
    def __init(self, balance, username, password, authenticated=False, minimum_balance=0):
        super().__init__(balance, username, password, authenticated=False)
        self.minimum_balance = minimum_balance

    def withdraw(self, amount):
        try:
            if self.authenticated:
                amount = int(amount)
                if (self.balance - amount) > 0:
                    super().withdraw(amount)
                else:
                    raise Exception('Amount exceeds available account balance.')
            else:
                raise Exception('You need to be authenticated first!')
        except Exception as e:
            print(e)


class ATM():
    def __init__(self, account_list, try_limit):
        self.account_list = account_list
        self.try_limit = try_limit
        self.current_tries = 0
        self.logged_in = False

        try:
            if not int(try_limit) > 0:
                raise Exception('Exceeded ATM Try Limit!')

            self.valid_accounts = []
            for account in account_list:
                if isinstance(account, BankAccount) or isinstance(account, MinimumBalanceAccount):
                    self.valid_accounts.append(account)

            if len(self.valid_accounts) == 0:
                raise Exception('No valid accounts found.')
                sys.exit(1)
            else:
                self.show_main_menu()
        except Exception as e:
            print(e)


    def show_main_menu(self):
        while not self.logged_in and self.current_tries < self.try_limit:
            print('\nWelcome! Choose an option below:')
            print('(l)ogin')
            print('(e)xit')

            menu_option = input('Select option: ')

            if menu_option == 'e':
                print('Goodbye!')
                sys.exit(0)
            elif menu_option == 'l':
                username = input('Username: ')
                password = input('Password: ')
                self.logged_in = self.login(username, password)
            else:
                print('Choose a valid menu option!')

        if self.current_tries == self.try_limit:
            print('Exceeded login attempt limit! Goodbye!')
            sys.exit(1)

    def login(self, username, password):
        for account in self.valid_accounts:
            if account.authenticate(username, password):
                print('Welcome!')
                self.show_account_menu(account)
                return True
        else:
            if not self.logged_in:
                self.current_tries += 1
                print('\nUsername / Password invalid.')
                return False

    def show_account_menu(self, account):
        menu_option = ''

        while menu_option != 'e':
            print('\nAccount Menu:')
            print('(c)heck balance')
            print('(d)eposit')
            print('(w)ithdraw')
            print('(e)xit')

            menu_option = input('Select a valid option: ')

            if menu_option == 'c':
                account.show_balance()
            if menu_option == 'd':
                amount = int(input('Deposit amount: '))
                account.deposit(amount)
            if menu_option == 'w':
                amount = int(input('Withdrawal amount: '))
                account.withdraw(amount)
            if menu_option == 'e':
                print('Goodbye!')
                sys.exit(0)


# my_account = MinimumBalanceAccount(-250, 'joeri', 'password')
# my_account.authenticate('joeri', 'password')
# #my_account.show_balance()
# #my_account.deposit(500)
# # my_account.show_balance()
# my_account.withdraw(500)
# # my_account.show_balance()

account_1 = MinimumBalanceAccount(-250, 'joeri', 'password')
account_2 = BankAccount(1000, 'joeri', 'joeri')
account_list = [account_1, 'string', account_2, 'string2']
atm = ATM(account_list, 3)

