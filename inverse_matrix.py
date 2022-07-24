def matrixInversa():
    """
    This function return a inverse matrix from a given matrix.
    :return:
    """
    print('='*60)
    print("find the inverse matrix of a given matrix".center(60).upper())
    print('='*60)
    l1, l2, n = [], [], 0
    print('')
    x = int(input('How many rows has the matrix you want to invert? '))
    y = int(input('How many colums has the matrix you want to invert? '))
    for i in range(x):
        for k in range(y):
            num = int(input(f"What's the value for {i + 1}st. row and {k + 1}st. colum "))
            l1.append(num)
        l2.append(l1)
        l1 = []
    print('')
    print('The given matrix is:')
    for i in range(0, len(l2)):
        for k in range(0, len(l2[i])):
            print(l2[i][k], end=' ')
        print('\n', end='')
    print('')
    print(l2)
    print('The inverse matrix is:')
    for i in range(0, len(l2)):
        for k in range(0, len(l2)):
            print(l2[i + n][k], end=' ')
        print('\n', end='')
        n += 1


matrixInversa()
