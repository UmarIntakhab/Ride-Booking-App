from user import User
from menu import menu
from validation import name_validation,contact_validation, money_validation

def main():
    #region INITIAL INPUT
    print("*********//WELCOME TO RIDE BOOKING APP//*********")  # Welcoming
    # code below 👇 to make it visually attractive
    print("-" * 50)
    print("\t\t\t\t\tUSER DETAILS")
    print("-" * 50)
    # code above 👆 to make it visually attractive
    # ASKING NAME CONTACT AND WALLET BALANCE TO LOGIN
    valid_name = name_validation()
    valid_contact = contact_validation()
    valid_wallet = money_validation()
    #endregion
    user1 = User(valid_name, valid_contact, valid_wallet)
    menu(user1)


if __name__ == '__main__':
    main()

