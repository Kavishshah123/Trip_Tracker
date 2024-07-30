import os
from datetime import datetime, timedelta
import re
import random
import time
import sys
class Register:
    userDetails = []

    def __init__(self, userName, password, mobile=None, email=None, age=None):
        self.userName = userName
        self.password = password
        self.mobile = mobile
        self.email = email
        self.age = age
        self.userFolder = os.path.join("registeredUsers", f"{userName}_data")

        os.makedirs(self.userFolder, exist_ok=True)

        user_trip_file = os.path.join(self.userFolder, "tripDetails.txt")
        with open(user_trip_file, "a"):
            pass

    def registerUser(self, userName, password, mobile, email, age):
        print("Registration Successful")
        user_details = {
            'username': userName,
            'password': password,
            'mobile': mobile,
            'email': email,
            'age': age
        }
        self.userDetails.append(user_details)

        with open("registeredUsers\\userDetails.txt", "a") as user_details_file:
            user_details_file.write(str(user_details) + "\n")


    def viewUpcomingTrips(self):
        user_trip_file = os.path.join(self.userFolder, "tripDetails.txt")
        current_datetime = datetime.now()

        with open(user_trip_file, "r") as trip_details_file:
            for line in trip_details_file:
                trip_data = line.strip().split("|")
                
                #destination and duration fetching
                destination = trip_data[1]
                duration = trip_data[2]

                # to get 9 nights format
                if "Nights" in duration and "Days" in duration:
                    num_nights = int(duration.split()[0])
                    start_date_str = (current_datetime + timedelta(days=num_nights)).strftime("%Y-%m-%d")
                else:
                    start_date_str = datetime.strptime(duration.split(" to ")[0], "%Y-%m-%d").strftime("%Y-%m-%d")

                if datetime.strptime(start_date_str, "%Y-%m-%d") > current_datetime:
                    print(f"Destination: {destination}, Start Date: {start_date_str}")


    
    def cancelTrip(self):
        while True:
            self.viewUpcomingTrips()
            
            while True:
                new_destination = input("Enter Destination to Cancel: ")
                if not new_destination:
                    print("Destination cannot be empty. Please enter a valid destination.")
                else:
                    break

            while True:
                new_start_date = input("Enter Start Date to Cancel (YYYY-MM-DD): ")
                try:
                    datetime.strptime(new_start_date, "%Y-%m-%d")
                    break  
                except ValueError:
                    print("Invalid date format. Please enter the date in the format YYYY-MM-DD.")

            trips = []
            user_trip_file = os.path.join(self.userFolder, "tripDetails.txt")
            found = False
            with open(user_trip_file, "r") as trip_details_file:
                for line in trip_details_file:
                    trip_data = line.strip().split("|")
                    trip_start_date = trip_data[2].split(" to ")[0] # get start date
                    if trip_data[1] == new_destination and trip_start_date == new_start_date:
                        print("Trip canceled successfully!")
                        found = True
                    else:
                        trips.append(line)

            if not found:
                print("No trip found with the specified destination and start date.")
            else:
                with open(user_trip_file, "w") as trip_details_file:
                    for trip in trips:
                        trip_details_file.write(trip)

            while True:
                choice = input("Do you want to cancel another trip? (yes/no): ").lower()
                if choice in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
            
            if choice == 'no':
                break
    def viewTripHistory(self):
        user_trip_file = os.path.join(self.userFolder, "tripDetails.txt")
        with open(user_trip_file, "r") as trip_details_file:
            for line in trip_details_file:
                trip_data = line.strip().split("|")
                print(f"Destination: {trip_data[1]}, Duration: {trip_data[2]}")

# End of Register Class
def validateUserName(userName):
    while True:
        if userName[0].isalpha():
            return userName
        else:
            userName = input("First Letter Must be an Alphabet. Retry: ")

def validatePassword(password):
    small, cap, dig, sp = 0, 0, 0, 0
    while True:
        if len(password) >= 8:
            for i in password:
                if i.isupper():
                    cap += 1
                if i.islower():
                    small += 1
                if i.isdigit():
                    dig += 1
                if i == "@" or i == "$":
                    sp += 1
            if cap >= 1 and small >= 1 and dig >= 1 and sp >= 1:
                return password
            else:
                print('''
Requirements of Password :
1) Minimum 8 Characters
2) At least 1 Upper Case
3) At least 1 Lower Case
4) At least 1 Digit Case
5) At least 1 Special Character from "@" and "$"
                ''')
                password = input("Retry: ")
        else:
            print('''
Requirements of Password :
1) Minimum 8 Characters
2) At least 1 Upper Case
3) At least 1 Lower Case
4) At least 1 Digit Case
5) At least 1 Special Character from "@" and "$"
                ''')
            password = input("Retry: ")
def validateMobile(mobile):
    while True:
        pattern = r'^\d{10}$'  

        if re.match(pattern, mobile):
            # print("Valid mobile number: ")
            return mobile
        else:
            print("Invalid mobile number. Please enter a 10-digit numeric mobile number.")
            mobile=input("Enter correct Mobile Number: ")
        
def validateEmail(email):
    while True:
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'

        if re.match(pattern, email):
            # print("Valid email address: ")
            return email
        else:
            print("Invalid email address. Please enter a valid email address.")
            email=input("Enter correct Email Id: ")
    
