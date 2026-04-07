contacts = {}

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    print("Contact added successfully!")

def view_contact():
    if not contacts:
        print("No contact found.")
        return

    for name, details in contacts.items():
        print("\nName:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])

def search_contact():
    name = input("Enter contact name to search: ")

    if name in contacts:
        print("Phone:", contacts[name]["phone"])
        print("Email:", contacts[name]["email"])
    else:
        print("Contact not found.")

def update_contact():
    name = input("Enter contact name to update: ")

    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")

        contacts[name]["phone"] = phone
        contacts[name]["email"] = email

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

while True:
    print("\n===== CONTACT BOOK =====")
    print("1. Add contact")
    print("2. View contact")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")

    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Please enter valid choice: ")
        continue
    
    choice = int(choice)

    if choice == 1:
        add_contact()

    elif choice == 2:
        view_contact()

    elif choice == 3:
        search_contact()

    elif choice == 4:
        update_contact()

    elif choice == 5:
        delete_contact()

    elif choice == 6:
        print("Exiting contact book.")
        break
    else:
        print("Invalid choice.")