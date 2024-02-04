import os
class Register:
    userDetails = []

    def __init__(self, userName, password):
        self.userName = userName
        self.password = password
        self.registerUser(userName, password)

    def registerUser(self, userName, password):
        print("Success")
        self.userDetails.append(userName)
        self.userDetails.append(password)
# End of Class Register
        

# Functions
def validateUserName(userName):
        while True:
            if userName[0].isalpha():
                return userName
            else:
                userName = input("First Letter Must be an Alphabet. Retry : ")
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
                    password = input("Retry : ")
            else:
                print('''
Requirements of Password :
1) Minimum 8 Characters
2) At least 1 Upper Case
3) At least 1 Lower Case
4) At least 1 Digit Case
5) At least 1 Special Character from "@" and "$"
                    ''')
                password = input("Retry : ")
def mainMenu():
    while True:
        print('''
1 - Login
2 - About-us
3 - Exit
''')
        try:
            choice = int(input("Enter Choice: "))
        except ValueError:
            print("Invalid Choice.")
            choice = int(input("Enter Valid Choice: "))

        if choice == 1:
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
            ob = Register(userName, password)
            print(ob.userDetails)

        elif choice == 2:
            # Placeholder for the About-us section
            pass

        elif choice == 3:
            print("Thank You!!")
            break

# Start Of Program

mainMenu()
# os.mkdir("registeredUsers") - to make folder of registeredUsers.

