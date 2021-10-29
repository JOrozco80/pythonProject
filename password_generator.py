"""
This project encompasses the challenges of using arrays, and nesting loops within each other.
The first step is adding import random.
"""
import random

"""
The pool of characters that will make the password will be captured in String character, lowercase, uppercase, digits
and special characters.
"""
chars = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()/?,.<>+=`~'"

"""
When the program runs, it will generate a password from the selection of characters above. The next evolution for this 
project is to add foreign language letters using characters drawn from a translator pipeline. For now this project
will display passwords in English.
"""

"""
The first loop will be a main loop that will continuously run. This loop will ask for user input having them choose 
a number between 8 & 24 for password length and how many passwords the user wants. The user will; only be able to enter 
integers. If an invalid character is entered the user will be prompt to enter a "number" for either question.
"""


while 1:
    password_len = int(input("Choose a number between 8 & 24 : "))
    if password_len < 7:
        print("Password must have 8 characters minimum")
    elif password_len > 24:
        print("Password have a maximum of 24 characters")
    else:
        password_count = int(input("How many passwords would like generated? : "))
        # This part of the code runs the amount of password requested by the user.#
        for x in range(password_count):
            password = ""
            for x in range(password_len):
                password_char = random.choice(chars)
                password = password + password_char
                print("Here is your password: ", password)





'''Used the range start, stop, set method placing the values in the password_len and the reuslt 
has generatedpasswords at 16 characters in length.'''














