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
            for j in range(0, len(pg[i][k])):
                print(pg[i][k][j], end="")
                sleep(0.08)
            print('\n', end="")
    a = 1
    q = 2
    b = a * q ** (64 - 1)  # This is the formula for a finite P.G.
    sleep(2)
    print("")
    print(f"Is needly {b} grain of rice to cover all 64º houses of a \n"
          f"chessboard.")


riceGrainsAndChess()