def validateAge(age):
    while True:
        try:
            if int(age) < 0:
                print("Age must be a non-negative integer.")
                age=input("Enter correct Age: ")
                
            elif int(age)>= 15:
                # print("You are eligible")
                return age
            else:
                print("You are not eligible")
                age=input("Enter correct Age: ")
        except ValueError:
            print("Invalid input, Age must be a whole number.")
            age=input("Enter correct Age: ")
def validateAadhar(aadhar):
     while True:
     
        pattern = r'^\d{12}$' 
        
        if re.match(pattern, aadhar):
            print("Valid Aadhar number.")
            return aadhar
        else:
            print("Invalid Aadhar number. Please enter a 12-digit Aadhar number without spaces or other characters.")
            aadhar=input("Enter Correct Aadhar Number: ")

def login():

    while True:
        userName = input("Enter UserName: ")
        with open("registeredUsers\\registeredUserNames.txt", "r") as usernm_file:
            if userName in usernm_file.read():
                while True:
                    password = input("Enter Password: ")
                    user = validateLogin(userName, password)
                    if user:
                        print("Login Successful!!")
                        tripMenu(user)
                        break
                    else:
                        print("Invalid Password.")
                        choice = int(input('''Press 1 - to enter the password again ,
2 - register , or
3 - go back to the main menu : '''))
                        if choice == 1:
                            continue
                        elif choice == 2:
                            register()
                            break
                        elif choice == 3:
                            break
                        else:
                            print("Invalid choice. Going back to the main menu.")
                            break
                break
            else:
                print("Username not found. Please try again.")

def validateLogin(userName, entered_password):
    with open("registeredUsers\\userDetails.txt", "r") as user_details_file:
        for line in user_details_file:
            user_details = eval(line)
            if user_details['username'] == userName and user_details['password'] == entered_password:
                user_instance = Register(
                    user_details['username'],
                    user_details['password'],
                    user_details.get('mobile'),
                    user_details.get('email'),
                    user_details.get('age')
                )
                return user_instance 
    return None


def register():
    flag_username = 0
    userName = input("Enter UserName: ")
    userName = validateUserName(userName)

    with open("registeredUsers\\registeredUserNames.txt", "a+") as usernm:
        usernm.seek(0)
        data = usernm.read()

        while flag_username != 1:
            if userName in data:
                print("Username already taken. Please try another username.")
                userName = input("Enter UserName: ")
                userName = validateUserName(userName)
            else:
                usernm.write(userName + "\n")
                usernm.flush()
                flag_username = 1

    password = input('''
Enter Password.
Requirements of Password :
1) Minimum 8 Characters
2) At least 1 Upper Case
3) At least 1 Lower Case
4) At least 1 Digit Case
5) At least 1 Special Character from "@" and "$"
    ''')
    password = validatePassword(password)

    mobile = input("Enter Mobile Number: ")
    mobile=validateMobile(mobile)

    email = input("Enter Email: ")
    email=validateEmail(email)

    age = input("Enter Age: ")
    age=validateAge(age)

    ob = Register(userName, password, mobile, email, age)
    ob.registerUser(userName, password, mobile, email, age)

def getIndianTrips():
    indian_trips_file = "IndianTrips.txt"
    trips = []

    if not os.path.isfile(indian_trips_file): # to check file exists
        with open(indian_trips_file, "w") as file:
            file.write("1|Manali|9 Nights/10 Days\n")
            file.write("2|Goa|4 Nights/5 Days\n")
            file.write("3|Jaipur|5 Nights/6 Days\n")
            file.write("4|Ooty|7 Nights/8 Days\n")
            file.write("5|Mumbai|2 Nights/3 Days\n")
            file.write("6|Shimla|6 Nights/7 Days\n")
            file.write("7|Kolkata|4 Nights/5 Days\n")
            file.write("8|Varanasi|4 Nights/5 Days\n")
            file.write("9|Agra|4 Nights/5 Days\n")
            file.write("10|Chennai|5 Nights/6 Days\n")

    with open(indian_trips_file, "r") as file:
        for line in file:
            trip_data = line.strip().split("|")
            trips.append(trip_data)

    return trips

