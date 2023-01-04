from random import randint
from math import log2

l1 = []
for num in range(100):
    l1.append(randint(1, 200))
l1.sort()

number = int(input("Wich number you want to find: "))


def binary_search():
    """
    This function use binary search as an algorithmo to search an
    item in a list given above.
    """
    low, high, cont = 0, len(l1) - 1, 0
    while low <= high:
        middle = int((low + high) / 2)
        guess = l1[middle]
        if guess == number:
            return print(f"{number} guessed in {cont} attempt")
        elif guess > number:
            high = middle - 1
        elif guess < number:
            low = middle + 1
        cont += 1
    return print(f"The number {number} is not in the list")


print(f"The Big O of this problem is O(log(n)) and {int(log2(128))} in the worst case")


binary_search()
