from random import randint

random_num = randint(1, 10)
user_num = 0
counter = 0

print("Guess the number between 1 to 10.")

while user_num != random_num:

    user_num = int(input("\nGuess your number: "))
    counter += 1

    if user_num == random_num:
        print("Congratulations ✨🎊 You won!")
        print(f"Total attempts: {counter}")

    elif user_num > random_num:
        print("Number is too high. Try smaller!")

    else:
        print("Number is too small. Try larger!")