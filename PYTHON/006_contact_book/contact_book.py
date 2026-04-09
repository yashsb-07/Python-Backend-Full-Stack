contacts = {}

def load_contacts():
    try: 
        with open ("contacts.txt", "r") as f:
            for line in f:
                name, phone, email = line.strip().split(",")
                contacts[name] = {
                    "phone": phone,
                    "email": email
                }
    except FileNotFoundError:
        pass

def save_contacts():
    with open ("contacts.txt", "w") as f:
        for name, details in contacts.items():
            f.write(f"{name}, {details['phone']}, {details['email']}\n")

def add_contact():
    name = input("Enter name: ").strip()

    if name in contacts:
        print("Contact already exists.")
        return

    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    contacts[name] = {
        "phone": phone,
        "email": email
    }

    save_contacts()

    print("Contact added successfully!")

def view_contact():
    if not contacts:
        print("No contact found.")
        return

    print("\nCONTACT LIST")
    print("-" * 40)

    for name, details in contacts.items():
        print("\nName:", name)
        print("Phone:", details["phone"])
        print("Email:", details["email"])
        print("-" * 40)

def search_contact():
    search = input("Enter contact name to search: ").lower()
    found = False

    print("\nSearch Results")
    print("-" * 40)

    for name, details in contacts.items():
        if search in name.lower():
            print(f"Name: {name}")
            print("Phone:", contacts[name]["phone"])
            print("Email:", contacts[name]["email"])
            print("-" * 40)
            found = True

    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter contact name to update: ").strip()

    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")

        contacts[name]["phone"] = phone
        contacts[name]["email"] = email

        save_contacts()

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter contact name to delete: ")

    if name in contacts:
        confirm = input("Are you sure? (y/n): ").lower()

        if confirm == "y":
            del contacts[name]
            save_contacts()
            print("Contact deleted successfully!")
        else:
            print("Deletion cancled.")
    else:
        print("Contact not found.")

load_contacts()

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