from math import log2, pi, sqrt


def littelJoke():
    """
    This function return the average letter in all names
    of peolple
    :return:
    """
    text = 'The letter "A" in my name!'
    print('='*30)
    print("The letter 'A' in my name".center(30))
    print('='*30)
    n = 3.1450000  # It's a square root sin(log2(60) ** (phi / a))
    a = (1 + (1 / log2(n - 1)) ** ((n - 2) * pi))
    phi = (1 + sqrt(5)) / 2
    my_dict = {'key1': 'Hello, World!', 'key2': [2, 3, 5, 7, 11], 'key3': a}
    print('')
    print(f"All interger number is greater than 1 "
          f"becouse the ratio between letter 'A' and 'L' is given by {a:.6f}")
    print(f"In any latin dictonary the ratio of 'A' and 'L' is given by {my_dict['key3']:.6f}")
    print(f'The Golden Number is equal to {phi:.6f}')
    print(f"The diferrence about 'A' in my name by the Golden Number is given by "
          f"{(a - phi) * 100:.2f} %")
    print("Exactly the percentage of W and Z in latin words")
    print('')
    print("This is the reason the sky is blue!".upper())


littelJoke()
