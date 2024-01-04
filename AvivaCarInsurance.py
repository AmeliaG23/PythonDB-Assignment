import sqlite3
from datetime import date


# Class- contains all data related to the customer and contains validations
class Customer:
    def __init__(self, customerName, customerPhoneNo, customerGender, customerAge, customerLicenceType):
        # constructor
        self.name = customerName
        self.phoneNo = customerPhoneNo
        self.gender = customerGender
        self.age = customerAge
        self.licenceType = customerLicenceType

    # Defines customer name
    @property
    def name(self):
        return self._name

    # Sets name value
    @name.setter
    def name(self, customerName):
        # Try/Except - outputs an error if the input is not in the correct format
        try:
            print("Enter your name:")
            customerName = input()  # Saves input to variable
        except:
            print("Error")  # When name errors
        self._name = customerName

    # Defines phone Number
    @property
    def phoneNo(self):
        return self.__phoneNo

    # Sets phone number value
    @phoneNo.setter
    def phoneNo(self, customerPhoneNo):
        validPhoneNo = False
        # While Loop - repeats until the input is classed as valid
        while not validPhoneNo:
            # Try/Except - outputs an error if the input is not in the correct format
            try:
                (print("Phone Number: "))
                customerPhoneNo = input()
                # If Statement - checks the input is 11 characters long and meaningful
                if len(customerPhoneNo) > 11 or len(customerPhoneNo) < 11:
                    print("Phone number is not the correct length")
                else:
                    validPhoneNo = True
            except:
                print("Input is not in a phone number format")
        self.__phoneNo = customerPhoneNo

    # Defines gender
    @property
    def gender(self):
        return self.__gender

    # Sets gender value
    @gender.setter
    def gender(self, customerGender):
        validGender = False
        # While Loop - repeats until the input is classed as valid
        while not validGender:
            # Try/Except - outputs an error if the input is not in the correct format
            try:
                print("Gender- M, F or O (for other): ")
                customerGender = input().capitalize()  # Capitalizes the char input
                # If Statement - checks the input is matching and meaningful
                if customerGender == 'M' or customerGender == 'F' or customerGender == 'O':
                    validGender = True
                else:
                    print("Input is not one of the recognisable options")
            except:
                print("Input is not a single character")
        self.__gender = customerGender

    # Defines age
    @property
    def age(self):
        return self.__age

    # Sets age value
    @age.setter
    def age(self, customerAge):
        validAge = False
        # While Loop - repeats until the input is classed as valid
        while not validAge:
            # Try/Except - outputs an error if the input is not in the correct format
            try:
                print("Age: ")
                customerAge = int(input())  # Changes the data type from str to int when being saved
                # If Statement - checks the input is more than or equal to 17 and meaningful
                if customerAge <= 17:
                    print("The customer is not old enough to have insurance with us")
                else:
                    validAge = True
            except:
                print("Input is not a number")
        self.__age = customerAge

    # Defines licence type
    @property
    def licenceType(self):
        return self.__licenceType

    # Sets licence type
    @licenceType.setter
    def licenceType(self, customerLicenceType):
        validLicenceType = False
        # While Loop - repeats until the input is classed as valid
        while not validLicenceType:
            # Try/Except - outputs an error if the input is not in the correct format
            try:
                print("Licence Type (Auto or Full):")
                customerLicenceType = input().capitalize()  # Capitalizes the input
                # If Statement - checks the input is matching and meaningful
                if customerLicenceType == "Auto" or customerLicenceType == "Full":
                    validLicenceType = True
                else:
                    print("Licence type is not recognised")
            except:
                print("Error")
        self.__licenceType = customerLicenceType


