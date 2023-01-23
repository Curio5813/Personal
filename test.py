def floyd_triangle():
    """
    This function generate the Floyd's Triangle.
    :return:
    """
    row = int(input("How many lines do you want in the triangle: "))
    a, b, n = 1, 2, 1
    for i in range(row):
        for k in range(a, b):
            print(f"{k:>3}", end=" ")
        a = b
        n += 1
        b = a + n
        print("\n", end="")


floyd_triangle()
