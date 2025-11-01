from abc import ABC, abstractmethod
from time import sleep
import textwrap

#region Main Abstract Class
class Ride(ABC):
    """This is an 'abstract class' so the child class
    can inherit the main method that needs to be called"""
    # --------------- Constructor ---------------
    # Initializes the ride with user(object), distance and vehicle type
    def __init__(self, user, distance, vehicle_type):
        self.user = user
        self.distance = distance
        self.vehicle = vehicle_type
    # --------------- Calculate Fare ---------------
    @abstractmethod
    def calc_fare(self):
        """Abstract method that all child class should
        always have"""
        pass
    # --------------- Ride Summary ---------------
    def ride_summary(self):
        """Method that is called in each child class
        with different implementation"""
        return (f"{self.vehicle} Ride Summary \n----------------------------------\n"
                f"Pickup Confirmed for: {self.user.name}"
                f"Ride Type: {self.vehicle}\n"
                f"Distance: {self.distance} km")
#endregion

#region Car Ride Class
# =========================================================
# ===============   CAR RIDE CLASS SECTION   ==================
# =========================================================
class CarRide(Ride):
    """This class deals with the car ride
    inherits required function from parent class
    and alters them as required"""
    # --------------- Constructor ---------------
    # Initializes the ride with user(object), distance and vehicle type
    def __init__(self, user, distance, vehicle_type, fare_per_km=20): #assigned fare as per the vehicle
        super().__init__(user, distance, vehicle_type) #inherited base class's attributes
        self.fare_per_km = fare_per_km
    # --------------- Calculate Total Fare ---------------
    def calc_total_fare(self):
        """Returns total fare based on
        distance to be travelled provided by user
        multiplied by vehicles rate per km
        includes base charge of Rs.50"""
        total_fare = self.distance * self.fare_per_km + 50
        return total_fare
    # --------------- Calculate Fare ---------------
    def calc_fare(self):
        """Returns Total Fare"""
        return f"Total Fare : Rs.{self.calc_total_fare()}"
    # --------------- Take Payment ---------------
    def take_payment(self):
        """Uses double confirmation to make payment
        and deduct money from user wallet based on
        what user decides."""

        #region main loop
        #Check if user has enough money in his/her wallet
        #if not it asks user to recharge
        while True:
            if self.user.deduct_fare(self.calc_total_fare()): #if wallet > fare user.deduct_fare works and makes the payment

                return True #main loop breaks here cuz no interruption has been there yet
            recharge = input("Do you want to recharge funds?(Y/N) : ").lower() #user is asked to recharge wallet
            if recharge == 'y': #if user says yes
                #region try block if user types anything instead of integer as a money input
                try:
                    # Code Below 👇 is just to make the program user readable
                    print("-" * 50)
                    print("\t\t\t\t\tTRANSFERRING MONEY")
                    print("-" * 50)
                    # Code Above 👆is just to make the program user readable
                    how_much = int(input("What amount do you want to add? : ")) #asks the user to add money
                    self.user.add_money(how_much) #calls user method to add money
                    double_confirmation = input("Do you want to pay now?(Y/N) : ").lower() #after adding money it asks again if the user wants to pay or not
                    if double_confirmation == 'y':#if user says yes
                        sleep(1) #to make real-world-like wait before processing payment
                        print("Processing payment......")
                        return True #based on this value our booking function is able to book a ride...loop breaks here
                    elif double_confirmation == 'n':#if user says no
                        print("\n")
                        print("Sorry You Cant Book a Ride Then.")
                        return False #based on this value our booking function is not able to book a ride...loop breaks here
                    else:#if user enters a invalid input
                        print("Leaving, since you did not provide a valid input.")
                        break # loop breaks as user did not provide a valid input
                except ValueError:
                    print("Come on man! money can not be a letter. Type an integer")#the loop continues if money is anything but an integer
                #endregion
            elif recharge == 'n':#if user says no
                print("\n")
                print("Sorry You Cant Book a Ride Then.")
                return False #loop break here and it prints this line as user did not want to recharge
            else:#if user enters a invalid input
                print("Please enter a valid input.")
        #endregion
    # --------------- Ride Summary ---------------
    def ride_summary(self):
        """Method that is inherited from parent class
        and gives summary of the ride before asking the user
        to make payment"""
        base = super().ride_summary()
        return (f"{base}\n"
                f"Estimated Fare : {self.calc_total_fare()}\n"
                f"Amenities    : Air Conditioned, Music System "
                f"Driver will arrive shortly!")
    # --------------- Trip Summary ---------------
    def trip_summary(self):
        """Returns the trip summary after the user has paid"""
        return textwrap.dedent(f"""
        Trip Summary:
        Rider Name      : {self.user.name}
        Vehicle Type    : {self.vehicle}
        Distance        : {self.distance} km
        Final Fare Paid : Rs.{self.calc_total_fare()}
        Payment Status  : Completed
        """)
