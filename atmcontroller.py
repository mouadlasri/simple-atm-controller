class Bank:
    def __init__(self):
        self.accounts = {}

    # add account to bank (can be checking or savings)
    # each account number can have two account types (checking and savings)
    def add_account(self, account_number, pin, type_account, balance):
            # check if account already exists, and type account is valid and already exists or not
            if account_number in self.accounts:
                self.accounts[account_number]['account'][type_account] = balance
                print(self.accounts)
                # raise ValueError("Account already exists")
                # return False
            elif type_account not in ["checking", "savings"]:
                # raise ValueError("Invalid account type")
                return False
            else:
                self.accounts[account_number] = {"pin" : pin, "account": {type_account: balance}}
                print(self.accounts)
                return True

    def verify_pin(self, account_number, pin):
        # check if account exists
        if account_number not in self.accounts:
            raise ValueError("Account does not exist")
        else:
            # check if pin is correct
            if self.accounts[account_number]['pin'] == pin:
                return True
            else:
                return False
        
        
class Account:
    # an account can be checking or savings under the same account number
    def __init__(self, account_number, pin, balance, type_account):
        self.account_number = account_number
        self.pin = pin
        self.balance = balance
        self.type_account = type_account

    # deposit to right account type under account number
    def deposit(self, amount, type_account):
        # deposit to correct account type of account number
        if self.type_account == type_account:
            self.balance += amount
        else:
            return False
        
    # withdraw from right account type under account number
    def withdraw(self, amount, type_account):
        # withdraw from correct account type of account number
        if self.type_account == type_account:
            # check if withdrawing is valid
            if self.balance - amount < 0:
                return False
                # raise ValueError("Insufficient funds")
            else:
                self.balance -= amount
                return True
        else:
            return False

    # get balance of right account type under account number
    def get_balance(self, type_account): 
        # check if type account of account number exists first before getting balance
        if self.type_account == type_account:
            return self.balance
        else:
            return 'Specific account doesnt exist'
 
class Controller:
        def __init__(self, bank):
            self.bank = bank

        def insert_card(self, account_number, pin):
            # check if account exists
            if account_number not in self.bank.accounts:
                return 'Account does not exist'
            else:
                # check if pin is correct
                if self.bank.verify_pin(account_number, pin):
                    return 'Valid pin'
                else:
                    return False
                
        # create account of specific number and type
        def create_account(self, account_number, pin, balance, type_account):
            # account = Account(account_number, pin, balance, type_account)
            if(self.bank.add_account(account_number, pin, type_account, balance)):
                print('Account created')
           
        
        # get account of specific number and type
        def get_account(self, account_number, type_account):
            return self.bank.accounts[account_number][type_account]

        # get account balance of specific account type of specific account number
        def get_balance(self, account_number, type_account):
            # check if account exists and if account exists, check if type account exists
            if account_number not in self.bank.accounts:
                return 'Account does not exist'
            elif type_account not in self.bank.accounts[account_number]['account']:
                return f'{type_account} account of accound number {account_number} doesnt exist yet'
            else:
                return self.bank.accounts[account_number]['account'][type_account]
            
    
        # deposit to specific account number of specific account type
        def deposit(self, account_number, type_account, amount):
            # check if account exists and if account exists, check if type account exists
            if account_number not in self.bank.accounts:
                message = 'account does not exist'
                return 'Account does not exist'
            elif type_account not in self.bank.accounts[account_number]['account']:
                message = f'{type_account} account of accound number {account_number} doesnt exist yet'
                # return f'{type_account} account of accound number {account_number} doesnt exist yet'
            else:
                self.bank.accounts[account_number]['account'][type_account] += amount
                message = f'{amount} deposited to {type_account} account of account number {account_number}'
                # return True
            return message
           
        def withdraw(self, account_number, type_account, amount):
            # check if account exists and if account exists, check if type account exists
            if account_number not in self.bank.accounts:
                return 'Account does not exist'
            elif type_account not in self.bank.accounts[account_number]['account']:
                return f'{type_account} account of accound number {account_number} doesnt exist yet'
            else:
                # check if withdrawing is valid
                if self.bank.accounts[account_number]['account'][type_account] - amount < 0:
                    return False
                    # raise ValueError("Insufficient funds")
                else:
                    self.bank.accounts[account_number]['account'][type_account] -= amount
                    return True


        # actions to do with account and specific account type
        def account_actions(self, account_number, pin, type_account, action, amount=0):
            # check if card is inserted and pin is valid before doing any actions
            if self.insert_card(account_number, pin) == 'Valid pin':
                if action == "See Balance":
                    return self.get_balance(account_number, type_account)
            
                elif action == "Deposit":
                    # add new balance to account
                    return self.deposit(account_number, type_account, amount)
                
                elif action == "Withdraw":
                    # subtract new balance from account
                    return self.withdraw(account_number, type_account, amount)

            else:
                # return False and a message
                return False, "Insert card first"

           
if __name__ == "__main__":

    # For each action after creating an account and inserting the card,
    # we verify if the card is inserted and pin is valid for extra verification and security

    # test the controller

    ###
    # CREATE ACCOUNT WITH BANK AND SPECIFIC ACCOUNT TYPE (Checking or Savings)
    ###
    # Command Pattern: controller.create_account(account_number, pin, balance, type_account)
    bank = Bank()
    test_controller = Controller(bank)
    test_controller.create_account(123456, 1234, 200, "checking")
    test_controller.create_account(123456, 1234, 200, "savings")


    # test_controller.account_actions(123456, 1234, "checking", "Deposit", 100)

    ###
    # INSERT CARD
    ###
    # Command Pattern: controller.insert_card(account_number, pin)
    print(f"Pin {1234}:", test_controller.insert_card(123456, 1234))
    # print balance of both accounts types if they exist
    print("Checking Balance: ", test_controller.account_actions(123456, 1234, "checking", "See Balance"))
    print("Savings Balance: ", test_controller.account_actions(123456, 1234, "savings", "See Balance")) # should throw an error since saving account under the account numbre doesn't exist yet

    # print new line
    print()

    ###
    # DEPOSIT
    ###
    # Command Pattern: controller.account_actions(account_number, pin, "Deposit", amount)
    print("Depositing 100..")
    print(test_controller.account_actions(123456, 1234, "checking", "Deposit", 100))
    print("Checking Balance: ", test_controller.account_actions(123456, 1234, "checking", "See Balance"))

    test_controller.deposit(123456, "savings", 200)
    print(test_controller.account_actions(123456, 1234, "Savings", "See Balance"))

    # print(controller.account_actions(123456, 1234, "See Balance"))
    # print new line
    print()
    ###
    # WITHDRAW
    ### 
    # Command Pattern: controller.account_actions(account_number, pin, "Withdraw", amount)
    print('Withdrawing 200 from checking account') # valid operation since balance is 300
    status = test_controller.account_actions(123456, 1234, "checking", "Withdraw", 200)
    print('Money withdrawn successfully') if status == True else print('Insufficient funds')
    print("Checking Balance: ", test_controller.account_actions(123456, 1234, "checking", "See Balance"))


    # print new line
    print()
    
    #withdraw 500 from checking account
    print('Withdrawing 500 from checking account') # invalid operation since balance is 100
    status = test_controller.account_actions(123456, 1234, "checking", "Withdraw", 500)
    print('Money withdrawn successfully') if status == True else print('Insufficient funds')
    print("Checking Balance: ", test_controller.account_actions(123456, 1234, "checking", "See Balance")) # should be 100 (no change)


    # Second bank test
    print()


