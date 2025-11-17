#Version 1.0 
#Missing log out,  log in to check account and creating a user account
#Extra stuff - storing accounts created so that I can keep making accounts
#And logging back into them. Version 1.5+

import sys
class Atm:
    """Class representing ATM functions and bank transactions"""
    def __init__(self):
        self.user = "Vee"
        self.pin = 1234
        self.balance = 10000
        self.deposit = 2000
        self.withdraw = 100
        self.card_inserted = True
        self.logout = False

    def __str__(self): #interface screen
        return(
            "Transaction Receipt:\n"
            f"Account User: {self.user}\n"
            f"Balance: $ {self.balance}"
        )

    def is_card_inserted(self,atm_answer):
        """definition to check if atm card is inserted
           return True or False
        """
        if atm_answer == "y":
            return True
        else:

            return False
    
    def auth_pin(self, pin):
        """definition to validate pin entered against pin stored for user"""
        if pin == self.pin:
            return True
        else: 
            return False

    def bank_options(self, option):
        """definition to handle user option from bank interace"""
        if option not in ('1', '2','3','x'):
            print("Invalid option.")
            option = input("Select an option: ")

        if option == '1':
            self.check_balance()
        if option == '2':
            self.withdraw_money()
        if option == '3':
            self.deposit_money()
        if option == 'x':
            self.account_logout()

    def check_balance(self):
        """definition to check balance"""
        print(f"Current Balance: ${self.balance}\n")
        self.user_interface()

    def withdraw_money(self):
        """definition to withdraw money and return new balance"""
        withdrawal_amount = int(input("Enter witdrawal amount (USD): "))
        if withdrawal_amount > self.balance:
            print("Sorry, we cannot process the withdrawal.\n")
            print(f"Current Balance: {self.balance}\n")
            self.user_interface()
            
        else:
            print(f"Processing withdrawal of ${withdrawal_amount}...")
            print("Completed.")
            new_balance = self.balance - withdrawal_amount
            self.balance = new_balance
            print(f"Current Balance : ${self.balance}\n")
            self.user_interface()
        
    def deposit_money(self):
        """defintion to handle deposits of money and return new balance"""
        deposit_amount = int(input("Enter deposit amount: $ "))
        new_balance = self.balance + deposit_amount
        self.balance = new_balance
        print(f"Your new balance is: ${self.balance}\n")
        self.user_interface()

    def user_interface(self):
        """definition of user interface the mani definition for user interaction"""
        print(""" 
              1 - Check Balance\n
              2 - Make a Withdrawal\n
              3 - Deposit Money\n
              X - Exit\n 
              """)
        option = input("Select an option: ")
        self.bank_options(option)
    
    def account_logout(self):
        """defintion to handle account log out"""
        return f"Exiting account...\n \n{str(self)}"


vees_atm = Atm()
print(" === Welcome to Bank of Vee ===\n")
AUTH_PIN = False

debit_card_check = input("Did you insert debit card? (Y/N): ")

CHECK_CARD = vees_atm.is_card_inserted(debit_card_check)
if CHECK_CARD is True:
    bank_pin = int(input("Enter pin: "))
    AUTH_PIN = vees_atm.auth_pin(bank_pin)
else:
    print("Sorry, you need to insert a debit card for ATM transacitons. Good Bye.")
    sys.exit(0)

if AUTH_PIN is True: 
    print(f"Welcome to Bank of Vee, {vees_atm.user}!\n")
    vees_atm.user_interface()
else:
    print("Sorry, this pin is not recognized. Have a Nice Day!")
    sys.exit(0)
print(vees_atm.account_logout())





