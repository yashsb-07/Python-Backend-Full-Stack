import random
import string 

def generate_password(length, use_digits, use_symbols):
    characters = string.ascii_letters

    if use_digits:
        characters += string.digits
    if use_symbols:
        characters += "!@#$%^&*"

    password = ""

    for i in range(length):
        password += random.choice(characters)

    return password
