def eulerNumber():
    """
    This function calculates the Euler number, a transcendental number
    used to compute exponential equations and rate changes that have
    themselves as derivatives.
    :return:
    """
    n = int(input("How precisely you want the number: "))
    e = (1 + (1 / n)) ** n
    print(e)


eulerNumber()