#endregion
#region Bike Ride Class
# =========================================================
# ===============   BIKE RIDE CLASS SECTION   ==================
# =========================================================
class BikeRide(Ride):
    """This class deals with the bike ride
        inherits required function from parent class
        and alters them as required"""
        # --------------- Constructor ---------------
    # Initializes the ride with user(object), distance and vehicle type
    def __init__(self, user, distance, vehicle_type, fare_per_km=15):#assigned fare as per the vehicle
        super().__init__(user, distance, vehicle_type)#inherited base class's attributes
        self.fare_per_km = fare_per_km
    # --------------- Calculate Total Fare ---------------
    def calc_total_fare(self):
        """Returns total fare based on
        distance to be travelled provided by user
        multiplied by vehicles rate per km
        includes base charge of Rs.30"""
        total_fare = self.distance * self.fare_per_km + 30
        return total_fare
    # --------------- Calculate Fare ---------------
    def calc_fare(self):
        """Returns Total Fare"""
        return f"Your total fare : Rs.{self.calc_total_fare()}"
    # --------------- Take Payment ---------------
    def take_payment(self):
        """Uses double confirmation to make payment
        and deduct money from user wallet based on
        what user decides."""
        # region main loop
        # Check if user has enough money in his/her wallet
        # if not it asks user to recharge
        while True:
            if self.user.deduct_fare(self.calc_total_fare()):#if wallet > fare user.deduct_fare works and makes the payment
                return True#main loop breaks here cuz no interruption has been there yet
            recharge = input("Do you want to recharge funds?(Y/N) : ").lower()#user is asked to recharge wallet
            if recharge == 'y':#if user says yes
                #region try block if user types anything instead of integer as a money input
                try:
                    # Code Below 👇 is just to make the program user readable
                    print("-" * 50)
                    print("\t\t\t\t\tPAYMENT CONFIRMATION")
                    print("-" * 50)
                    # Code Above 👆is just to make the program user readable
                    how_much = int(input("What amount do you want to add? : "))#asks the user to add money
                    self.user.add_money(how_much)
                    double_confirmation = input("Do you want to pay now?(Y/N) : ").lower()#after adding money it asks again if the user wants to pay or not
                    if double_confirmation == 'y':#if user says yes
                        sleep(1)#to make real-world-like wait before processing payment
                        print("Processing payment......")
                        return True#based on this value our booking function is able to book a ride...loop breaks here
                    elif double_confirmation == 'n':#if user says no
                        print("\n")
                        print("Sorry You Cant Book a Ride Then.")
                        return False#based on this value our booking function is not able to book a ride...loop breaks here
                    else:#if user enters a invalid input
                        print("Leaving, since you did not provide a valid input.")
                        break# loop breaks as user did not provide a valid input
                except ValueError:
                    print("Come on man! money can not be a letter. Type an integer")#the loop continues if money is anything but an integer
                #endregion
            elif recharge == 'n':#if user says no
                print("\n")
                print("Sorry You Cant Book a Ride Then.")
                return False#loop break here and it prints this line as user did not want to recharge
            else:#if user enters a invalid input
                print("Please enter a valid input.")
        #endregion
    # --------------- Ride Summary ---------------
    def ride_summary(self):
        """Method that is inherited from parent class
        and gives summary of the ride before asking the user
        to make payment"""
        base = super().ride_summary()
        return (f"{base}\n"
                f"Estimated Fare : {self.calc_total_fare()}\n"
                f"Amenities    : Helmets Provided "
                f"Driver will arrive shortly!")
        # --------------- Trip Summary ---------------
    def trip_summary(self):
        """Returns the trip summary after the user has paid"""
        return textwrap.dedent(f"""
        Trip Summary:
        Rider Name      : {self.user.name}
        Vehicle Type    : {self.vehicle}
        Distance        : {self.distance} km
        Final Fare Paid : Rs.{self.calc_total_fare()}
        Payment Status  : Completed
        """)
