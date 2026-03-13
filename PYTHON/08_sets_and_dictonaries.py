"""Sets"""

#Unique visitor tracker

visitors = set()
normalized_names = set()

print("Visitors: ")
while True:

    print("\n1. Add visitor.")
    print("2. View visitor")
    print("3. Total unique visitors")
    print("4. Exit")

    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Please enter valid choice!")
        continue

    choice = int(choice)

    if choice == 1:
        name = input("Enter visitor name: ").strip()
        key = name.casefold()

        if key in normalized_names:
            print("Visitor is already exits.")
        else:
            visitors.add(name)
            normalized_names.add(key)
            print("visitor added!")

    elif choice == 2:
        if not visitors:
            print("No visitors are available.")
        else:
            print("\nVisitors: ")
            for i, name in enumerate(sorted(visitors), start=1):
                print(f"{i}. {name}")

    elif choice == 3:
        print(f"Total unique visitors: {len(visitors)}")

    elif choice == 4:
        print("Good bye!")
        break

    else:
        print("please enter valid choice between 1-4.")
