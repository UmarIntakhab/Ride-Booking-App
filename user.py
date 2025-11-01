from time import sleep

class User:
    """This class contains all necessary information of a user
    and methods to work with the user wallet"""
    # --------------- Constructor ---------------
    # Initializes the user with name, contact, and wallet balance
    def __init__(self, name, contact, wallet_balance: int):
        self.name = name
        self.contact = contact
        self.__wallet_balance = wallet_balance

    # --------------- Get Balance ---------------
    def get_wallet_balance(self):
        """This method gets the wallet balance
        as it has been made private"""
        return self.__wallet_balance

    # --------------- Add Money ---------------
    def add_money(self, amount):
        """This method adds money to the user wallet"""
        print("Processing Transfer from bank......")
        sleep(1) #creates a real-world timing mechanism to pause for a moment before processing
        self.__wallet_balance += amount
        print(f"Rs.{amount} Added. Current balance: Rs.{self.__wallet_balance}")
    # --------------- Deduct money ---------------
    def deduct_fare(self, amount):
        """This method deducts money from wallet
        based on the fare ,and it returns False/True
         based on which out take payment functions """
        if self.__wallet_balance < amount: #check if the fare is more than user's money
            print("Insufficient Funds")
            return False
        else:
            print("Processing payment......")
            sleep(1)#creates a real-world timing mechanism to pause for a moment before processing
            self.__wallet_balance -= amount
            #Code Below 👇 is just to make the program user readable
            print("\n")
            print("-" * 50)
            print("\t\t\t\t\tPAYMENT CONFIRMATION")
            print("-" * 50)
            print("\n")
            #Code Above 👆is just to make the program user readable
            print(f"Payment Done. | Rs.{amount} deducted | Remaining balance: Rs.{self.__wallet_balance}")
            return True
    # --------------- User Summary ---------------
    def user_summary(self):
        """This method returns the user's name
        and wallet balance"""
        print(f"Name : {self.name} | Wallet Balance : {self.__wallet_balance}")