# Class- contains all data related to a vehicle for an insurance policy and includes validations for data
class Vehicle:
    def __init__(self, vehicleReg):
        # constructor
        self.reg = vehicleReg

    # Defines reg
    @property
    def reg(self):
        return self.__reg

    # Sets reg value
    @reg.setter
    def reg(self, vehicleReg):
        validReg = False
        # While Loop - repeats until the input is classed as valid
        while not validReg:
            # Try/Except - outputs an error if the input is not in the correct format
            try:
                print("Reg: ")
                vehicleReg = input().upper()  # Capitalizes the whole input
                # If Statement - checks the input is less than 7 characters long and meaningful
                if len(vehicleReg) > 7:
                    print("Registration Number is too long")
                else:
                    validReg = True
            except:
                print("Error")
        self.__reg = vehicleReg


# Class- contains all data related to the insurance and contains all validations for the data
class Insurance:
    def __init__(self, insuranceDate, paymentType):
        # constructor
        self.insuranceDate = insuranceDate
        self.paymentType = paymentType

    # Defines insurance date
    @property
    def insuranceDate(self):
        return self.__insuranceDate

    # Sets insurance date
    @insuranceDate.setter
    def insuranceDate(self, insuranceDate):
        insuranceDate = date.today()
        self.__insuranceDate = insuranceDate

    # Defines payment type
    @property
    def paymentType(self):
        return self._paymentType

    # Sets payment type
    @paymentType.setter
    def paymentType(self, paymentType):
        validPaymentType = False
        # While Loop - repeats until the input is classed as valid
        while not validPaymentType:
            # Try/Except - outputs an error if the input is not in the correct format
            try:
                print("Payment Type (Yearly or Monthly): ")
                paymentType = input().capitalize()  # Capitalizes user input
                # If Statement - checks the input is matching and meaningful
                if paymentType == "Yearly" or paymentType == "Monthly":
                    validPaymentType = True  # Stops the while loop if the if statement is true
                else:
                    print("Payment type is not recognised- Yearly or Monthly")  # If the  if statement is false
            except:
                print("Error")
        self._paymentType = paymentType


# Creates connection to the database which stores all of the insurance details
connection = sqlite3.connect('CarInsuranceDetails.db')
cursor = connection.cursor()
dateStarted = date.today()

# ONCE THE PROGRAM HAS BEEN RAN ONCE, PLEASE COMMENT OUT FROM LINE 11 TILL LINE 121
# Created the database table to store the car insurance details to
# cursor.execute("""CREATE TABLE CarDetailsTable (
# name text,
# phoneNo integer,
# gender char,
# age integer,
# vehicleReg text,
# licenceType text,
# paymentType text,
# dateStarted text
# )""")

cursor.execute(
    "INSERT INTO CarDetailsTable VALUES (:name, :phoneNo, :gender, :age, :vehicleReg, :licenceType, "
    ":paymentType, :dateStarted)",
    {
        'name': "Amelia Goldsby",
        'phoneNo': '077843255318',
        'gender': 'F',
        'age': 19,
        'vehicleReg': "P8XAR",
        'licenceType': "Auto",
        'paymentType': "Monthly",
        'dateStarted': dateStarted,
    }
)

