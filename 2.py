import os

class Register:
    userDetails = []

    def __init__(self, userName, password, mobile=None, email=None, age=None):
        self.userName = userName
        self.password = password
        self.mobile = mobile
        self.email = email
        self.age = age
        self.registerUser(userName, password, mobile, email, age)

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

def login():
    while True:
        userName = input("Enter UserName: ")
        with open("registeredUsers\\registeredUserNames.txt", "r") as usernm_file:
            if userName in usernm_file.read():
                while True:
                    password = input("Enter Password: ")
                    if validateLogin(userName, password):
                        print("Login Successful")
                        break
                    else:
        #                 try:
        #     choice = int(input("Enter Choice: "))
        # except ValueError:
        #     print("Invalid Choice.")
        #     continue
                        print("Invalid Password.")
                        choice = int(input('''Press 1 - to enter the password again ,
2 - register , or
3 - go back to the main menu : ''' ))
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
                return True
    return False

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
    email = input("Enter Email: ")
    age = input("Enter Age: ")

    ob = Register(userName, password, mobile, email, age)

def mainMenu():
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
            login()
        elif choice == 2:
            register()
        elif choice == 3:
            # Placeholder for the About-us section
            pass
        elif choice == 4:
            print("Thank You!!")
            break
# End of Functions.



# Start Of Program
mainMenu()
# os.mkdir("registeredUsers")  # Uncomment if you want to create the 'registeredUsers' folder.

# flight