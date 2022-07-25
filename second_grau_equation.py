def secondGrauEquation():
    """
    This function print the roots of quadratic equation, if has
    or not solution into the domain of real set.
    :return:
    """
    print("Barkara's Formula")
    print("y = ax² + bx + c")
    print("")
    a = float(input("Digit a number for coeficient a: "))
    b = float(input("Digit a number for coeficient b: "))
    c = float(input("Digit a number for coeficient c: "))
    d = b ** 2 - 4 * a * c
    print("")
    if d >= 0:
        if d == 0:
            print("It has one root in the real domain")
        if d > 0:
            print("Are there two real roots")
    else:
        print("The equation dosen't have any real roots.")
    if d >= 0:
        if d == 0:
            x1 = - b / 2 * a
            print(f"The only real root is {x1}")
        if d > 0:
            x1 = (- b - (d ** (1/2)))/2 * a
            x2 = (- b + (d ** (1/2)))/2 * a
            print(f"The two real roots are: {x1:.1f} e {x2:.1f}")


secondGrauEquation()
