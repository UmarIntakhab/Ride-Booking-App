def add_money_to_wallet_user_input(user):
    try:
        # code below 👇 is just to make it visually attractive
        print("\n")
        print("-" * 50)
        print("\t\t\t\tTRANSFERRING MONEY")
        print("-" * 50)
        print("\n")
        # code above 👆 is just to make it visually attractive
        amount = int(input("How much money to add? : "))  # asks user to enter amount of money
        user.add_money(amount)  # calls object function to add money
        return True
    except ValueError:
        print("Money should be in numbers")
        return False# if input is anything but integer it restarts 3rd loop)