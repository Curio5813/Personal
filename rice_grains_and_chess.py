from time import sleep
from csv import reader


def riceGrainsAndChess():
    """
    This function print a solution for a finit Geometric Progression.
    :return:
    """
    arq = open("rice_grains_and_chess.csv")
    pg = reader(arq)
    pg = list(pg)
    ls = []
    for i in range(0, len(pg)):
        for k in range(0, len(pg[i])):
            ls.append(pg[i][k])
    for i in range(0, len(ls)):
        for k in range(0, len(ls[i])):
            print(ls[i][k], end="")
            sleep(0.05)
        print('\n', end="")
    a = 1
    q = 2
    b = a * q ** (64 - 1)
    sleep(2)
    print("")
    print(f"Is needly {b} grain of rice to cover all 64º houses of a \n"
          f"chessboard.")


riceGrainsAndChess()
