import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n"))
nr_numbers = int(input("How many numbers would you like in your password?\n"))
nr_symbols = int(input("How many symbols would you like in your password?\n"))

password = []
sorted_password = []
for letter in range(0, nr_letters):
    generated_letter = letters[random.randint(0, len(letters) - 1)]
    password.append(generated_letter)

for number in range(0, nr_numbers):
    generated_number = numbers[random.randint(0, len(numbers) - 1)]
    password.append(generated_number)

for symbol in range(0, nr_symbols):
    generated_symbol = symbols[random.randint(0, len(symbols) - 1)]
    password.append(generated_symbol)

for character in range(0, len(password)):
    random_index = random.randint(0, len(password) - 1)
    sorted_password.append(password[random_index])
    password.pop(random_index)

final_password = ''
for char in sorted_password:
    final_password += char

print(final_password)
