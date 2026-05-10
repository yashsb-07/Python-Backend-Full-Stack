"""Level 1"""

# Project First 

# name = input("Enter your name: ")
# birth_year = int(input("Enter your birth year: "))

# current_year = 2026
# age = current_year - birth_year

# print(f"\nHello {name}!")
# print(f"You are {age} years old.")

# if age < 0:
#     print("Invalid birth year entered.")
# elif age < 18:
#     print("Category: Minor")
# elif age <= 60:
#     print("Category: Adult")
# else:
#     print("Category: Senior Citizen")

#Project Second

# num = int(input("Enter a number: "))

# if num < 0:
#     print("Number is negative.")

# if num % 2 == 0:
#     print("Num is even.")
#     if num % 5 == 0:
#         print("Number is devisible of 5.")
# else:
#     print("Num is odd.")

#     if num % 5 == 0:
#         print("Number is devisible of 5")

#Project Third

# username = "admin"
# password = "1234"

# username1 = input("Enter your username: ")
# password1 = input("Enter your password: ")

# if username == username1 and password == password1:
#     print("Access Granted..!")
# else:
#     print("Access Denied..!")

#Project Four

# product_price = int(input("Enter your product price: "))

# if product_price < 0:
#     print("Invalid product price.")
# else:
#     if product_price > 500:
#         discount_price = product_price * 20 / 100
#     elif product_price >= 200:
#         discount_price = product_price * 10 / 100
#     else:
#         discount_price = 0

#     final_price = product_price - discount_price

#     print(f"Original price is {product_price:.2f}")
#     print(f"Discount price is {discount_price:.2f}")
#     print(f"Final price is {final_price:.2f}")

#Project Five

# sentence = input("Enter your sentence here: ")

# if sentence.strip() == "":
#     print("The sentence is empty")
# else: 
#     print(f"Length of string is {len(sentence)}")
#     print(f"Uppercase: {sentence.upper()}")
#     print(f"Lowercase: {sentence.lower()}")
    
#     if "python" in sentence.lower():
#         print("The sentence conatins name python.")
#     else:
#         print("The sentence not contains name python.")

"""Level 2"""

#Project 1

# balance = 10000
# amt = float(input("Enter amount to withdraw: "))

# if amt <= 0:
#     print("Invalid amount!")
# elif amt > balance:
#     print("Insufficient funds!")
# else:
#     balance -= amt
#     print("\nTransaction Successful!")
#     print(f"Withdrawn: ₹{amt:.2f}")
#     print(f"Remaining Balance: ₹{balance:.2f}")

#Project 2

# secret_number = 7
# user_num = int(input("Enter your guess: "))

# print("\nChecking your guess...\n")

# if user_num > secret_number:
#     print("Too high! Try again.")
# elif user_num < secret_number:
#     print("Too low! Try again.")
# else:
#     print("Congratulations! You won!")

#Project 3

# first_num = int(input("Enter your first number here: "))
# operator = input("Enter your operator here: ")
# second_num = int(input("Enter your second number here: "))

# if operator == "+":
#     print(first_num + second_num)
# elif operator == "-":
#     print(first_num - second_num)
# elif operator == "*":
#     print(first_num * second_num)
# elif operator == "/":
#     if second_num != 0:
#         print(first_num / second_num)
#     else:
#         print("The number is not devisible by 0.")
# else:
#     print("Invalid operator..!")

#Project 4

# marks = int(input("Enter your marks: "))

# if marks < 0 or marks > 100:
#     print("Invalid marks entered.")
# else:
#     if marks >= 90:
#         grade = "A"
#     elif marks >= 75:
#         grade = "B"
#     elif marks >= 50:
#         grade = "C"
#     else:
#         grade = "Fail"

#     print(f"Grade: {grade}")

#Student Eligibility System

# name = input("Enter you name here: ")
# age = int(input("Enter your age: "))
# marks = float(input("Enter your marks: "))
# attendance = int(input("Enter your attendance: "))

# if age <= 0 or marks < 0 or marks > 100 or attendance < 0 or attendance > 100:
#     print("Invalid input entered.")
# else: 
#     if age >= 18 and marks >=60 and attendance >=75:
#         print(f"Congratulations {name} you are eligible.")
#     else:
#         print(f"Sorry, {name} you are not eligible.")

#E-Commerce Order Validator

# product_price = float(input("Enter your product price: "))
# premium_user = input("Are you a premium user? (yes/no): ").lower()
# user_location = input("Where are you from? (india/other): ").lower()

# if product_price < 0 or premium_user.strip() == "" or user_location.strip() == "":
#     print("Invalid input.")
# else:

#     # Discount
#     if product_price > 1000:
#         discount = product_price * 15 / 100
#     else:
#         discount = 0

#     # Shipping
#     if premium_user == "yes":
#         shipping = 0
#     elif user_location != "india":
#         shipping = 200
#     else:
#         shipping = 0

#     final_price = product_price - discount + shipping

#     print("\n--- Order Summary ---")
#     print(f"Product Price: ₹{product_price:.2f}")
#     print(f"Discount: ₹{discount:.2f}")
#     print(f"Shipping: ₹{shipping:.2f}")
#     print(f"Final Payable Amount: ₹{final_price:.2f}")
    