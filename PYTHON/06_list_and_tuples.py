#To-Do list manager

task = []

print("Welcome to To-Do list manager app")

while True:

    print("\n1. Show task")
    print("2. Add task")
    print("3. Remove task")
    print("4. Exit")

    choice = int(input("\nEnter you choice: "))

    if choice == 1:
        if not task:
            print("No task available.")
        else:
            print(task)
    
    elif choice == 2:
        user_task = input("Enter task: ")
        task.append(user_task)
        print("Task added succesfully!")
    
    elif choice == 3:
        if not task:
            print("No task available to remove.")
        else:
            idx = int(input("Enter index no: "))
            
            if 1 <= idx <= len(task):
                removed = task.pop(idx - 1)
                print(f"Removed task: {removed}")
            else:
                print("Invalid task number.")

    elif choice == 4:
        print("Thank you!")
        break

    else:
        print("Invalid choice! Please select between 1-4.")
