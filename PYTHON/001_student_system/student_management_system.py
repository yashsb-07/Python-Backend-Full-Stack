# STUDENT MANAGEMENT SYSTEM

students = {}

def add_student():
    roll = input("Enter roll number: ")
    name = input("Enter name: ")
    age = input("Enter age: ")
    course = input("Enter course: ")

    students[roll] = {
        "name": name,
        "age": age,
        "course": course
    }

    print("Student added successfully!")

def view_student():
    if not students:
        print("No student found!")
        return
    
    for roll, details in students.items():
        print("\nRoll:", roll)
        print("Name:", details["name"])
        print("Age:", details["age"])
        print("Course:", details["course"])

def search_student():
    roll = input("Enter roll number to search: ")
    if roll in students:
        print(students[roll])
    else:
        print("Student not found.")

def update_student():
    roll = input("Enter roll number to update: ")
    if roll in students:
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        course = input("Enter new course: ")

        students[roll] = {
            "name": name, 
            "age": age,
            "course": course
        }

        print("Student updated successfully!")
    else:
        print("Student not found!")

def delete_student():
    roll = input("Enter roll number to delete:")
    if roll in students:
        del students[roll]
        print("Student deleted successfully!")
    else:
        print("Student not found!")

while(True):
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")
        
    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Please enter valid choice.")
        break

    choice = int(choice)

    if choice == 1:
        add_student()

    elif choice == 2:
        view_student()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        print("Exiting program..")
        break

    else:
        print("Invalid choice.")