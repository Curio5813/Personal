from math import factorial


def mega_sena_probability():
    """
    This function calculate the probability to win the MegaSena prize
    in a simple game.
    :return:
    """
    comb = int(factorial(60) / (factorial(6) * (factorial(60 - 6))))
    return print(f"Probability from 1 to {comb} millions.")


mega_sena_probability()
print("")
print("It's all folks!")
