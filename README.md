# Ride Booking System (Python - OOP Based)

A Python project implementing a Ride Booking Application using Object Oriented Programming principles.  
This project also uses text file handling to store a user’s ride history.

---

## Features

- New User Registration
- Wallet System (Add money / Deduct Fare on Booking)
- Book Ride (Auto / Bike / Car)
- Fare Calculation based on Vehicle + Distance
- Cancel Ride
- View Ride Summary
- Ride History stored in text files (per user)
- Input Validation Functions (email, username, password)

---

## Project Folder Structure
```
ride_booking/
│
├── history/ (Auto generated to store ride histories)
├── Payment history/ (Auto generated to store ride histories)
├── README.md
├── history
├── main.py
├── menu.py
├── ride.py
├── user.py
└── validation.py
```
---

## How To Run

1. Clone the repo  
2. In terminal:

```bash
python3 main.py
```

## Technologies Used

* Python 3.x
* Object Oriented Programming
* File Handling (Text Based)

## Future Enhancements

* Replace text based history with SQLite database
* Add Driver Recommendation / Match System
* Add web frontend or GUI
* Add authentication security for login