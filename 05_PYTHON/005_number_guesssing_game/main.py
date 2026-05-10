import game

while True:
    print("\n===== NUMBER GUESSING GAME =====")
    print("1. Play Game")
    print("2. Exit")

    choice = input("\nEnter your choice: ")

    if not choice.isdigit():
        print("Invalid choice: ")
        continue

    choice = int(choice)

    if choice == 1:
        game.play_game()
    elif choice == 2:
        print("Thanks for playing!")
        break
    else:
        print("Invalid choice.")