def displayIndianTrips():
    print("Available Indian Trips:")
    trips = getIndianTrips()
    for trip in trips:
        print(f"{trip[0]}. Destination: {trip[1]}, Details: {trip[2]}")
        if trip[1] == "Manali":
            print('''
            Day 1: Arrival in Manali, check-in at the hotel, leisure time.
            Day 2: Explore Manali town, visit Hadimba Devi Temple and Manu Temple.
            Day 3: Excursion to Solang Valley, enjoy adventure activities like paragliding and zorbing.
            Day 4: Visit Rohtang Pass, enjoy snow activities (subject to weather conditions).
            Day 5: Day trip to Kullu, visit the famous Kullu Shawl Factory.
            Day 6: Visit Naggar Castle and Art Gallery, explore local markets.
            Day 7: Trek to Jogini Waterfalls, relax amidst nature.
            Day 8: Visit Vashisht Hot Water Springs and Old Manali.
            Day 9: Explore nearby villages like Malana or Kasol.
            Day 10: Departure from Manali.
''')
        elif trip[1] == "Goa":
            print('''
            Day 1: Arrival in Goa, check-in at the beach resort, leisure time.
            Day 2: Explore North Goa beaches like Baga, Calangute, and Anjuna.
            Day 3: Visit historic sites in Old Goa, including Basilica of Bom Jesus and Se Cathedral.
            Day 4: Explore South Goa beaches like Palolem and Agonda, visit Cabo de Rama Fort.
            Day 5: Departure from Goa.
''')

        elif trip[1] == "Jaipur":
            print('''
            Day 1: Arrival in Jaipur, check-in at the hotel, leisure time.
            Day 2: Visit Amber Fort, enjoy an elephant ride (optional), visit Jal Mahal and Hawa Mahal.
            Day 3: Explore City Palace, Jantar Mantar, and Albert Hall Museum.
            Day 4: Excursion to Nahargarh Fort and Jaigarh Fort, enjoy panoramic views of Jaipur.
            Day 5: Visit the famous markets of Jaipur for shopping.
            Day 6: Departure from Jaipur.
''')
        elif trip[1] == "Ooty":
            print('''
            Day 1: Arrival in Ooty, check-in at the hotel, leisure time.
            Day 2: Explore Ooty Botanical Gardens and Rose Garden.
            Day 3: Visit Doddabetta Peak for panoramic views of Nilgiri Hills.
            Day 4: Excursion to Coonoor, visit Sim's Park and Dolphin's Nose Viewpoint.
            Day 5: Enjoy a boat ride in Ooty Lake, visit Thread Garden.
            Day 6: Visit Pykara Lake and Falls, enjoy a scenic picnic.
            Day 7: Explore tea estates and chocolate factories in and around Ooty.
            Day 8: Departure from Ooty.
''')
        elif trip[1] == "Mumbai":
            print('''
            Day 1: Arrival in Mumbai, check-in at the hotel, leisure time.
            Day 2: Visit Gateway of India, Marine Drive, and Hanging Gardens.
            Day 3: Explore Elephanta Caves (optional), visit Siddhivinayak Temple, departure from Mumbai.
''')
        elif trip[1] == "Shimla":
            print('''
            Day 1: Arrival in Shimla, check-in at the hotel, leisure time.
            Day 2: Explore Mall Road, visit Christ Church and Scandal Point.
            Day 3: Excursion to Kufri, enjoy horse riding and skiing (seasonal).
            Day 4: Visit Jakhu Temple, enjoy panoramic views of Shimla.
            Day 5: Day trip to Chail, visit Chail Palace and Kali Ka Tibba.
            Day 6: Visit Mashobra and Naldehra, enjoy nature walks.
            Day 7: Departure from Shimla.
''') 
        elif trip[1] == "Kolkata":
            print('''
            Day 1: Arrival in Kolkata, check-in at the hotel, leisure time.
            Day 2: Explore Victoria Memorial, St. Paul's Cathedral, and Indian Museum.
            Day 3: Visit Dakshineswar Kali Temple and Belur Math.
            Day 4: Explore Howrah Bridge and Prinsep Ghat, enjoy a river cruise on Hooghly River.
            Day 5: Departure from Kolkata.
''')
        elif trip[1] == "Varanasi":
            print('''
            Day 1: Arrival in Varanasi, check-in at the hotel, leisure time.
            Day 2: Early morning boat ride on River Ganges, visit Kashi Vishwanath Temple and Sarnath.
            Day 3: Explore Varanasi Ghats, visit Assi Ghat and Dashashwamedh Ghat.
            Day 4: Visit Ramnagar Fort and Banaras Hindu University.
            Day 5: Departure from Varanasi.
''')        
        elif trip[1] == "Agra":
            print('''
            Day 1: Arrival in Agra, check-in at the hotel, leisure time.
            Day 2: Visit Taj Mahal at sunrise, explore Agra Fort and Itmad-ud-Daula.
            Day 3: Excursion to Fatehpur Sikri, visit Buland Darwaza and Jama Masjid.
            Day 4: Visit Mehtab Bagh for a view of the Taj Mahal at sunset, explore local markets.
            Day 5: Departure from Agra.
''')        
        elif trip[1] == "Chennai":
            print('''
            Day 1: Arrival in Chennai, check-in at the hotel, leisure time.
            Day 2: Visit Marina Beach, San Thome Cathedral, and Kapaleeshwarar Temple.
            Day 3: Explore Mahabalipuram, visit Shore Temple and Pancha Rathas.
            Day 4: Day trip to Kanchipuram, visit Ekambareswarar Temple and Kailasanathar Temple.
            Day 5: Visit Valluvar Kottam and Government Museum, explore local cuisine.
            Day 6: Departure from Chennai.
''')        
def displayAvailableFlights(destination, start_location):
    available_flights = []
    with open("flights.txt", "r") as flight_details_file:
        for line in flight_details_file:
            flight_data = line.strip().split("|")
            if flight_data[2] == destination:
                available_flights.append(flight_data)

    print(f"\nAvailable Flights from {start_location} to {destination}:")
    for idx, flight_data in enumerate(available_flights, start=1):
        print(f"{idx}. ID: {flight_data[0]}, {flight_data[1]} - {flight_data[4]}, Price: {flight_data[3]}")

    return available_flights

