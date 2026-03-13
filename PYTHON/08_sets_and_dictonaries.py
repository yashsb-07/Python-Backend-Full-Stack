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

    print("\n1. Add student")
    print("2. View student")
    print("3. Search student")
    print("4. Update student")
    print("5. Delete student")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Please enter valid choice.")
        continue

    choice = int(choice)

    if choice == 1:
        student_id = input("Enter student id: ")

        if not student_id.isdigit():
            print("Id must be an integer value.")
            continue

        student_id = int(student_id)

        student_name = input("Enter student name: ").strip().lower()

        if not student_name.replace("", "").isalpha():
            print("Name conatin only letters")
            continue
        
        student_marks = input("Enter student marks: ")

        if not student_marks.isdigit():
            print("Marks must be a number.")
            continue

        student_marks = int(student_marks)

        if student_id in students:
            print("Student id must be unique.")
        else:
            students[student_id] = {
                "name" : student_name,
                "marks" : student_marks
            }
            print("Student added succesfully!")

    elif choice == 2:
        if not students:
            print("No data available.")
        else:
            print("\nStudents: ")
            for sid, data in students.items():
                print(f"ID: {sid} | Name: {data['name']} | Marks: {data['marks']}")
        
    elif choice == 3:
        student_id = input("Enter student id to search: ")

        if not student_id.isdigit():
            print("Invalid id.")
            continue
        
        student_id = int(student_id)

        if student_id in students:
            student = students[student_id]
            print(f"ID: {student_id} | Name: {student['name']} | Marks: {student['marks']}")
        else:
            print("Student not found.")

    elif choice == 4:
        student_id = input("Enter student id to update: ")

        if not student_id.isdigit():
            print("Invalid id.")
            continue

        student_id = int(student_id)

        if student_id in students:
            new_name = input("Update student name: ").strip().lower()
            new_marks = input("Update student marks: ")

            if not new_marks.isdigit():
                print("Marks must be a number.")
                continue

            students[student_id]['name'] = new_name
            students[student_id]['marks'] = int(new_marks)

            print("Student updated succesfully!")
            
        else:
            print("Student not found.")

    elif choice == 5:
        student_id = input("Enter student id to delete: ")

        if not student_id.isdigit():
            print("Enter valid id.")
            continue

        student_id = int(student_id)

        if student_id in students:
            del students[student_id]
            print("Student deleted succesfully!")
        else:
            print("Student not found.")

    elif choice == 6:
        print("Exiting program..")
        break

    else:
        print("Invalid choice. Please try again!")

