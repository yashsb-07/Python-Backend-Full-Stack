import password_generator

while True:
    print("\n==== PASSWORD GENERATOR ====")
    print("1. Generate Password")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Please enter valid choice: ")
        break

    choice = int(choice)

    if choice == 1:
        length = int(input("Enter your password length: "))
        digits = input("Include digits? (y/n): ")
        symbols = input("Include symbols (y/n): ")

        password = password_generator.generate_password(
            length, 
            digits == "y",
            symbols == "y"
        )

        print("Generated Password: ", password)

    elif choice == 2:
        print("Exiting program..")
        break
    else:
        print("Invalid choice.")