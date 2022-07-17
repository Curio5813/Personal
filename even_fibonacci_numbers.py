def evenFibonacciNumbers():
    """
    This function return the even numbers into the Fibonacci sequence
    given the number of terms of the sequence
    :return:
    """
    a, b, p, cont, l = 0, 0, 1, 0, []
    num = int(input('How many terms do you want to have the sequence? '))
    for i in range(num):
        a, b, = b, p
        p = a + b
        if a % 2 == 0 and a != 0:
            cont += 1
            l.append(a)
    print(f"The number of even numbers between the first and last term are {cont}.")
    return print(*l)


evenFibonacciNumbers()
