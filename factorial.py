def factorial():
    """
    This function return the factorial of a given number.
    :return:
    """
    num = int(input('What number do you wish to calculate its factorial? '))
    n, fat = 1, 1
    while n <= num:
        fat *= n
        n += 1
    return print(fat)


factorial()
