"""Sets"""

#Unique visitor tracker

# visitors = set()
# normalized_names = set()

# print("Visitors: ")
# while True:

#     print("\n1. Add visitor.")
#     print("2. View visitor")
#     print("3. Total unique visitors")
#     print("4. Exit")

#     choice = input("\nEnter your choice: ")

#     if not choice.isdigit():
#         print("Please enter valid choice!")
#         continue

#     choice = int(choice)

#     if choice == 1:
#         name = input("Enter visitor name: ").strip()
#         key = name.casefold()

#         if key in normalized_names:
#             print("Visitor is already exits.")
#         else:
#             visitors.add(name)
#             normalized_names.add(key)
#             print("visitor added!")

#     elif choice == 2:
#         if not visitors:
#             print("No visitors are available.")
#         else:
#             print("\nVisitors: ")
#             for i, name in enumerate(sorted(visitors), start=1):
#                 print(f"{i}. {name}")

#     elif choice == 3:
#         print(f"Total unique visitors: {len(visitors)}")

#     elif choice == 4:
#         print("Good bye!")
#         break

#     else:
#         print("please enter valid choice between 1-4.")

"""Dictionaries"""

#Contact Book

# contacts = {}

# while True:

#     print("\n1. Add contact")
#     print("2. View contact")
#     print("3. Search contact")
#     print("4. Delete contact")
#     print("5. Exit")

#     choice = input("\nEnter your choice: ")

#     if not choice.isdigit():
#         print("Please enter valid choice.")
#         continue

#     choice = int(choice)

#     if choice == 1:
#         name = input("Enter name: ").strip()
#         phone = input("Enter phone: ").strip()

#         if not phone.isdigit():
#             print("Please enter valid phone number.")
#             continue

#         key = name.lower()

#         if key in contacts:
#             print("Contact already exists!")
#         else:
#             contacts[key] = {"name": name, "phone": phone}
#             print("Contact added!")

#     elif choice == 2:
#         if not contacts:
#             print("Contact book is empty.")
#         else:
#             print("\nContacts:")
#             for contact in contacts.values():
#                 print(f"{contact['name']} : {contact['phone']}")

#     elif choice == 3:
#         name = input("Enter name to search: ").strip().lower()

#         if name in contacts:
#             contact = contacts[name]
#             print(f"{contact['name']} : {contact['phone']}")
#         else:
#             print("Contact not found!")

#     elif choice == 4:
#         name = input("Enter name to delete: ").strip().lower()

#         if name in contacts:
#             del contacts[name]
#             print("Contact removed!")
#         else:
#             print("Contact not found!")

#     elif choice == 5:
#         print("Good bye!")
#         break
    
#     else:
#         print("Please enter valid choice between 1-5")

#Inventory Management System

# inventory = {}

# while True:

#     print("\n1. Add Product")
#     print("2. View Inventory")
#     print("3. Update Quantity")
#     print("4. Remove Product")
#     print("5. Exit")

#     choice = input("\nEnter your choice: ")

#     if not choice.isdigit():
#         print("Please enter a valid choice.")
#         continue

#     choice = int(choice)

#     if choice == 1:
#         product_name = input("Enter product name: ").strip().lower()
#         quantity = input("Enter product quantity: ")

#         if not quantity.isdigit():
#             print("Quantity must be a number.")
#             continue

#         quantity = int(quantity)

#         if product_name in inventory:
#             print("Product already exists!")
#         else:
#             inventory[product_name] = {
#                 "name": product_name,
#                 "quantity": quantity
#             }
#             print("Product added!")

#     elif choice == 2:
#         if not inventory:
#             print("Inventory is empty!")
#         else:
#             print("\nInventory:")
#             for i, item in enumerate(inventory.values(), start=1):
#                 print(f"{i}. {item['name']} : {item['quantity']}")

#     elif choice == 3:
#         product_name = input("Enter product name to update: ").strip().lower()

#         if product_name in inventory:
#             new_quantity = input("Enter new quantity: ")

#             if not new_quantity.isdigit():
#                 print("Quantity must be a number.")
#                 continue

#             inventory[product_name]["quantity"] = int(new_quantity)
#             print("Quantity updated!")
#         else:
#             print("Product not found!")

#     elif choice == 4:
#         product_name = input("Enter product name to remove: ").strip().lower()

#         if product_name in inventory:
#             del inventory[product_name]
#             print("Product removed!")
#         else:
#             print("Product not found!")

#     elif choice == 5:
#         print("Thank you!")
#         break

#     else:
#         print("Please enter a valid choice between 1–5.")


#Student Database System

students = {}

while True:

    print("\n====== STUDENT DATABASE SYSTEM ======")
    print("1. Add student")
    print("2. View students")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    choice = input("\nEnter your choice: ").strip()

    if not choice.isdigit():
        print("Please enter a valid number.")
        continue

    choice = int(choice)

    # ================= ADD STUDENT =================
    if choice == 1:

        student_id = input("Enter student ID: ").strip()

        if not student_id.isdigit():
            print("Student ID must be a number.")
            continue

        student_id = int(student_id)

        if student_id in students:
            print("Student ID already exists!")
            continue

        name = input("Enter student name: ").strip()

        if not name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue

        marks = input("Enter student marks: ").strip()

        if not marks.isdigit():
            print("Marks must be a number.")
            continue

        marks = int(marks)

        if marks < 0 or marks > 100:
            print("Marks must be between 0 and 100.")
            continue

        students[student_id] = {
            "name": name,
            "marks": marks
        }

        print("Student added successfully!")

    # ================= VIEW STUDENTS =================
    elif choice == 2:

        if not students:
            print("No students found.")
        else:
            print("\nStudents:\n")

            for i, (sid, data) in enumerate(students.items(), start=1):
                print(f"{i}. ID: {sid} | Name: {data['name']} | Marks: {data['marks']}")

            print(f"\nTotal students: {len(students)}")

    # ================= SEARCH STUDENT =================
    elif choice == 3:

        sid = input("Enter student ID to search: ").strip()

        if not sid.isdigit():
            print("Invalid ID.")
            continue

        sid = int(sid)

        if sid in students:
            student = students[sid]
            print(f"\nID: {sid} | Name: {student['name']} | Marks: {student['marks']}")
        else:
            print("Student not found.")

    # ================= UPDATE STUDENT =================
    elif choice == 4:

        sid = input("Enter student ID to update: ").strip()

        if not sid.isdigit():
            print("Invalid ID.")
            continue

        sid = int(sid)

        if sid not in students:
            print("Student not found.")
            continue

        new_name = input("Enter new name: ").strip()

        if not new_name.replace(" ", "").isalpha():
            print("Name must contain only letters.")
            continue

        new_marks = input("Enter new marks: ").strip()

        if not new_marks.isdigit():
            print("Marks must be a number.")
            continue

        new_marks = int(new_marks)

        if new_marks < 0 or new_marks > 100:
            print("Marks must be between 0 and 100.")
            continue

        students[sid]["name"] = new_name
        students[sid]["marks"] = new_marks

        print("Student updated successfully!")

    # ================= DELETE STUDENT =================
    elif choice == 5:

        sid = input("Enter student ID to delete: ").strip()

        if not sid.isdigit():
            print("Invalid ID.")
            continue

        sid = int(sid)

        if sid in students:
            del students[sid]
            print("Student deleted successfully!")
        else:
            print("Student not found.")

    # ================= EXIT =================
    elif choice == 6:
        print("Exiting program...")
        break

    else:
        print("Invalid choice. Please select between 1 and 6.")