cursor.execute(
    "INSERT INTO CarDetailsTable VALUES (:name, :phoneNo, :gender, :age, :vehicleReg, :licenceType, "
    ":paymentType, :dateStarted)",
    {
        'name': "Max Pike",
        'phoneNo': '077843255319',
        'gender': 'M',
        'age': 21,
        'vehicleReg': "M8XPK",
        'licenceType': "Full",
        'paymentType': "Yearly",
        'dateStarted': dateStarted,
    }
)
cursor.execute(
    "INSERT INTO CarDetailsTable VALUES (:name, :phoneNo, :gender, :age, :vehicleReg, :licenceType, "
    ":paymentType, :dateStarted)",
    {
        'name': "John Smith",
        'phoneNo': '077843278919',
        'gender': 'M',
        'age': 39,
        'vehicleReg': "RJ19MJO",
        'licenceType': "Full",
        'paymentType': "Monthly",
        'dateStarted': dateStarted,
    }
)
cursor.execute(
    "INSERT INTO CarDetailsTable VALUES (:name, :phoneNo, :gender, :age, :vehicleReg, :licenceType, "
    ":paymentType, :dateStarted)",
    {
        'name': "Lisa Newman",
        'phoneNo': '077843675319',
        'gender': 'F',
        'age': 29,
        'vehicleReg': "LM68PWE",
        'licenceType': "Full",
        'paymentType': "Yearly",
        'dateStarted': dateStarted,
    }
)
cursor.execute(
    "INSERT INTO CarDetailsTable VALUES (:name, :phoneNo, :gender, :age, :vehicleReg, :licenceType, "
    ":paymentType, :dateStarted)",
    {
        'name': "Jack March ",
        'phoneNo': '077393285319',
        'gender': 'O',
        'age': 18,
        'vehicleReg': "RE13PEO",
        'licenceType': "Full",
        'paymentType': "Monthly",
        'dateStarted': dateStarted,
    }
)
cursor.execute(
    "INSERT INTO CarDetailsTable VALUES (:name, :phoneNo, :gender, :age, :vehicleReg, :licenceType, "
    ":paymentType, :dateStarted)",
    {
        'name': "Sarah Jarrod",
        'phoneNo': '077843215319',
        'gender': 'F',
        'age': 44,
        'vehicleReg': "PE21RNO",
        'licenceType': "Auto",
        'paymentType': "Monthly",
        'dateStarted': dateStarted,
    }
)
cursor.execute(
    "INSERT INTO CarDetailsTable VALUES (:name, :phoneNo, :gender, :age, :vehicleReg, :licenceType, "
    ":paymentType, :dateStarted)",
    {
        'name': "Hugo Arrons",
        'phoneNo': '077648215381',
        'gender': 'M',
        'age': 50,
        'vehicleReg': "PO22UXJ",
        'licenceType': "Full",
        'paymentType': "Monthly",
        'dateStarted': dateStarted,
    }
)


# Method- allows the user to enter a policy number and returns it
def getChosenPolicyNo():
    chosenPolicy = 0
    validChosenPolicyNo = False
    # While loop - repeats until the input is in the right format (when set to true)
    while not validChosenPolicyNo:
        # Try/Except - outputs an error if the input is not in the correct format
        try:
            print("What is the chosen policy number?")
            chosenPolicy = int(input())  # Saves input as an integer to a local variable
            validChosenPolicyNo = True  # Means that the input is in the correct format
        except:
            print("Input is not recognised, try again.")

    return chosenPolicy


# Method - Gets details for a new customer and saves it to the database
def addPolicy():
    # Creates objects of each class
    customer = Customer("", 0, '', 0, "")
    vehicle = Vehicle("")
    insurance = Insurance("", "")
    # Try/Except - if the details cannot be stored to the database, an error message will be displayed
    try:
        cursor.execute(
            "INSERT INTO CarDetailsTable VALUES (:name, :phoneNo, :gender, :age, :vehicleReg, :licenceType, "
            ":paymentType, :dateStarted)",  # Inserts the data into the database
            {
                # Calls methods to get details and store them to the database
                'name': customer.name,
                'phoneNo': customer.phoneNo,
                'gender': customer.gender,
                'age': customer.age,
                'vehicleReg': vehicle.reg,
                'licenceType': customer.licenceType,
                'paymentType': insurance.paymentType,
            })
    except:
        print("Error - Could not write to the database")


