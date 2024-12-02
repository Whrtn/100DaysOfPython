import string
import random

letters = string.ascii_letters
numbers = string.digits
special_chars = string.punctuation
selection_list = letters + numbers + special_chars


def generatePasswords():
    num_of_passwords = int(input("How many passwords would you like?"))
    password_length = int(input("How long should the passwords be?"))

    for i in range(num_of_passwords):
        password = ''
        for i in range(password_length):
            password += ''.join(random.choice(selection_list))
        print(password)

generatePasswords()

        


