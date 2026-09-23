# Car Dealership Management System

A desktop-based Car Dealership Management System developed using Python and PyQt5.

## Project Overview

This project is a graphical user interface (GUI) application designed to manage different aspects of a car dealership.

The system consists of four main sections:

- Login
- Vehicle Management
- Customer Registration
- Vehicle Booking

## Features

### Login

The login screen allows a user to enter a username and password before accessing the system.

**Demo Login:**

- Username: `admin`
- Password: `admin123`

### Vehicle Management

The Vehicle Management screen allows the user to enter:

- Vehicle make
- Vehicle model
- Registration number
- Price
- Vehicle type
- Availability

Available vehicle types include:

- New Car
- Used Car
- SUV
- Sedan
- Hatchback
- Bakkie

Availability options include:

- Available
- Sold
- Reserved

### Customer Registration

The Customer Registration screen allows the user to enter:

- Customer name
- ID number
- Phone number
- Email
- Customer type
- Preferred contact method

Customer types include:

- Private Customer
- Business Customer

Preferred contact methods include:

- Phone
- Email
- SMS

### Vehicle Booking

The Vehicle Booking screen allows the user to enter:

- Customer name
- Vehicle registration number
- Booking date
- Booking status

Booking statuses include:

- Pending
- Confirmed
- Cancelled

## Technologies Used

- Python
- PyQt5
- Qt Designer
- Anaconda / Jupyter Notebook
- Git
- GitHub

## Project Structure
```text
Car Dealership Management System/
│
├── main.py
├── gui1.py
├── gui1.ui
├── gui2.py
├── gui2.ui
├── gui3.py
├── gui3.ui
├── gui4.py
├── gui4.ui
├── CarDealershipSystem.ui
├── requirements.txt
├── .gitignore
└── README.md
```

## How to Run

### 1. Install the required dependencies

Open Anaconda Prompt or a terminal and navigate to the project folder.

Run:

```bash
pip install -r requirements.txt
```

### 2. Run the application

Run:

```bash
python main.py
```

### 3. Login

Use the demo credentials:

```text
Username: admin
Password: admin123
```

## Skills Demonstrated

- Python programming
- PyQt5 GUI development
- Qt Designer
- Object-oriented programming
- Event-driven programming
- Form validation
- Working with multiple Python modules
- Git and GitHub

## Academic Project

This project was developed as part of my Visual Programming II coursework.

## Future Improvements

Possible future improvements include:

- Connecting the application to a database
- Adding stronger authentication
- Adding search and filtering
- Improving input validation
- Adding persistent vehicle and customer records
- Adding booking management and reporting
- Further improving the user interface
