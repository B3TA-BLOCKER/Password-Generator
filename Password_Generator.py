# importing system libary
from os import system
# importing random Libary (for Random number,character and symbols generation)
import random

letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '_', '-', '+', '=', '[', ']', '{', '}', '|', '\\', ';', ':', ',', '.', '<', '>', '/', '?', '`', '~', "'", '"']

# clear screen
system('cls')
print("Welcome to the Password Generator!")

num_letter=int(input("How many letters would you like in your password?\n"))
num_symbols = int(input("How many symbols would you like?\n"))
num_numbers = int(input("How many numbers would you like?\n"))

password_list = []
for char in range(1,num_letter+1):
    password_list.append(random.choice(letters))

for char in range (1,num_symbols +1):
    password_list.append(random.choice(symbols))

for char in range (1,num_numbers+1):
    password_list.append(random.choice(numbers))

random.shuffle(password_list)

password = ""
for char in password_list:
    password += char

# Final Result.
print(f"Your Password is : {password}")
