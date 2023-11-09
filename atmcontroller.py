

class Bank:
    def __init__(self):
        self.accounts = {}

    def add_account(self, account):
        # check if account already exists
        if account.account_number in self.accounts:
            raise ValueError("Account already exists")
        else:
            self.accounts[account.account_number] = account

    def verify_pin(self, account_number, pin):
        # check if account exists
        if account_number not in self.accounts:
            raise ValueError("Account does not exist")
        else:
            # check if pin is correct
            if self.accounts[account_number].pin == pin:
                return True
            else:
                return False
        
    def get_balance(self, account_number):
        # check if account exists
        if account_number not in self.accounts:
            raise ValueError("Account does not exist")
        else:
            return self.accounts[account_number].balance

class Account:
        def __init__(self, account_number, pin, balance):
            self.account_number = account_number
            self.pin = pin
            self.balance = balance
    
        def deposit(self, amount):
            self.balance += amount
    
        def withdraw(self, amount):
            # check if withdrawing is valid
            if self.balance - amount < 0:
                return False
                # raise ValueError("Insufficient funds")
            else:
                self.balance -= amount
                return True
            


class Controller:
        def __init__(self, bank):
            self.bank = bank

        def insert_card(self, account_number, pin):
            # check if pin is correct
            if self.bank.verify_pin(account_number, pin):
                return 'Valid pin' # valid pin
            else:
                return False # invalid pin

        def get_account(self, account_number):
            return self.bank.accounts[account_number]
    
        def create_account(self, account_number, pin, balance):
            account = Account(account_number, pin, balance)
            self.bank.add_account(account)
            return account
    
        def deposit(self, account_number, amount):
            self.get_account(account_number).deposit(amount)
    
        def withdraw(self, account_number, amount):
            self.get_account(account_number).withdraw(amount)


        # Only interact with the controller through actions
        # Actions call the functions (to separate business logic)
        def account_actions(self, account_number, pin, action, amount=0):
            # check if card is inserted and pin is valid before doing any actions
            if self.insert_card(account_number, pin) == 'Valid pin':
                if action == "See Balance":
                    return self.bank.get_balance(account_number)
            
                elif action == "Deposit":
                    # add new balance to account
                    self.deposit(account_number, amount)
                    # update balance
                    return self.bank.get_balance(account_number)
                
                elif action == "Withdraw":
                    # subtract new balance from account
                    self.withdraw(account_number, amount)
                    # update balance
                    return self.bank.get_balance(account_number)

            else:
                # return False and a message
                return False, "Insert card first"
                
           
                

           

            




    

if __name__ == "__main__":

    # test the controller
    bank = Bank()
    controller = Controller(bank)
    controller.create_account(123456, 1234, 100) # account_number, pin, balance

    # for each action, we verify if the card is inserted and pin is valid for extra security

    # swipe card first before being allowed to do any actions

    ###
    # INSERT CARD
    ###
    # Command Pattern: controller.insert_card(account_number, pin)

    controller.insert_card(123456, 1234)

    print(f"Pin {1234}:", controller.insert_card(123456, 1234))
    print("Account balance: ", controller.account_actions(123456, 1234, "See Balance", 0))
   
    ###
    # DEPOSIT
    ###
    # Command Pattern: controller.account_actions(account_number, pin, "Deposit", amount)
    controller.deposit(123456, 100)
    print("Depositing 100 - New Balance: ", controller.account_actions(123456, 1234, "See Balance"))
    controller.deposit(123456, 200)
    print("Depositing 200 - New Balance: ", controller.account_actions(123456, 1234, "See Balance"))

    print(controller.account_actions(123456, 1234, "See Balance"))

    ###
    # WITHDRAW
    ### 
    # Command Pattern: controller.account_actions(account_number, pin, "Withdraw", amount)
    
    print('Withdrawing 300..')
    if(controller.account_actions(123456, 1234, "Withdraw", 300)):
        print("Withdrawal Successful - New Balance: ", controller.account_actions(123456, 1234, "See Balance"))
    else:
        print(f"Insufficient funds ({controller.account_actions(123456, 1234, 'See Balance')})")
   


# Path: simple-atm-controller/test_atmcontroller.py