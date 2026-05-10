import json

def load_contacts():
    global contacts
    try:
        with open("contacts.json", "r") as f:
            contacts = json.load(f)
    except FileNotFoundError:
        contacts = {}

def save_contacts():
    with open("contacts.json", "w") as f:
        json.dump(contacts, f, indent=4)

#Number Validation
def is_valid_phone(phone):
    return phone.isdigit() and len(phone) == 10

def add_contact():
    name = input("Enter name: ").strip()
    phone = input("Enter phone number: ")
    email = input("Enter email: ")

    if not is_valid_phone(phone):
        print("Invalid phone number (must be 10 digits)")
        return

    contact_data = {"phone": phone, "email": email}

    if name in contacts:
        contacts[name].append(contact_data)
    else:
        contacts[name] = [contact_data]

    save_contacts()
    print("Contact added successfully!")

def view_contact():
    if not contacts:
        print("No contacts found.")
        return

    print("\nCONTACT LIST")
    print("=" * 40)

    for name in sorted(contacts.keys()):
        print(f"\n{name}")
        for i, detail in enumerate(contacts[name], start=1):
            print(f"  [{i}] Phone: {detail['phone']}, Email: {detail['email']}")

def search_contact():
    search = input("Enter name to search: ").lower()

    found = False
    for name in contacts:
        if search in name.lower():
            print(f"\n{name}")
            for detail in contacts[name]:
                print(f"Phone: {detail['phone']}, Email: {detail['email']}")
            found = True

    if not found:
        print("No matching contact found.")

def update_contact():
    name = input("Enter name to update: ")

    if name in contacts:
        for i, detail in enumerate(contacts[name]):
            print(f"{i+1}. {detail}")

        index = int(input("Select contact number: ")) - 1

        phone = input("Enter new phone: ")
        email = input("Enter new email: ")

        if not is_valid_phone(phone):
            print("Invalid phone number")
            return

        contacts[name][index] = {"phone": phone, "email": email}

        save_contacts()
        print("Updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter name to delete: ")

    if name in contacts:
        for i, detail in enumerate(contacts[name]):
            print(f"{i+1}. {detail}")

        index = int(input("Select contact number: ")) - 1

        confirm = input("Are you sure? (y/n): ").lower()

        if confirm == "y":
            contacts[name].pop(index)

            if not contacts[name]:
                del contacts[name]

            save_contacts()
            print("Deleted successfully!")
        else:
            print("Cancelled")
    else:
        print("Contact not found.")

#Export Contact in TXT
def export_contacts():
    with open("export.txt", "w") as f:
        for name, details in contacts.items():
            for detail in details:
                f.write(f"{name} - {detail['phone']} - {detail['email']}\n")

    print("Contacts exported successfully!")

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