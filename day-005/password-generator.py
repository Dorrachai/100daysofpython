import random

# Define character sets for password generation
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

# Introduce the password generator
print("This is a password generator. You will state yourself how many letters, numbers and symbols you want in your password.")

# Get user input for the number of each character type
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))

# Initialize an empty list to store the password characters
password_list = []

# Add random letters to the password list
for n in range(nr_letters):
    password_list.append(random.choice(letters))

# Add random symbols to the password list
for n in range(nr_symbols): 
    password_list.append(random.choice(symbols))

# Add random numbers to the password list
for n in range(nr_numbers):
    password_list.append(random.choice(numbers))

# Shuffle the characters in the password list
random.shuffle(password_list)

# Combine the characters in the password list into a single string
password = "".join(password_list)

# Display the generated password
print(f"Your generated password is: {password}")
