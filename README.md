# Car Dealership Management System

A GUI-based Car Dealership Management System developed using Python and PyQt5 as part of my Visual Programming II coursework.

## Overview

The application provides a graphical interface for managing different aspects of a car dealership, including vehicle information, customer registration and vehicle bookings.

The system consists of four main interfaces:

1. Login
2. Vehicle Management
3. Customer Registration
4. Vehicle Booking

## Features

### Login

The login interface provides fields for:

- Username
- Password

It also provides Login and Cancel controls.

### Vehicle Management

The vehicle management interface captures:

- Vehicle make
- Vehicle model
- Registration number
- Price
- Vehicle type
- Availability

Vehicle types include:

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

The customer registration interface captures:

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

The vehicle booking interface captures:

- Customer name
- Vehicle registration number
- Booking date
- Booking status

Booking statuses include:

- Pending
- Confirmed
- Cancelled

## Technologies

- Python
- PyQt5
- Qt Designer
- Jupyter Notebook / Anaconda

## Project Structure

```text
car-dealership-management-system/
│
├── README.md
├── requirements.txt
├── .gitignore
│
├── untitled2.ipynb
├── CarDealershipSystem.ui
│
├── gui1.py
├── gui1.ui
├── gui2.py
├── gui2.ui
├── gui3.py
├── gui3.ui
├── gui4.py
└── gui4.ui
