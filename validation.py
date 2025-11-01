# -------- Function: name_validation --------
def name_validation():
    """Asks user to enter their name and if
    input is anything but an alphabet it loops the function
    until user enters a valid name"""
    while True:
        user_name = input("Enter Name : ")
        if not user_name.replace(" ", "").isalpha():
            print("Please enter a valid name.")
        else:
            break
    return user_name #gives correct username as an output

# -------- Function: contact_validation --------
def contact_validation():
    """Asks user to enter their contact
    and if input is anything but a digit
    and less than or greater than 10 it
    loops the function until user enters
    a valid contact"""
    while True:
        contact = input("Enter Contact Number : ")
        if (not contact.isdigit()) or len(contact) != 10:
            print("You did not enter a valid contact number")
        else:
            break
    return contact #gives correct contact as an output

# -------- Function: money_validation --------
def money_validation():
    """Asks user to enter their wallet
    balance and uses try block to check if
    the input is integer and the loop
    continues until user types an integer.
    and loop also continues if money is less
    than 0"""
    while True:
        try:
            wallet_input = int(input("Enter Wallet Amount : "))
            if wallet_input < 0:
                print("Money can not be less than 0")
            else:
                break
        except ValueError:
            print("Please enter a integer.")
    return wallet_input #gives correct money balance as an output

# -------- Function: distance_validation --------
def distance_validation():
    """Asks user to enter distance they
    want to travel in km and if user types
    distance < 0 or if distance is not an
    integer then the loop continues asking
    again until user enters a valid distance"""
    while True:
        try:
            dist = int(input("How far is your destination? : "))
            if dist < 0:
                print("Distance must be greater than 0")
            else:
                break
        except ValueError:
            print("Can distance be in words? No right? Enter an integer")
    return dist #returns distance as an output
#