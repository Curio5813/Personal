def eulerNumber():
    """
    This function calculates the Euler number, a transcendental number
    used in calculating exponential equations and rate changes and which
    is itself its derivative.
    :return:
    """
    n = int(input("How precisely you want the number: "))
    e = (1 + (1 / n)) ** n
    print(e)


eulerNumber()
