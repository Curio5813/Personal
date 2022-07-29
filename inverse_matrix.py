def givenMatrix():
    """
    This function print a matrix created by user and return a list with it.
    :return:
    """
    l1, l2 = [], []
    print('')
    x = int(input('How many rows has the matrix you want to invert? '))
    y = int(input('How many colums has the matrix you want to invert? '))
    for i in range(x):
        for k in range(y):
            num = int(input(f"What's the value for {i + 1}st. row "
                            f"and {k + 1}st. colum? "))
            l1.append(num)
        l2.append(l1)
        l1 = []
    print("")
    print("The given matrix is: ")
    for i in range(0, len(l2)):             # This iteration print the matrix
        for k in range(0, len(l2[i])):
            print(l2[i][k], end=' ')
        print('\n', end='')
    return l2


def inverseMatrix(l2):
    """
    This function print the inverse matrix from matrix generated
    above by the user.
    :param l2:
    :return:
    """
    l3, l4 = [], []
    for i in range(0, len(l2[0])):   # This iteration put in a list the inverse matrix.
        for k in range(len(l2)):     # The colums must to be the lines and the lines the colums.
            l3.append(l2[k][i])      # This avoid the list index error out of range.
        l4.append(l3)
        l3 = []
    print("")
    print("The inverse matrix is: ")
    for i in range(0, len(l4)):
        for k in range(0, len(l4[i])):
            print(l4[i][k], end=' ')
        print("\n", end='')


inverseMatrix(givenMatrix())
