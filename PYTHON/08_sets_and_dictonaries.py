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

contacts = {}

while True:

    print("\n1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Delete contact")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Please enter valid choice.")
        continue

    choice = int(choice)

    if choice == 1:
        name = input("Enter name: ").strip()
        phone = input("Enter phone: ").strip()

        if not phone.isdigit():
            print("Please enter valid phone number.")
            continue

        key = name.lower()

        if key in contacts:
            print("Contact already exists!")
        else:
            contacts[key] = {"name": name, "phone": phone}
            print("Contact added!")

    elif choice == 2:
        if not contacts:
            print("Contact book is empty.")
        else:
            print("\nContacts:")
            for contact in contacts.values():
                print(f"{contact['name']} : {contact['phone']}")

    elif choice == 3:
        name = input("Enter name to search: ").strip().lower()

        if name in contacts:
            contact = contacts[name]
            print(f"{contact['name']} : {contact['phone']}")
        else:
            print("Contact not found!")

    elif choice == 4:
        name = input("Enter name to delete: ").strip().lower()

        if name in contacts:
            del contacts[name]
            print("Contact removed!")
        else:
            print("Contact not found!")

    elif choice == 5:
        print("Good bye!")
        break
    
    else:
        print("Please enter valid choice between 1-5")