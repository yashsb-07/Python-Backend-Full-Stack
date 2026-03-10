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

marks = []

print("Welcome to the student marks manager system")

while True:

    print("\n1. Show all marks")
    print("2. Add student marks")
    print("3. Show highest marks")
    print("4. Show average marks")
    print("5. Exit")

    choice = int(input("\nEnter your choice: "))

    if choice == 1:
        if not marks:
            print("Marks are not available.")
        else:
            for i, mark in enumerate(marks, start=1):
                print(f"Student {i}: {mark}")

    elif choice == 2:
        student_marks = int(input("Enter marks: "))
        if 0 <= student_marks <= 100:
            marks.append(student_marks)
            print("Marks added successfully!")
        else:
            print("Please enter marks between 0 and 100.")

    elif choice == 3:
        if not marks:
            print("No marks are available.")
        else:
            print(f"Highest marks: {max(marks)}")

    elif choice == 4:
        if not marks:
            print("Marks are not available.")
        else:
            avg = sum(marks) / len(marks)
            print(f"Average marks: {avg:.2f}")

    elif choice == 5:
        print("Thank you!")
        break

    else:
        print("Please enter a valid choice.")