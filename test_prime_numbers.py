from time import time

start = time()


def testIfPrimeNumber():
    """
    This function print if a given number is prime or not prime number.
    :return:
    """
    num = int(input("Digit a interger number: "))
    for i in range(2, 500_000_000 + 1):
        if num % i == 0 and num != i:
            return print("This number is not a prime number.")
        elif num % i == 0 and num == i:
            return print("It's a prime number!")


testIfPrimeNumber()
end = time()
print(f"{(end - start):.2f}")