def displayAvailableTrains(destination, start_location):
    available_trains = []
    with open("trains.txt", "r") as train_details_file:
        for line in train_details_file:
            train_data = line.strip().split("|")
            if train_data[2] == destination:
                available_trains.append(train_data)

    print(f"\nAvailable Trains from {start_location} to {destination}:")
    for idx, train_data in enumerate(available_trains, start=1):
        print(f"{idx}. ID: {train_data[0]}, {train_data[1]} - {train_data[4]}, Price: {train_data[3]}")

    return available_trains

def generateRandomSeats():
    return random.randint(0, 120)

def collectPassengerDetails(total_passengers):
    passenger_details = {
        "name": [],
        "age": [],
        "phone": [],
        "email": [],
        "aadhar": []
    }
    

    for i in range(total_passengers):
        print(f"\nEnter details for Passenger {i + 1}:")
        passenger_name = input("Name: ")
        passenger_name=validateUserName(passenger_name)
        passenger_age = input("Age: ")
        passenger_age=validateAge(passenger_age)
        passenger_phone = input("Phone: ")
        passenger_phone=validateMobile(passenger_phone)
        passenger_email = input("Email: ")
        passenger_email=validateEmail(passenger_email)
        passenger_aadhar = input("Aadhar Number: ")
        passenger_aadhar=validateAadhar(passenger_aadhar)

        passenger_details["name"].append(passenger_name)
        passenger_details["age"].append(passenger_age)
        passenger_details["phone"].append(passenger_phone)
        passenger_details["email"].append(passenger_email)
        passenger_details["aadhar"].append(passenger_aadhar)

    return passenger_details

def make_payment_via_bank_card(total_amount, discount_percent=0, discounted_total=0):
    while True:
        # Display final amount to be paid
        if discount_percent > 0:
            print()
            print(f"Original Price: {total_amount}")
            print(f"Discount Applied: {discount_percent}%")
            print(f"Discounted Price: {discounted_total}")
        else:
            print()
            print(f"Total Amount: {total_amount}")
        print()
        print("Payment via Bank Card:")
        
        def validate_card_number(card_number):
            if len(card_number) != 12 or not card_number.isdigit():
                return False
            return True

        def validate_expiration_date(expiration_date):
            parts = expiration_date.split('/')
            if len(parts) != 2:
                return False
            month, year = parts
            if not (month.isdigit() and year.isdigit()):
                return False
            if not (1 <= int(month) <= 12):
                return False

            expiration_datetime = datetime(int(year), int(month), 1)

            today = datetime.today().replace(day=1)

            if expiration_datetime <= today:
                return False

            return True

        def validate_cvv(cvv):
            if len(cvv) != 3 or not cvv.isdigit():
                return False
            return True

        card_number = input("Enter your card number: ")
        expiration_date = input("Enter expiration date (MM/YYYY): ")
        cvv = input("Enter CVV: ")
        
        if not (validate_card_number(card_number) and 
                validate_expiration_date(expiration_date) and 
                validate_cvv(cvv)):
            print("Invalid input. Please enter valid card details.")
            continue  
        print("Processing payment...")
        time.sleep(2)  
        print("Payment successful! Enjoy Your Trip!!")
        break

def make_payment_via_upi(total_amount, discount_percent=0, discounted_total=0):
    while True:

        if discount_percent > 0:
            print()
            print(f"Original Price: {total_amount}")
            print(f"Discount Applied: {discount_percent}%")
            print(f"Discounted Price: {discounted_total}")
        else:
            print()
            print(f"Total Amount: {total_amount}")
        print()
        print("Payment via UPI:")
        
        def validate_upi_id(upi_id):
            if "@" not in upi_id:
                return False
            
            username, domain = upi_id.split("@")
            if not (username and domain):
                return False
            
            if len(username) < 3 or len(username) > 64:
                return False
            if len(domain) < 3 or len(domain) > 255:
                return False
            
            return True

        upi_id = input("Enter your UPI ID: ")
        
        if validate_upi_id(upi_id):
            break
        else:
            print("Invalid input. Please enter a valid UPI ID.")
    
    print("Processing payment...")
    print("Payment successful! Enjoy Your Trip!!")
    

def make_payment_via_phonepe(total_amount, discount_percent=0, discounted_total=0):
    while True:
        if discount_percent > 0:
            print()
            print(f"Original Price: {total_amount}")
            print(f"Discount Applied: {discount_percent}%")
            print(f"Discounted Price: {discounted_total}")
        else:
            print()
            print(f"Total Amount: {total_amount}")
        print()
        print("Payment via PhonePe:")
        
        def validate_phonepe_number(phonepe_number):
            if len(phonepe_number) != 10 or not phonepe_number.isdigit():
                return False
            return True

        phonepe_number = input("Enter your PhonePe number: ")
        
        # Validate the input
        if not validate_phonepe_number(phonepe_number):
            print("Invalid input. Please enter a valid PhonePe number.")
            continue  
        print("Processing payment...")
        time.sleep(2) 
        print("Payment successful! Enjoy your Trip!!")
        break

