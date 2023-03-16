from random import randint
from math import log2

l1, l2 = [], []
for num in range(1000 + 1):
    l1.append(num)
l2.append(randint(1, 1000))
number = l2[0]


def binary_search():
    """
    This function use binary search as an algorithmo to search an
    item in a list given above. Here is the prototype of the game
    of guess a number.
    """
    low, high, cont = 0, len(l1) - 1, 0
    while low <= high:
        middle = int((low + high) / 2)
        print(f"Best guess {middle}.")
        guess = int(input("Try to gess the number: "))
        print("")
        if guess == number:
            print("")
            return print(f"{number} guessed in {cont} attempt.")
        elif guess > number:
            print("The number is less than the guess.")
            high = middle - 1
        elif guess < number:
            print("The number is greater than the guess.")
            low = middle + 1
        cont += 1
    print("")
    return print("You cannot guess the number.")


binary_search()
print("")
print(f"The number is {number}.")
print(f"The Big(O) of this problem is O(log(n)), {int(log2(len(l1)))} in the worst case.")



