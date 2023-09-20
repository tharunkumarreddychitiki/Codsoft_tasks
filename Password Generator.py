#Hello All I'm Tharun Kumar Reddy Chitiki 
# This is my third task in codsoft internship 
# This task is to write a python code to generate random passwords.

import random
import string

# Function to generate a random password
def generate_password(length):
    # Define characters to use for the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Check if the length is valid
    if length < 8:
        return "Password length must be at least 8 characters long for better security."

    # Generate the password using random.choices
    password = ''.join(random.choices(characters, k=length))

    return password

# Main program loop
while True:
    try:
        length = int(input("Enter the desired length of the password (at least 8): "))
        password = generate_password(length)
        print(f"Generated Password: {password}")
        break  # Exit the loop after generating and displaying the password
    except ValueError:
        print("Invalid input. Please enter a valid number for the password length.")
