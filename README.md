# simple-atm-controller

To clone the repository: git clone https://github.com/mouadlasri/simple-atm-controller

Python 3.10 or higher

### Code Details

Controller.py has three main sections:

- Bank Class

  - Holds bank accounts
  - Can add new accounts (saving or checking, or both) with their balances when created

- Account Class

  - Can be used to create independent accounts (in the future, use Account to populate Bank objects)

- Controller Class

  -- All interaction with the bank account are done through Controller actions

  - Check if card is inserted or not, and PIN verification
  - Can check balance, deposit or withdraw from specific account of account number (checking or saving)
  - Type account can either be "checking" or "savings"
  - Creating an account command: `controller.create_account(account_number, pin, balance, type_account)`
  - Inserting card command: `controller.insert_card(account_number, pin)`
  - Controller action pattern: `controller.account_actions(account_number, pin, type_account, amount)`
  - Different actions:
    - Deposit Action: `controller.account_actions(account_number, pin, type_account, "Deposit", amount)`
    - Withdraw Action: `controller.account_actions(account_number, pin, type_account, "Withdraw", amount)`

- Main

  - Has testing of the controller
  - More tests can be added following the right command formats writte as comments
  - Running the program from the command-line will run the test cases.

### Program execution

Run: `python atmcontroller.py` in the command line
