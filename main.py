import sys

from PyQt5.QtWidgets import (
    QApplication,
    QMainWindow,
    QMessageBox
)

from gui1 import Ui_MainWindow
from gui2 import Ui_MainWindow as Ui_VehicleWindow
from gui3 import Ui_MainWindow as Ui_CustomerWindow
from gui4 import Ui_MainWindow as Ui_BookingWindow


class LoginWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.loginButton.clicked.connect(self.login)

        self.ui.cancelButton.clicked.connect(self.cancel)

    def login(self):

        username = self.ui.usernameLineEdit.text()
        password = self.ui.passwordLineEdit.text()

        if username == "admin" and password == "admin123":

            QMessageBox.information(
                self,
                "Login Successful",
                "Welcome to the Car Dealership Management System!"
            )

            self.vehicleWindow = VehicleWindow()
            self.vehicleWindow.show()

            self.hide()

        else:

            QMessageBox.warning(
                self,
                "Login Failed",
                "Incorrect username or password."
            )

    def cancel(self):

        self.ui.usernameLineEdit.clear()
        self.ui.passwordLineEdit.clear()

class VehicleWindow(QMainWindow):

    def __init__(self):
        super().__init__()

        self.ui = Ui_VehicleWindow()
        self.ui.setupUi(self)

        # Connect buttons
        self.ui.saveVehicleButton.clicked.connect(self.save_vehicle)
        self.ui.clearButton.clicked.connect(self.clear_fields)
        self.ui.backButton.clicked.connect(self.go_back)

    def save_vehicle(self):

        make = self.ui.vehicleMakeLineEdit.text()
        model = self.ui.vehicleModelLineEdit.text()
        registration = self.ui.registrationLineEdit.text()
        price = self.ui.priceLineEdit.text()
        vehicle_type = self.ui.vehicleTypeComboBox.currentText()
        availability = self.ui.availabilityComboBox.currentText()

        if make == "" or model == "" or registration == "" or price == "":

            QMessageBox.warning(
                self,
                "Missing Information",
                "Please complete all vehicle information."
            )

            return

        QMessageBox.information(
            self,
            "Vehicle Saved",
            "Vehicle information has been saved successfully.\n\n"
        )
        self.customerWindow = CustomerWindow()
        self.customerWindow.show()
        self.hide()
        

    def clear_fields(self):

        self.ui.vehicleMakeLineEdit.clear()
        self.ui.vehicleModelLineEdit.clear()
        self.ui.registrationLineEdit.clear()
        self.ui.priceLineEdit.clear()

        self.ui.vehicleTypeComboBox.setCurrentIndex(0)
        self.ui.availabilityComboBox.setCurrentIndex(0)

    def go_back(self):

        self.close()
        self.loginWindow = LoginWindow()
        self.loginWindow.show()

class CustomerWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_CustomerWindow()
        self.ui.setupUi(self)

        self.ui.saveCustomerButton.clicked.connect(self.save_customer)
        self.ui.clearButton.clicked.connect(self.clear_fields)
        self.ui.backButton.clicked.connect(self.go_back)
        self.ui.saveCustomerButton.clicked.connect(self.open_booking)

    def save_customer(self):
        name = self.ui.customerNameLineEdit.text()
        id_number = self.ui.idNumberLineEdit.text()
        phone = self.ui.phoneLineEdit.text()
        email = self.ui.emailLineEdit.text()

        if name == "" or id_number == "" or phone == "" or email == "":
            QMessageBox.warning(
                self,
                "Missing Information",
                "Please complete all customer information."
            )
            return

        if self.ui.privateRadioButton.isChecked():
            customer_type = "Private Customer"
        elif self.ui.businessRadioButton.isChecked():
            customer_type = "Business Customer"
        else:
            customer_type = "Not Selected"

        contact_method = self.ui.contactMethodComboBox.currentText()

        QMessageBox.information(
            self,
            "Customer Saved",
            "Customer information has been saved successfully.\n\n"
            f"Name: {name}\n"
            f"ID Number: {id_number}\n"
            f"Phone: {phone}\n"
            f"Email: {email}\n"
            f"Customer Type: {customer_type}\n"
            f"Preferred Contact: {contact_method}"
        )

    def clear_fields(self):
        self.ui.customerNameLineEdit.clear()
        self.ui.idNumberLineEdit.clear()
        self.ui.phoneLineEdit.clear()
        self.ui.emailLineEdit.clear()
        self.ui.privateRadioButton.setChecked(False)
        self.ui.businessRadioButton.setChecked(False)
        self.ui.contactMethodComboBox.setCurrentIndex(0)

    def go_back(self):
        self.close()
        self.vehicleWindow = VehicleWindow()
        self.vehicleWindow.show()

    def open_booking(self):
        self.bookingWindow = BookingWindow()
        self.bookingWindow.show()
        self.hide()

class BookingWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_BookingWindow()
        self.ui.setupUi(self)

        self.ui.saveBookingButton.clicked.connect(self.save_booking)
        self.ui.clearButton.clicked.connect(self.clear_fields)
        self.ui.backButton.clicked.connect(self.go_back)

    def save_booking(self):
        customer = self.ui.bookingCustomerLineEdit.text()
        registration = self.ui.bookingRegistrationLineEdit.text()
        date = self.ui.bookingCalendarWidget.selectedDate().toString("dd MMMM yyyy")
        status = self.ui.bookingStatusComboBox.currentText()

        if customer == "" or registration == "":
            QMessageBox.warning(
                self,
                "Missing Information",
                "Please enter the customer name and vehicle registration."
            )
            return

        QMessageBox.information(
            self,
            "Booking Saved",
            "Vehicle booking has been saved successfully.\n\n"
            f"Customer: {customer}\n"
            f"Vehicle Registration: {registration}\n"
            f"Booking Date: {date}\n"
            f"Status: {status}"
        )

    def clear_fields(self):
        self.ui.bookingCustomerLineEdit.clear()
        self.ui.bookingRegistrationLineEdit.clear()
        self.ui.bookingStatusComboBox.setCurrentIndex(0)

    def go_back(self):
        self.close()
        self.customerWindow = CustomerWindow()
        self.customerWindow.show()

app = QApplication(sys.argv)

window = LoginWindow()
window.show()

sys.exit(app.exec_()) this is whats in untitled2



