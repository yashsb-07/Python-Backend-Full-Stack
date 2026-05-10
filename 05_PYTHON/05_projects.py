#Guessing game

# from random import randint

# random_num = randint(1, 10)
# user_num = 0
# counter = 0

# print("Guess the number between 1 to 10.")

# while user_num != random_num:

#     user_num = int(input("\nGuess your number: "))
#     counter += 1

#     if user_num == random_num:
#         print("Congratulations ✨🎊 You won!")
#         print(f"Total attempts: {counter}")

#     elif user_num > random_num:
#         print("Number is too high. Try smaller!")

#     else:
#         print("Number is too small. Try larger!")

#Login system with retry limit

# correct_username = "yashsb07"
# correct_password = "Yash@123"

# attempts = 0
# max_attempts = 3

# while attempts < max_attempts:

#     username = input("Enter username: ")
#     password = input("Enter password: ")

#     attempts += 1

#     if username == correct_username and password == correct_password:
#         print("Access Granted!")
#         break

#     else:
#         if attempts < max_attempts:
#             remaining_attempts = max_attempts - attempts
#             print("Access denied! Try again.")
#             print(f"Attempts left: {remaining_attempts}")
#         else:
#             print("Account locked.")

#ATM Menu System Program

# balance = 1000

# print("Welcome to the Bank ATM.")

# while True:

#     print("\n1. Check Balance")
#     print("2. Deposit Amount")
#     print("3. Withdraw Amount")
#     print("4. Exit")

#     choice = int(input("\nEnter your choice: "))

#     if choice == 1:
#         print(f"Available balance: ₹{balance}")

#     elif choice == 2:
#         amt = int(input("Enter deposit amount: "))
#         if amt <= 0:
#             print("Invalid amount.")
#         else:
#             balance += amt
#             print(f"₹{amt} deposited successfully!")

#     elif choice == 3:
#         amt = int(input("Enter withdraw amount: "))
#         if amt <= 0:
#             print("Invalid amount.")
#         elif amt > balance:
#             print("Insufficient balance!")
#         else:
#             balance -= amt
#             print(f"₹{amt} withdrawn successfully!")

#     elif choice == 4:
#         print("Thank you for using ATM.")
#         break

#     else:
#         print("Invalid choice. Please select 1–4.")