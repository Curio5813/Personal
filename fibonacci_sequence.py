def fibonacciSequence():
    """
    This function return the fibonacci sequence until the term
    specified by the user.
    :return:
    """
    a, b, = 0, 1
    num = int(input("How many terms do you want have the fibonacci "
                    "sequence? "))
    for i in range(num + 1):
        print(a, end=" ")
        a, b, = b, a + b


fibonacciSequence()
print("")
