from datetime import datetime , date

# -------- Function:Save  Ride History --------
def save_ride_history(user,ride):
    file_path = f"history/ride_history_for_{user.name}.txt"
    try:
        with open(file_path, "r") as history:
            content = history.read().strip()
            ride_no = 1 if content == "" else content.count("Ride #") + 1
    except FileNotFoundError:
        ride_no = 1
    with open(file_path, "a") as history:
        history.write(f"\n===== Ride #{ride_no} =====\n")
        history.write(ride.trip_summary() + "\n")

# -------- Function: Ride History --------
def ride_history(user):
    file_path = f"history/ride_history_for_{user.name}.txt"
    print("\n")
    print("-"*50)
    print(f"\t\t\t\tRIDE HISTORY")
    print("-"*50)
    try:
        with open(file_path,"r") as history:
            content = history.read()
            print(content)
    except FileNotFoundError:
        print(f"No trips has been made yet by {user.name}")

# -------- Function: Save Payment History --------
def save_payment_history(user,ride):
    file_path = f"Payment history/Payment_history_of_{user.name}.txt"
    now = datetime.now()
    current_time = now.strftime("%H:%M:%S")
    try:
        with open(file_path, "r") as payment:
            content = payment.read().strip()
            payment_no = 1 if content == "" else content.count("Payment Made") + 1
    except FileNotFoundError:
        payment_no = 1
    with open(file_path, "a") as payment:
        payment.write(f"{payment_no}.[{date.today()}] | [{current_time}] | Payment Made : Rs.{ride.calc_total_fare()}\n")

# -------- Function: show Payment History --------

def payment_history(user):
    file_path = f"Payment history/Payment_history_of_{user.name}.txt"
    print("\n")
    print("-"*50)
    print(f"\t\t\t\tPAYMENT HISTORY")
    print("-"*50)
    print("\n")
    try:
        with open(file_path,"r") as history:
            content = history.read()
            print(content)
    except FileNotFoundError:
        print(f"No payment has been made yet by {user.name}")