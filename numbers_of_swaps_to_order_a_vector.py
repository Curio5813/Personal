from random import randint


def main():
    """
    This function return the number of swaps needly to let
    a given aleatory list ordered.
    :return:
    """
    lth = int(input("What's the length of the list: "))
    i, swap, v = 0, 0, []
    while len(v) < lth:
        a = randint(0, 100)
        v.append(a)
    print(v)
    x = v.copy()
    x.sort()
    while v != x:
        i += 1
        while v[i - 1] > v[i]:
            v[i - 1], v[i] = v[i], v[i - 1]
            swap += 1
        if i >= len(v) - 1:
            i = 0
    print(f"Swaps made: {swap}")
    print(v)


if __name__ == '__main__':
    main()
