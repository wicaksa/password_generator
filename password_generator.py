#Password Generator Project

import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '22', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters = int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

print (letters[random.randint(0, len(letters)-1)])
user_generated_password = ''

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91

### Start Eazy Level ########

# Input: integers that show how many of each items the user wants in their password.
# Output: String that is randomly created from a list of items. 

# Psuedocode: 
# Create an empty string.
# Iterate from (0, nr_letters) and randomly add a letter to the list. 
# Iterate from (0, nr_symbols) and randomly add a symbol to the list. 
# Iterate from (0, nr_numbers) and randomly add a number to the list. 
# Print the string.

# # Add random letters.
# for letter in range(0, nr_letters):
#     # Generate a random letter from letter[] and add it into user_generated_password
#     random_letter = letters[random.randint(0, len(letters)-1)]
#     user_generated_password += random_letter
#     print(user_generated_password)
# # Add random symbols. 
# for symbol in range(0, nr_symbols):
#     random_symbol = symbols[random.randint(0, len(symbols)-1)]
#     user_generated_password += random_symbol
# # Add random numbers.
# for number in range(0, nr_numbers):
#     random_number = numbers[random.randint(0, len(numbers)-1)]
#     user_generated_password += random_number
# # Print the list to show the randomly generated password.
# print(f"Your new password is {user_generated_password}.")

### End Eazy Level ###


#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

# Iterate from 0 to the total length of symbols, numbers, and letters.
# At each index, randomly choose either letter, symbol, or number before concatenating the string.
# Print the string at the end. 

# Find the total length of the string password.
total_length = nr_letters + nr_symbols + nr_numbers 

for index in range (0, total_length):
    random_digit = random.randint(0,2)
    if random_digit == 0: # Add letter
        random_letter = letters[random.randint(0, len(letters)-1)]
        user_generated_password += random_letter
    elif random_digit == 1: # Add Symbol
        random_symbol = symbols[random.randint(0, len(symbols)-1)]
        user_generated_password += random_symbol
    else: # Add number.
        random_number = numbers[random.randint(0, len(numbers)-1)]
        user_generated_password += random_number 
print(f"Your new password is: {user_generated_password} .")

### End Hard Level ###
