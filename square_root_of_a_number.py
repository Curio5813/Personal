from math import sqrt


def square_root_of_a_number():
    """
    By using Newton Aproximation.
    :return:
    """
    n = 5
    estimativa = 10  # It can be any number.
    nova_estimativa = 0
    for i in range(10000):
        nova_estimativa = (estimativa + (n / estimativa)) / 2
        estimativa = nova_estimativa
    print(f"By using Newton Aproximation: {nova_estimativa:.50f}")
    print(f"By using the Python's function sqrt: {sqrt(n):.50f}")


square_root_of_a_number()
