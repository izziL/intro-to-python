# This is a list of the most common passwords from 2018.
commonPasswords = ["123456", "password", "123456789", "12345678", "12345", "111111", "1234567", "sunshine", "qwerty", "iloveyou", "princess", "admin", "welcome", "666666", "abc123", "football", "123123", "monkey", "654321", "!@#$%^&*", "charlie", "aa123456", "donald", "password1", "qwerty123"]

# This function will be called in passwordCheck(). It cleans the input.
def clean(x):
    return x.lower().strip()

# This function checks if the password is common. If it is common, the user will be prompted to enter a different password.
def passwordCheck():
    userPass = input("Please enter a password.")
    userPass = clean(userPass)

    if userPass in commonPasswords:
        print("The password that you inputted is a common password. Please enter a different password.")
        passwordCheck()
    else:
        print("The password that you entered is relatively uncommon!")

# Call the function.
passwordCheck()
