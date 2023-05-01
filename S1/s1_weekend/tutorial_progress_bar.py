# for progress bar we are using █ - Alt219
import math



def progress_bar(progress, total):
    percent = 100 * (progress/ float(total))
    bar = "█" * int(percent) + "-" * (100 - int(percent))
    print(f"\r|{bar}| {percent:.2f}%", end="\r")             # :.2f - too see up to 2 decimals


numbers = [x * 1 for x in range(6000, 7000)]
results = []


def loader():
    progress_bar(0, len(numbers))
    for i, x in enumerate(numbers):
        results.append(math.factorial(x))
        progress_bar(i + 1, len(numbers))

check = True


while check:
    answer = input("Y/N: ")
    if answer.upper() == "N":
        check = False
    else:
        loader()
        print()