# Method - allows a user to update the details of a policy
def updatePolicy():
    print("---Update a Policy---")
    print("")
    displayAllPolicies()  # Calls method to display all policies
    chosenPolicyNo = str(getChosenPolicyNo())  # Calls method to get a chosen policy number off of the user and
    # stores it locally
    # Creates objects of each class
    customer = Customer("", 0, '', 0, "")
    vehicle = Vehicle("")
    insurance = Insurance("", "")
    # Try/Except - if the details of the chosen policy cannot be updated, an error message will appear, not break
    try:
        cursor.execute("""UPDATE CarDetailsTable SET name = :name, phoneNo = :phoneNo, gender = :gender, 
        age = :age, vehicleReg = :vehicleReg, licenceType = :licenceType, paymentType = :paymentType WHERE oid = 
        :oid""",
                       {
                           'name': customer.name,
                           'phoneNo': customer.phoneNo,
                           'gender': customer.gender,
                           'age': customer.age,
                           'vehicleReg': vehicle.reg,
                           'licenceType': customer.licenceType,
                           'paymentType': insurance.paymentType,
                           'oid': chosenPolicyNo
                       })
        connection.commit()
    except:
        print("Error- could not update chosen record. ")


# Method- allows a user to delete a policy from entering a policy number
def deletePolicy():
    print("---Delete---")
    displayAllPolicies()  # Calls method to display all policies
    chosenPolicyNo = str(getChosenPolicyNo())  # Calls method to get a chosen policy number off of the user and
    # stores it locally
    # Try/Except - if the policy cannot be deleted from the database, it will ensure the code will not stop
    try:
        cursor.execute("DELETE FROM CarDetailsTable WHERE oid =" + chosenPolicyNo)  # deletes the policy from the
        # database where the entered policy number and primary key are the same
        connection.commit()
    except:
        print("Error- could not delete selected record.")


# Method - allows user to choose a policy to display from entering a policy number
def displayOnePolicy():
    print("---Display one---")
    chosenPolicyNo = str(getChosenPolicyNo())  # Calls method to get a chosen policy number off of the user and
    # stores it locally
    # Try/Except - if the policies cannot be fetched from the database, the code will not stop
    try:
        cursor.execute("SELECT *,oid FROM CarDetailsTable WHERE oid=" + chosenPolicyNo)  # Selects policy with
        # matching primary key
        policy = cursor.fetchall()  # Fetches all of the policies with matching policy numbers
        print(policy)  # Outputs policy
    except:
        print("Error- could not display selected record.")


# Method - allows all policies from the database to be displayed
def displayAllPolicies():
    print("---Display all Policies---")
    cursor.execute("SELECT *,oid FROM CarDetailsTable")  # Selects every policy from the database with * symbol
    policies = cursor.fetchall()  # Fetches all of the policies and stores them in a local variable
    # For Loop - repeats until every policy has been outputted
    for policy in policies:
        print(policy)


# Main Menu
exitProgram = False
choice = 0

# While loop - allows main menu to reappear after one action is completed
while not exitProgram:
    # Try/Except - in case the input is not in the correct format, the program will not break
    try:
        # Main Menu Display
        print("Menu: "
              "\n1- Add a New Insurance Policy"
              "\n2- Update a Policy"
              "\n3- Delete a Policy"
              "\n4- Display a Chosen Policy"
              "\n5- Display All Insurance Policies"
              "\n6- Exit")
        choice = int(input())
    # If the input is not in the correct format
    except:
        print("Input is not recognised, try again. Please enter a number between 1-5")

    if choice == 1:
        # Directs user to add a policy
        addPolicy()
    elif choice == 2:
        # Directs user to update a chosen policy
        updatePolicy()
    elif choice == 3:
        # Directs a user to delete a chosen policy
        deletePolicy()
    elif choice == 4:
        # Directs a user to display a chosen policy
        displayOnePolicy()
    elif choice == 5:
        # Directs a user to display all policies
        displayAllPolicies()
    elif choice == 6:
        # Allows the user to exit the program
        exitProgram = True
        connection.close()  # Closes connection to the database
    else:
        # If the input is a number but not one of the options, it will re-print the menu and allow the user to
        # re-enter a choice
        print("Input is not recognised.")