"""List"""

#To-Do list manager

# task = []

# print("Welcome to To-Do list manager app")

# while True:

#     print("\n1. Show task")
#     print("2. Add task")
#     print("3. Remove task")
#     print("4. Exit")

#     choice = int(input("\nEnter you choice: "))

#     if choice == 1:
#         if not task:
#             print("No task available.")
#         else:
#             print(task)
    
#     elif choice == 2:
#         user_task = input("Enter task: ")
#         task.append(user_task)
#         print("Task added succesfully!")
    
#     elif choice == 3:
#         if not task:
#             print("No task available to remove.")
#         else:
#             idx = int(input("Enter index no: "))
            
#             if 1 <= idx <= len(task):
#                 removed = task.pop(idx - 1)
#                 print(f"Removed task: {removed}")
#             else:
#                 print("Invalid task number.")

#     elif choice == 4:
#         print("Thank you!")
#         break

#     else:
#         print("Invalid choice! Please select between 1-4.")

#Students Marks Manager

# marks = []

# print("Welcome to the student marks manager system")

# while True:

#     print("\n1. Show all marks")
#     print("2. Add student marks")
#     print("3. Show highest marks")
#     print("4. Show average marks")
#     print("5. Exit")

#     choice = int(input("\nEnter your choice: "))

#     if choice == 1:
#         if not marks:
#             print("Marks are not available.")
#         else:
#             for i, mark in enumerate(marks, start=1):
#                 print(f"Student {i}: {mark}")

#     elif choice == 2:
#         student_marks = int(input("Enter marks: "))
#         if 0 <= student_marks <= 100:
#             marks.append(student_marks)
#             print("Marks added successfully!")
#         else:
#             print("Please enter marks between 0 and 100.")

#     elif choice == 3:
#         if not marks:
#             print("No marks are available.")
#         else:
#             print(f"Highest marks: {max(marks)}")

#     elif choice == 4:
#         if not marks:
#             print("Marks are not available.")
#         else:
#             avg = sum(marks) / len(marks)
#             print(f"Average marks: {avg:.2f}")

#     elif choice == 5:
#         print("Thank you!")
#         break

#     else:
#         print("Please enter a valid choice.")

#Shopping Cart

# cart = []

# print("Welcome to the Super Market!")

# while True:

#     print("\n1. Add item")
#     print("2. View cart")
#     print("3. Remove item")
#     print("4. Total items")
#     print("5. Exit")

#     choice = input("\nEnter your choice: ")

#     if not choice.isdigit():
#         print("Please enter a valid number.")
#         continue

#     choice = int(choice)

#     if choice == 1:
#         item = input("Enter item name: ")
#         cart.append(item)
#         print(f"'{item}' added to cart!")

#     elif choice == 2:
#         if not cart:
#             print("Cart is empty!")
#         else:
#             print("\nYour Cart:")
#             for i, item in enumerate(cart, start=1):
#                 print(f"{i}. {item}")

#     elif choice == 3:
#         if not cart:
#             print("No items in cart to remove.")
#         else:
#             item_index = int(input("Enter item number: "))

#             if 1 <= item_index <= len(cart):
#                 removed_item = cart.pop(item_index - 1)
#                 print(f"'{removed_item}' removed from cart!")
#             else:
#                 print("Invalid item number.")

#     elif choice == 4:
#         print(f"Total items in cart: {len(cart)}")

#     elif choice == 5:
#         print("Thank you for shopping. Have a great day!")
#         break

#     else:
#         print("Invalid choice! Choose between 1-5.")

"""Tuples"""

#Student result system

students_result = []

print("Welcome to the Student Result System")

while True:

    print("\n1. Add student result")
    print("2. View all results")
    print("3. Show topper")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Enter a valid choice.")
        continue

    choice = int(choice)

    if choice == 1:
        name = input("Enter student name: ")

        marks_input = input("Enter student marks: ")
        if not marks_input.isdigit():
            print("Marks must be a number.")
            continue

        marks = int(marks_input)

        students_result.append((name, marks))
        print("Student result added successfully.")

    elif choice == 2:
        if not students_result:
            print("No student results available!")
        else:
            print("\nStudent Results:")
            for i, (name, marks) in enumerate(students_result, start=1):
                print(f"{i}. {name} - {marks}")

    elif choice == 3:
        if not students_result:
            print("No results available to find topper.")
        else:
            topper = max(students_result, key=lambda x: x[1])
            print(f"Topper: {topper[0]} ({topper[1]})")

    elif choice == 4:
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice! Choose between 1-4.")

    
    