def main():
    from random import randint
    i, swap, v = 0, 0, []
    while len(v) < 20:
        a = randint(0, 100)
        v.append(a)
    x = v.copy()
    x.sort()
    print(*v)
    print('')
    while v != x:
        i += 1
        while v[i - 1] > v[i]:
            v[i - 1], v[i] = v[i], v[i - 1]
            swap += 1
        if i >= len(v) - 1:
            i = 0
    print(f'Swaps realizados: {swap}')
    print(*v)


if __name__ == '__main__':
    main()