#endregion
#region Auto Ride Class
# =========================================================
# ===============   AUTO RIDE CLASS SECTION   ==================
# =========================================================
class AutoRide(Ride):
    # --------------- Constructor ---------------
    # Initializes the ride with user(object), distance and vehicle type
    def __init__(self, user, distance, vehicle_type, fare_per_km=10):#assigned fare as per the vehicle
        super().__init__(user, distance, vehicle_type)#inherited base class's attributes
        self.fare_per_km = fare_per_km
    # --------------- Calculate Total Fare ---------------
    def calc_total_fare(self):
        """Returns total fare based on
        distance to be travelled provided by user
        multiplied by vehicles rate per km
        includes base charge of Rs.20"""
        total_fare = self.distance * self.fare_per_km + 20
        return total_fare
    # --------------- Calculate Fare ---------------
    def calc_fare(self):
        """Returns Total Fare"""
        return f"Your total fare : Rs.{self.calc_total_fare()}"
    # --------------- Take Payment ---------------
    def take_payment(self):
        """Uses double confirmation to make payment
                and deduct money from user wallet based on
                what user decides."""
        # region main loop
        # Check if user has enough money in his/her wallet
        # if not it asks user to recharge
        while True:
            if self.user.deduct_fare(self.calc_total_fare()):  # if wallet > fare user.deduct_fare works and makes the payment
                return True  # main loop breaks here cuz no interruption has been there yet
            recharge = input("Do you want to recharge funds?(Y/N) : ").lower()  # user is asked to recharge wallet
            if recharge == 'y':  # if user says yes
                # region try block if user types anything instead of integer as a money input
                try:
                    # Code Below 👇 is just to make the program user readable
                    print("-" * 50)
                    print("\t\t\t\t\tPAYMENT CONFIRMATION")
                    print("-" * 50)
                    # Code Above 👆is just to make the program user readable
                    how_much = int(input("What amount do you want to add? : "))  # asks the user to add money
                    self.user.add_money(how_much)
                    double_confirmation = input(
                        "Do you want to pay now?(Y/N) : ").lower()  # after adding money it asks again if the user wants to pay or not
                    if double_confirmation == 'y':  # if user says yes
                        print("Processing payment......")
                        sleep(1)  # to make real-world-like wait before processing payment
                        return True  # based on this value our booking function is able to book a ride...loop breaks here
                    elif double_confirmation == 'n':  # if user says no
                        print("\n")
                        print("Sorry You Cant Book a Ride Then.")
                        return False  # based on this value our booking function is not able to book a ride...loop breaks here
                    else:  # if user enters a invalid input
                        print("Leaving, since you did not provide a valid input.")
                        break  # loop breaks as user did not provide a valid input
                except ValueError:
                    print(
                        "Come on man! money can not be a letter. Type an integer")  # the loop continues if money is anything but an integer
                # endregion
            elif recharge == 'n':  # if user says no
                print("\n")
                print("Sorry You Cant Book a Ride Then.")
                return False  # loop break here and it prints this line as user did not want to recharge
            else:  # if user enters a invalid input
                print("Please enter a valid input.")
        # endregion
    # --------------- Ride Summary ---------------
    def ride_summary(self):
        """Method that is inherited from parent class
        and gives summary of the ride before asking the user
        to make payment"""
        base = super().ride_summary()
        return (f"{base}\n"
                f"Estimated Fare : {self.calc_total_fare()}\n"
                f"Driver will arrive shortly!")
        # --------------- Trip Summary ---------------
    def trip_summary(self):
        """Returns the trip summary after the user has paid"""
        return textwrap.dedent(f"""
        Trip Summary:
        Rider Name      : {self.user.name}
        Vehicle Type    : {self.vehicle}
        Distance        : {self.distance} km
        Final Fare Paid : Rs.{self.calc_total_fare()}
        Payment Status  : Completed
        """)
#endregion
