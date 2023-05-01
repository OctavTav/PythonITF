import random
import math


def progress_bar(progress, total):
    percent = 100 * (progress / float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent))
    print(f"\r|{bar}|", end="\r")


numbers = [x * 5 for x in range(1000, 2000)]
results = []


def loader():
    progress_bar(0, len(numbers))
    for i, x in enumerate(numbers):
        results.append(math.factorial(x))
        progress_bar(i+1, len(numbers))


def dice_roll():
    print("wait for the computer to roll the dice!")
    loader()
    print()
    return random.randint(1, 6)


def check_guess(number_computer, number_user):
    if number_computer == number_user:
        print("Such wow! Much happy!")
    else:
        print(f"Such shame! Much sad... Roll was {number_computer}")
    print("Wanna play again? Yes/No")


def check_answer(user_answer):
    if user_answer != "no":
        return True
    else:
        return False


def game():
    number_rolled = 0
    user_answer = input()
    if check_answer(user_answer):
        number_rolled = dice_roll()
        # print(number_rolled)
        print("Guess the number rolled")
        while True:
            user_answer = input()
            try:
                user_answer = int(user_answer)
            except:
                print("Enter valid answer!")
                continue
            if user_answer not in range(1, 7):
                print("Dice roll can be from 1 to 6")
            else:
                break
        check_guess(number_rolled, user_answer)

        return True
    else:
        return False


print("Hello! Welcome to THE DICE ROLL GAME! Wanna try your luck? Yes/No")
play = True
while play:
    play = game()
print("Come back anytime you want!")
