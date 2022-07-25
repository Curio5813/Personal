def poligonalDiagonal():
    """
    This function print the numbers of diagonal that has a
    given poligonal given the numbers of sides.
    :return:
    """
    s = int(input("How many sides has the poligonal : "))
    d = int((s * (s - 3)) / 2)
    print(d)


poligonalDiagonal()
