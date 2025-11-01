from ride import CarRide,BikeRide,AutoRide
from validation import distance_validation
from history import save_ride_history ,save_payment_history,ride_history,payment_history
import os
os.makedirs("history" ,exist_ok=True)
os.makedirs("Payment history" ,exist_ok=True)
# -------- Function: Booking --------
def booking(user):
    """Responsible for booking a cab based
    on user input.
    Ask the user which vehicle they want
    then checks if it is in out available vehicles
    """
    #region Main Loop
    while True:
        option = input("Select Vehicle :\n" #ask the user to select their vehicle
                       "* Car\n"
                       "* Bike\n"
                       "* Auto\n"
                       "Your Choice : ").title()
        print("\n")
        rides = {"Car": CarRide, "Bike": BikeRide, "Auto": AutoRide} #stores object(as value) in a dict with input as key to easily access them

        if option in rides: #check if user vehicle is in our dict
            #if yes
            dist = distance_validation() #user is asked to enter distance they want to travel
            ride = rides[option](user, dist, option) #selects our ride(object) from dict and initialise the object with required values
            # code below 👇 is just to make it visually attractive
            print("\n")
            print("-"*50)
            print("\t\t\t\t\tRIDE SUMMARY")
            print("-"*50)
            print("\n")
            # code above 👆 is just to make it visually attractive
            print(ride.ride_summary()) #prints user ride summary before payment
            # code below 👇 is just to make it visually attractive
            print("\n")
            print("-"*50)
            print("\t\t\t\t\tCONFIRMATION")
            print("-"*50)
            print("\n")
            # code above 👆 is just to make it visually attractive
            #this loop does not break yet as nothing has interrupted yet
            #region Second Loop to ask the user if they want to book or not
            while True:
                cont = input("Do you want to book a ride?(y/n) :").lower() # ask the user if they want to book or not
                if cont == 'y': #if yes
                    if ride.take_payment():#checks if ride.take_payment in our objects return True if yes then:-
                        #learner
                        save_ride_history(user,ride)
                        save_payment_history(user,ride)
                        # code below 👇 is just to make it visually attractive
                        print("\n")
                        print("-" * 50)
                        print("\t\t\t\t\tBOOKING DETAILS")
                        print("-" * 50)
                        print("\n")
                        # code above 👆 is just to make it visually attractive
                        print(ride.trip_summary()) #print trip summary when user confirms to book a ride.
                        print("\nBooking complete. Have a safe journey!\n")
                    break #loop breaks here and we return to menu
                elif cont == 'n': #if user say no to booking a ride
                    print("Ride cancelled. Goodbye then.")
                    break #loop breaks here and we return to menu
                else:
                    print("Enter a valid option please.")
                    #loops restart until user enters y or n
            #endregion
            break #main loop breaks here if the previous loop has worked as it should have
        else:
            print("Invalid option")
            #loop continues until user enters an available vehicle
    #endregion
# -------- Function: wallet_open(user) --------
def wallet_open(user):
    """Responsible for opening wallet
    and adding money to wallet"""
    #region Main Loop
    while True:
        #region Try block to check user input is int
        try:
            option = int(input("1.View Wallet\n"
                               "2.Add Money\n"
                               "Your Choice : ")) #asks the user to select what he wants to do with wallet
            if option == 1: #if he selects to view
                balance = user.get_wallet_balance() #wallet balance is called using a getter method from user class
                print(f"Current Wallet Balance : Rs.{balance}") #printed balance
                #region 2nd Main Loop to ask if they want to add money
                while True:
                    add = input("Want to add money?(y/n) : ").lower()
                    if add == 'y': #if yes
                        #region 3rd Loop to verify user entered an integer and runs until he does so
                        while True:
                            # region Try block to check user input is int
                            try:
                                # code below 👇 is just to make it visually attractive
                                print("\n")
                                print("-" * 50)
                                print("\t\t\t\tTRANSFERRING MONEY")
                                print("-" * 50)
                                print("\n")
                                # code above 👆 is just to make it visually attractive
                                amount = int(input("How much money to add? : ")) #asks user to enter amount of money
                                user.add_money(amount) #calles object function to add money
                                break #3rd loop breaks here
                            except ValueError:
                                print("Money should be in numbers") #if input is anything but integer it restarts 3rd loop)
                            # endregion
                        #endregion
                        break #2nd loop breaks here as user wants to add money and it has happened now
                    elif add == 'n': #if user selects not to add money
                        print("Leaving Wallet.....")
                        break #2nd loop breaks
                    else:
                        print("Enter a valid input")
                        #2nd loop restarts if user mistakenly entered a wrong input
                #endregion
                break #main loop breaks here as user has decided to add or not add money and we go back to menu
            elif option == 2:
                #region 2nd Main Loop to continue looping if money is not int
                while True:
                    #region Try block to check user enter money as int
                    try:
                        # code below 👇 is just to make it visually attractive
                        print("\n")
                        print("-" * 50)
                        print("\t\t\t\tTRANSFERRING MONEY")
                        print("-" * 50)
                        print("\n")
                        # code above 👆 is just to make it visually attractive
                        amount = int(input("How much money to add? : ")) #asks to add oney
                        print("\n")
                        user.add_money(amount) #adds money to user wallet
                        break #breaks 2nd loop if the user typed an integer
                    except ValueError:
                        print("Money should be in numbers") #if input is anything but integer it restarts 2nd loop)
                    #endregion
                break #main loop breaks here as user has decided how much money to add we go back to menu
                #endregion
            else:  # if user entered invalid integer we are leaving wallet
                print("Invalid input.\n"
                      "Leaving wallet......")
                break  # main loop breaks because of invalid input
        except ValueError:
            print("Enter a valid input.")#if user entered anything but integer the main loop restarts from here
        #endregion

    #endregion





# -------- Function: exit --------
def exit_app():
    """Exits the complete program when
    user selects the number corresponding
    to this function in main func"""
    print("Leaving app.......")
    #code below 👇 is just to make it visually attractive
    print("-"*50)
    print("\t\t\t\tTHANKS FOR VISITING")
    print("-" * 50)
    #code above 👆 is just to make it visually attractive
    quit()
#endregion
#region Menu
# ---------------------------------------------------------
# -------------------   MENU FUNCTIONS   ------------------
# ---------------------------------------------------------

# -------- Function: menu(user) --------
def menu(user):
    """ Displays menu to the user"""
    #region Main Loop
    while True:
        #Code below 👇is to make it visually attractive
        print("\n")
        print("-" * 50)
        print("\t\t\t\t\tAPP MENU")
        print("-" * 50)
        print("\n")
        #Code above 👆 is to make it visually attractive
        #region Try block to handle value error
        try:
            option = int(input("1.Book a ride\n"#shows option to the user
                               "2.Check Wallet\n"
                               "3.Ride History\n"
                               "4.Payment History\n"
                               "5.Exit\n"
                               "Your Choice : "))
            if option == 1:
                # Code below 👇is to make it visually attractive
                print("-"*50)
                print("\t\t\t\tBOOKING INTERFACE")
                print("-" * 50)
                # Code above 👆 is to make it visually attractive
                booking(user)#calls the booking function

            elif option == 2:
                wallet_open(user)#calls the wallet function
            elif option == 3:
                ride_history(user)
            elif option == 4:
                payment_history(user)
            elif option == 5:
                exit_app()#calls the exit function
                break #exits the loop and quit the app
            else:
                print("Enter a valid integer(1-3)") #continue looping in invalid integer is entered
        except ValueError:
            print("Enter a valid integer(1-3)")#continue looping in invalid integer is entered
        #endregion
    #endregion
#endregion