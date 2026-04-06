import calculator

while (True):
    print("\n===== CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Please enter valid choice!")
        break
    
    choice = int(choice)

    if choice == 5:
        print("Existing calculator..")
        break

    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", calculator.add(a,b))

    elif choice == 2:
        print("Result:", calculator.substract(a,b))
    
    elif choice == 3:
        print("Result:", calculator.multiply(a,b))

    elif choice == 4:
        print("Result:", calculator.divide(a,b))

    else:
        print("Invalid choice!")