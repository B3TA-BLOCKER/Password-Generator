# Password-Generator

This Python code is a password generator program. Here's a step-by-step description of what the code does:

from os import system: This line imports the system function from the os module. The system function is used to run operating system commands.

import random: This line imports the random module, which is used to generate random numbers and make selections from lists randomly.

Three lists are defined:

letters: Contains uppercase and lowercase letters of the alphabet.
numbers: Contains digits from 0 to 9.
symbols: Contains a variety of special symbols.
system('cls'): This line clears the console screen. It's commonly used in Windows systems to clear the command prompt or terminal window.

The program prints a welcome message to the user.

It then prompts the user to input the following:

num_letter: The number of letters to include in the password.
num_symbols: The number of symbols to include in the password.
num_numbers: The number of numbers to include in the password.
An empty list password_list is initialized to store the characters of the password.

Three loops are used to randomly select characters for the password:

The first loop adds random letters to password_list according to the user-specified num_letter.
The second loop adds random symbols to password_list according to the user-specified num_symbols.
The third loop adds random numbers to password_list according to the user-specified num_numbers.
After all the characters are added to password_list, the random.shuffle() function is used to shuffle the characters randomly.

The shuffled characters in password_list are concatenated together to form the final password, stored in the password variable.

The program prints the generated password to the user.

In summary, this code generates a random password based on user-defined criteria for the number of letters, symbols, and numbers to include in the password. It then displays the generated password to the user.
