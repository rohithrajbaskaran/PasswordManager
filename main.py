import maskpass
import base64

def editMasterPassword():
    print ("")
    with open("masterPassword.txt", 'w') as file:
        file.write("")
    passwordEntered = maskpass.askpass(prompt="Enter new master password:\n", mask="*")
    file = open("masterPassword.txt", 'w')
    file.write(passwordEntered)
    print ("\nMaster password has been updated\n")

def viewPasswords():
    decodedString = ""
    password = open("passwords.txt", "r")
    print ("")
    for i in password:
        i = i[1:]
        decode = base64.b64decode(bytes(i, 'utf-8')).decode("utf-8")
        decodedString = decodedString + str(decode) + "\n"
    return decodedString

def editPasswords():
    pass

def addPasswords():
    command3 = input("\nEnter new information?\n")
    password = open("passwords.txt", "a")
    encode = base64.b64encode(command3.encode("utf-8"))
    password.write(str(encode) + "\n")
    password.close()
    print ("\nPassword has been added")

def removePasswords():
    command3 = input ("\nAre you sure you want to delete all your passwords?\n1. Yes\n2. No\n\n")
    while True:
        if command3 == "1":
            with open("passwords.txt", 'w') as file:
                file.write("")
            print ("\nAll passwords has been cleared\n")
            break
        elif command3 == "2":
            break
        else:
            print ("\nEnter a valid number\n")
            command3 = input ("\nAre you sure you want to delete all your passwords?\n1. Yes\n2. No\n\n")


passwordEntered = maskpass.askpass(prompt="Enter master password:\n", mask="*")

while True:
    password = open("masterPassword.txt", "r")

    if str(password.readline())==passwordEntered:

        command1 = input("\nWhat would you like to do? (Enter the number)\n1. View Passwords\n2. Edit Passwords\n3. Change master password\n4. Exit\n\n")
        
        if command1 == "1":
            print (viewPasswords())

        elif command1 == "2":
            print("")
            command2 = input ("Would you like to:\n1. Add\n2. Remove everything\n3. Change a password\n4. Return to main menu\n\n")
            while True:
                if command2 == "1":
                    addPasswords()
                    command2 = input ("\nWould you like to:\n1. Add\n2. Remove everything\n3. Change a password\n4. Return to main menu\n\n")
                elif command2 == "2":
                    removePasswords()
                    command2 = input ("\nWould you like to:\n1. Add\n2. Remove everything\n3. Change a password\n4. Return to main menu\n\n")
                elif command2 == "3":
                    editPasswords()
                    command2 = input ("\nWould you like to:\n1. Add\n2. Remove everything\n3. Change a password\n4. Return to main menu\n\n")
                elif command2 == "4":
                    break
                else:
                    print ("Enter a correct number")
                    command2 = input ("\nWould you like to:\n1. Add\n2. Remove everything\n3. Change a password\n4. Return to main menu\n\n")

        elif command1 == "3":
            editMasterPassword()

        elif command1 == "4":
            break
        
        else:
            print("\nPlease enter a correct number\n")

    else:

        print("\nIncorrect master password, please try again\n")
        passwordEntered = maskpass.askpass(prompt="Enter master password:\n", mask="*")

password.close()