def make_payment_via_internet_banking(total_amount, discount_percent=0, discounted_total=0):
    while True:
        if discount_percent > 0:
            print()
            print(f"Original Price: {total_amount}")
            print(f"Discount Applied: {discount_percent}%")
            print(f"Discounted Price: {discounted_total}")
        else:
            print()
            print(f"Total Amount: {total_amount}")
        print()
        print("Payment via Internet Banking:")
        
        def validate_bank_account_number(account_number):
            if len(account_number) != 10 or not account_number.isdigit():
                return False
            return True

        account_number = input("Enter your bank account number: ")
        
        if not validate_bank_account_number(account_number):
            print("Invalid input. Please enter a valid bank account number.")
            continue  
        
        print("Processing payment...")
        time.sleep(2)
        print("Payment successful! Enjoy Your Trip!!")
        break
        

def displayAvailableHotels(destination):
    available_hotels = []
    with open("hotels.txt", "r") as hotel_details_file:
        for line in hotel_details_file:
            hotel_data = line.strip().split("|")
            if hotel_data[1] == destination:
                available_hotels.append(hotel_data)

    print(f"\nAvailable Hotels in {destination}:")
    for idx, hotel_data in enumerate(available_hotels, start=1):
        print(f"{idx}. ID: {hotel_data[0]}, Hotel Name: {hotel_data[2]}, Stars: {hotel_data[3]}, Price Per Night: {hotel_data[4]}")

    return available_hotels

def generate_bill(user, trip_package, trip_details, total_amount, discount_percent=0, discounted_total=0, coupon_name="",book_hotel_choice="no",Hotel_Details=None,total_hotel_amount=0, payment_option=""):
    trip_start_date = trip_details.split("|")[2].split()[0]
    bill_filename = f"{trip_package}_{trip_start_date}_Bill.txt"
    
    # Split trip_details by '|'
    trip_info = trip_details.split("|")[:-1] 
    
    # Extract trip details
    user_name, destination, date_range, passengers = trip_info[:4]
    transport_details = trip_info[4] if len(trip_info) > 4 else ""

    passengers = passengers.split(":")[1].strip()
    flight_details = ""
    train_details = ""
    if transport_details:
        if "Flight" in transport_details:
            flight_details = transport_details.strip()[0:-1].replace(',', '\n').replace('{', '').replace('}', '')
        else:
            train_details = transport_details.strip()[0:-1].replace(',', '\n').replace('{', '').replace('}', '')
   
    bill_content = ""
    bill_content += "****************************************************\n"
    bill_content += "*                  Trip Booking Bill               *\n"
    bill_content += "****************************************************\n"
    bill_content += f"User Name: {user_name}\n"
    bill_content += "----------------------------------------------------\n"
    bill_content += f"Destination: {destination}\n"
    bill_content += "----------------------------------------------------\n"
    bill_content += f"Date Range: {date_range}\n"
    bill_content += "----------------------------------------------------\n"
    # bill_content += f"Passengers: {passengers}\n"
    bill_content += "****************************************************\n"
    bill_content += "Transport Details:\n"
    if flight_details:
        bill_content += "Flight Details:\n"
        bill_content += f"{flight_details}\n"
        bill_content += "----------------------------------------------------\n"
    elif train_details:
        bill_content += "Train Details:\n"
        bill_content += f"{train_details}\n"
        bill_content += "----------------------------------------------------\n"
    bill_content += "****************************************************\n"
    if book_hotel_choice == "yes":
        bill_content += "Hotel Details:\n"
        for id,hotel_detail in Hotel_Details.items():
            bill_content += (f"{id} : {hotel_detail}\n")
        bill_content+=(f"Total Hotel Amount : {total_hotel_amount}\n")
    else:
        bill_content += "Hotel Details:\n"
        hotel_detail = "No hotel booked"
    bill_content += "****************************************************\n"
    bill_content += "----------------------------------------------------\n"
    bill_content += f"Total Amount: Rs. {total_amount:.2f}\n"
    if coupon_name != "":
        bill_content += "Coupon Details:\n"
        bill_content += f"Coupon Name: {coupon_name}\n"
        # bill_content += f"Discount Percent: {coupon_discount_percen}%\n"
    if discount_percent > 0:
        bill_content += "----------------------------------------------------\n"
        bill_content += f"Discount Applied: {discount_percent}%\n"
        bill_content += f"Discounted Final Price: Rs. {discounted_total:.2f}\n"
    bill_content += "****************************************************\n"
    bill_content += f"Payment Option: {payment_option}\n"
    bill_content += "****************************************************\n"

    bill_path = os.path.join(user.userFolder, bill_filename)
    with open(bill_path, "w") as bill_file:
        bill_file.write(bill_content)
    
    print(f"Bill generated successfully at: {bill_path}")

def bookHotel(user, destination, total_passengers):
    print(f"\nBooking a hotel for your trip to {destination}:\n")

    while True:
        available_hotels = displayAvailableHotels(destination)

        try:
            selected_hotel_idx = int(input("Enter the number corresponding to the desired hotel: ")) - 1
            
            if selected_hotel_idx < 0 or selected_hotel_idx >= len(available_hotels):
                print("Invalid hotel number. Please enter a number within the range.")
                continue  
            
            selected_hotel = available_hotels[selected_hotel_idx]
            print(f"\nSelected Hotel: {selected_hotel[2]}, Stars: {selected_hotel[3]}, Price Per Night: {selected_hotel[4]}")

           
            num_rooms_required = (total_passengers + 3) // 4  
            hotel_booking_details = {
                "ID": selected_hotel[0],
                "Name": selected_hotel[2],
                "Stars": selected_hotel[3],
                "PricePerNight": float(selected_hotel[4]),
                "Rooms": num_rooms_required
            }

            print("Hotel booked successfully!")
                
            return hotel_booking_details

        except ValueError:
            print("Invalid input. Please enter a valid number.")
            continue 

