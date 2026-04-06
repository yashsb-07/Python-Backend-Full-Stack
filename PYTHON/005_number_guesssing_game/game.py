import random

def play_game():
    print("\nSelect Difficulty Level:")
    print("1. Easy (1-50)")
    print("2. Medium (1-100)")
    print("3. Hard (1-200)")

    level = input("\nEnter choice: ")

    if level == "1":
        max_num = 50

    elif level == "2":
        max_num = 100
    
    elif level == "3":
        max_num = 200

    else:
        print("Invalid choice, Default medium selected.")
        max_num = 100

    number = random.randint(1, max_num)
    attempt = 0

    print(f"\nGuess a number between 1 and {max_num}")

    while True:
        guess = int(input("Enter you guessing number: "))
        attempt += 1

        if guess > number:
            print("Too High!")
        elif guess < number:
            print("Too Low!")
        else:
            print(f"Correct! You guessed in {attempt} attempts.")
            break
