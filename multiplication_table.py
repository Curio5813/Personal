def multiplicationTable():
    """
    This function print a multiplication table for a number given by
    user from 1 to 10.
    :return:
    """
    number = int(input("which number do you want to see the multiplication table: "))
    for i in range(1, 10 + 1):
        print(f"{number} x {i:>2} = {(number * i):>2}")
    print("")


multiplicationTable()