def getIndianTripDetails(trip_id):
    trips = getIndianTrips()
    for trip in trips:
        if int(trip[0]) == trip_id:
            return trip[1], trip[2]
    return None, None

def tripMenu(user):


    while True:
        print('''
1 - Plan a Trip
2 - View Upcoming Trips
3 - Cancel a Trip
4 - View Trip History
5 - View Available Indian Trips
6 - Logout
''')
        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid Choice. Please enter a valid integer choice.")
            continue

        if choice == 1:
            planTripWithStartDate(user)
        elif choice == 2:
            user.viewUpcomingTrips()
        elif choice == 3:
            user.cancelTrip()
        elif choice == 4:
            user.viewTripHistory()
        elif choice == 5:
            displayIndianTrips()
        elif choice == 6:
            print("Logging out. Have a great day!")
            sys.exit(1)
        else:
            print("Invalid choice. Please enter a valid option.")
def about_us():
    print('''
    Welcome to Trip-Tracker!

    At Trip-Tracker, we're passionate about simplifying your travel experiences. Our platform is designed to make planning, managing, and enjoying your trips effortless and enjoyable. Whether you're embarking on a solo adventure, a family vacation, or a business trip, Trip-Tracker is here to be your trusted companion every step of the way.
    ''')
    print('''
    Our Mission:
          
    Our mission at Trip-Tracker is to empower travelers like you to explore the world with confidence and ease. We believe that travel has the power to enrich lives, create unforgettable memories, and foster connections between people and cultures. Our goal is to provide you with the tools and resources you need to make every trip a success.
    ''')
    print('''
        
    What Sets Us Apart:

    User-Focused Design: We prioritize user experience above all else. Our platform is intuitive, user-friendly, and tailored to meet the needs of modern travelers. From seamless booking to personalized recommendations, we're dedicated to making your journey as smooth as possible.

    Comprehensive Features: With Trip-Tracker, you have everything you need in one place. Plan your itinerary, book flights and accommodations, track expenses, and share memories with ease. Our comprehensive features streamline the travel process, so you can focus on what matters most – enjoying your trip.

    Commitment to Excellence: We're committed to delivering excellence in everything we do. Our team of travel enthusiasts is constantly innovating, refining, and improving our platform to ensure that you have the best possible experience. Your satisfaction is our driving force.
    ''')
    print('''
        
    Our Team:

    Meet the passionate individuals behind Trip-Tracker. Our team brings together a diverse range of expertise, from software development and design to travel industry knowledge and customer support. Together, we're dedicated to helping you make the most of your travel adventures.

    ''')
    print('''
        
    Get in Touch:

    Have questions, feedback, or ideas for improvement? We'd love to hear from you! Your input helps us continually enhance Trip-Tracker to better serve your needs. Don't hesitate to reach out to us via email, social media, or our online support channels.

    ''')
    print('''
        
    Join Our Community:

    Connect with fellow travelers, share tips and stories, and stay up-to-date on the latest travel trends by joining the Trip-Tracker community. Follow us on social media and subscribe to our newsletter to be part of the journey.

    ''')
    print('''
        
    Thank You for Choosing Trip-Tracker:

    We're grateful for the opportunity to be part of your travel experiences. Thank you for choosing Trip-Tracker as your trusted travel companion. Here's to many more adventures together!

    ''')
def mainMenu():
    print(" " * 20 + "╔══════════════════════╗")
    print(" " * 20 + "║     Trip-Tracker     ║")
    print(" " * 20 + "╚══════════════════════╝")

    while True:
        print('''
1 - Login
2 - Register
3 - About-us
4 - Exit
''')
        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid Choice.")
            continue

        if choice == 1:
            user = login()
            if user:
                tripMenu(user) 
        elif choice == 2:
            register()
        elif choice == 3:
            about_us()
        elif choice == 4:
            print("Thank You!!")
            break
