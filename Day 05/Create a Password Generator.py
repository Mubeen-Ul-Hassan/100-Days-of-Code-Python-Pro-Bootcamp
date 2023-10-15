import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input("How many symbols would you like?\n"))
nr_numbers = int(input("How many numbers would you like?\n"))

# Password variable to store random generate letters, symbols, and numbers.
password = ''

# To generate letters from letters variable
for counter_1 in  range(0, nr_letters):
    random_letter = random.choice(letters)
    password += random_letter

# To generate symbol from symbols variable
for counter_2 in range(0, nr_symbols):
    random_symbol = random.choice(symbols)
    password += random_symbol

# To generate number from numbers variable
for counter_2 in range(0, nr_numbers):
    random_number = random.choice(numbers)
    password += random_number


print(f"Here is your password: {password}")