def planTripWithStartDate(user):
    while True:
        try:
            displayIndianTrips()
            try:
                trip_id = int(input("Enter the ID of the trip you want to plan: "))
            except ValueError:
                print("Invalid input for trip ID.")
                continue
            
            destination, duration = getIndianTripDetails(trip_id)
            if destination and duration:
                num_days = int(duration.split()[0])

                try:
                    start_date = input("Enter the start date of the trip (YYYY-MM-DD): ")
                    start_datetime = datetime.strptime(start_date, "%Y-%m-%d")
                except ValueError:
                    print("Invalid input for start date.")
                    continue

                current_datetime = datetime.now()
                if (start_datetime - current_datetime).days < 7:
                    print("Invalid start date. Minimum 7 days gap required.")
                    return

                end_datetime = start_datetime + timedelta(days=num_days)
                end_date = end_datetime.strftime("%Y-%m-%d")

                while True:
                    try:
                        book_transport = input("Do you want to book a flight or train? ").lower()
                        if book_transport != "flight" and book_transport != "train":
                            print("Invalid Input")
                            continue
                        else:
                            break
                    except ValueError:
                        print("Invalid input for booking transport.")
                        continue

                formatted_trip_details = ""
                if book_transport == "flight":
                    start_location = input("Enter your start location: ")
                    available_flights = displayAvailableFlights(destination, start_location)

                    try:
                        selected_flight_idx = None
                        while selected_flight_idx is None:
                            try:
                                selected_flight_idx = int(input("Enter the number corresponding to the desired flight: ")) - 1
                                if selected_flight_idx < 0 or selected_flight_idx >= len(available_flights):
                                    print("Invalid flight number. Please enter a number within the range.")
                                    selected_flight_idx = None
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")
                                selected_flight_idx = None

                        selected_flight = available_flights[selected_flight_idx]
                        print()
                        print(f"Selected Flight: {selected_flight[1]} - {selected_flight[4]}, Price: {selected_flight[3]}")

                        available_seats = generateRandomSeats()
                        print(f"Available Seats: {available_seats}")

                        total_passengers = None
                        while total_passengers is None:
                            try:
                                total_passengers = int(input("Enter the total number of passengers: "))
                                if total_passengers <= 0:
                                    print("Invalid input. Please enter a positive number of passengers.")
                                    total_passengers = None
                                elif total_passengers > available_seats:
                                    print("Not enough available seats. Please enter a lower number of passengers.")
                                    total_passengers = None
                            except ValueError:
                                print("Invalid input. Please enter a valid number.")

                        passenger_details = collectPassengerDetails(total_passengers)

                        formatted_passenger_details = {
                            "Name": passenger_details["name"],
                            "Age": passenger_details["age"],
                            "Phone": passenger_details["phone"],
                            "Email": passenger_details["email"],
                            "Aadhar": passenger_details["aadhar"]
                        }

                        formatted_trip_details = f"Flight:{{ID:{selected_flight[0]}, Name:{selected_flight[1]}, Date:{start_date}, Time:{selected_flight[4]}, Price:{selected_flight[3]}, Passengers:{total_passengers}, PassengerDetails:{formatted_passenger_details}, TotalPrice:{float(selected_flight[3]) * total_passengers:.2f}}}|Train: Null"

                    except (ValueError, IndexError):
                        print("Invalid input. Flight booking aborted.")

                elif book_transport == "train":
                    start_location = input("Enter your start location: ")
                    available_trains = displayAvailableTrains(destination, start_location)

                    while True:
                        try:
                            selected_train_idx = int(input("Enter the number corresponding to the desired train: ")) - 1

                            if 0 <= selected_train_idx < len(available_trains): 
                                selected_train = available_trains[selected_train_idx]
                                print(f"Selected Train: {selected_train[1]} - {selected_train[4]}, Price: {selected_train[3]}")

                                available_seats = generateRandomSeats()
                                print(f"Available Seats: {available_seats}")

                                total_passengers = int(input("Enter the total number of passengers: "))
                                
                                if total_passengers > available_seats:
                                    print("Not enough available seats. Train booking aborted.")
                                    return

                                passenger_details = collectPassengerDetails(total_passengers)

                                formatted_passenger_details = {
                                    "Name": passenger_details["name"],
                                    "Age": passenger_details["age"],
                                    "Phone": passenger_details["phone"],
                                    "Email": passenger_details["email"],
                                    "Aadhar": passenger_details["aadhar"]
                                }

                                formatted_trip_details = f"Train:{{ID:{selected_train[0]}, Name:{selected_train[1]}, Date:{start_date}, Time:{selected_train[4]}, Price:{selected_train[3]}, Passengers:{total_passengers}, PassengerDetails:{formatted_passenger_details}, TotalPrice:{float(selected_train[3]) * total_passengers:.2f}}}|Flight: Null"

                                break  

                            else:
                                print("Invalid train choice. Please enter a number within the given range.")

                        except ValueError:
                            print("Invalid input. Please enter a valid number.")

                        except IndexError:
                            print("Invalid train choice. Please enter a number within the given range.")

                book_hotel_choice = input("Do you want to book a hotel for this trip? (yes/no): ").lower()
                if book_hotel_choice == "yes":
                    Hotel_Details = bookHotel(user, destination, total_passengers)
                elif book_hotel_choice == "no":
                    Hotel_Details = None
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")
                    while True:
                        book_hotel_choice = input("Do you want to book a hotel for this trip? (yes/no): ").lower()
                        if book_hotel_choice == "yes":
                            Hotel_Details = bookHotel(user, destination, total_passengers)
                            break
                        elif book_hotel_choice == "no":
                            Hotel_Details = None
                            break
                        else:
                            print("Invalid input. Please enter 'yes' or 'no'.")

                trip_details = f"{user.userName}|{destination}|{start_date} to {end_date}|Travelers: {', '.join(passenger_details)}|{formatted_trip_details}"

                if Hotel_Details:
                    trip_details += f"|Booked_Hotel:{Hotel_Details}"

                total_hotel_amount = 0
                if Hotel_Details:
                    hotel_price_per_night = float(Hotel_Details['PricePerNight'])
                    num_rooms_required = (total_passengers + 3) // 4
                    total_hotel_amount = hotel_price_per_night * num_rooms_required * num_days
                    print()
                    print("Total Hotel Amount:", total_hotel_amount)

                if book_transport == "flight":
                    total_flight_amount = float(selected_flight[3]) * total_passengers
                    total_train_amount = 0
                    print("Total Flight Amount:", total_flight_amount)
                elif book_transport == "train":
                    total_train_amount = float(selected_train[3]) * total_passengers
                    total_flight_amount = 0
                    print("Total Train Amount:", total_train_amount)

                total_amount = total_hotel_amount + total_flight_amount + total_train_amount
                print()
                print("Grand Total :", total_amount)

                discount_coupons = {
                    "ADVENTUREPLUS10": 10,
                    "EXPLOREMORE12": 12,
                    "JOURNEYWISE15": 15,
                    "ROAMFREE18": 18,
                    "DISCOVERNOW20": 20,
                    "WANDERWELL22": 12,
                    "TOURTALES25": 15,
                    "TRAVELBLISS28": 9,
                    "ADVENTUREQUEST30": 10,
                    "WORLDWANDER32": 12,
                    "EXPLOREXPRESS35": 5,
                    "VOYAGEPLUS38": 18,
                    "TRAVELADORN40": 11,
                    "ROAMRICH42": 17,
                    "DISCOVERDREAM45": 8,
                }

                selected_coupons = random.sample(list(discount_coupons.keys()), 5)
                print("Available Coupons:")
                for idx, coupon in enumerate(selected_coupons, start=1):
                    print(f"{idx}. {coupon} - {discount_coupons[coupon]}% off")

                is_coupon_applied = False
                coupon_name = ""
                discount_percent = 0
                discounted_total = 0

                while True:
                    try:
                        use_coupon = input("Do you want to use any coupon? (yes/no): ").lower()
                        if use_coupon == "yes":
                            coupon_choice = int(input("Enter the number corresponding to the desired coupon: "))

                            if 1 <= coupon_choice <= len(selected_coupons):
                                selected_coupon = selected_coupons[coupon_choice - 1]
                                discount_percent = discount_coupons[selected_coupon]
                                discount_amount = total_amount * (discount_percent / 100)
                                discounted_total = total_amount - discount_amount
                                print(f"Discount Applied using {selected_coupon}: {discount_percent}% off")
                                print(f"Discounted Total Amount: {discounted_total}")
                                is_coupon_applied = True
                                coupon_name = selected_coupon
                                break
                            else:
                                print("Invalid coupon choice. Please enter a number within the given range.")

                        elif use_coupon == "no":
                            print("No coupon used. Proceeding with the original total amount.")
                            break

                        else:
                            print("Invalid input. Please enter 'yes' or 'no'.")

                    except ValueError:
                        print("Invalid input. Please enter a valid number for coupon selection.")

                is_coupon_applied_str = "True" if is_coupon_applied else "False"
                user_trip_file = os.path.join(user.userFolder, "tripDetails.txt")
                with open(user_trip_file, "a") as user_trip_details_file:
                    user_trip_details_file.write(f"{trip_details}|Flight_Price:{total_flight_amount}|Train_Price:{total_train_amount}|Hotel_Price:{total_hotel_amount}|Grand_Total:{total_amount}|Is_Coupon_Applied:{is_coupon_applied_str}|Coupon_Name:{coupon_name}|Discount_Percent:{discount_percent}|Discounted_Final_Price:{discounted_total}\n")

                print()
                print("Choose a payment option:")
                print("1. Bank Card")
                print("2. UPI")
                print("3. PhonePe")
                print("4. Internet Banking")

                while True:
                    option = input("Enter your choice (1-4): ")
                    if option not in ['1', '2', '3', '4']:
                        print("Invalid choice. Please enter a number between 1 and 4.")
                    else:
                        if option == '1':
                            print("You have chosen to pay via Bank Card.")
                            make_payment_via_bank_card(total_amount, discount_percent, discounted_total)
                            generate_bill(user, destination, trip_details, total_amount, discount_percent, discounted_total, coupon_name, book_hotel_choice, Hotel_Details, total_hotel_amount, "Bank Card")
                            return
                        elif option == '2':
                            print("You have chosen to pay via UPI.")
                            make_payment_via_upi(total_amount, discount_percent, discounted_total)
                            generate_bill(user, destination, trip_details, total_amount, discount_percent, discounted_total, coupon_name, book_hotel_choice, Hotel_Details, total_hotel_amount, "UPI")
                            return
                        elif option == '3':
                            print("You have chosen to pay via PhonePe.")
                            make_payment_via_phonepe(total_amount, discount_percent, discounted_total)
                            generate_bill(user, destination, trip_details, total_amount, discount_percent, discounted_total, coupon_name, book_hotel_choice, Hotel_Details, total_hotel_amount, "PhonePe")
                            return
                        else:
                            print("You have chosen Internet Banking")
                            make_payment_via_internet_banking(total_amount, discount_percent, discounted_total)
                            generate_bill(user, destination, trip_details, total_amount, discount_percent, discounted_total, coupon_name, book_hotel_choice, Hotel_Details, total_hotel_amount, "Internet Banking")
                            return
            else:
                print("Invalid trip ID. Please select a valid ID.")
        except ValueError:
            print("Invalid input.")

# End of Functions.


# Start Of Program
mainMenu()
