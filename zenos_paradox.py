def zenosParadox():
    """
    This function treat about the Zeno's Paradox.
    :return:
    """
    distance, zeno, turtle, cont = 100, 0, 100, 0
    while zeno != turtle:
        distance /= 2
        turtle += 1
        zeno += distance + 1
        cont += 1
        if cont == 100:
            return print(f"Zeno will never reach the turtle. Zeno ran {zeno} metres.")
    return print(f"Zeno needs {cont} leaps to reach the turtle and will reach the "
                 f"turtle at the distance {zeno} metres.")


zenosParadox()
print("")
print("It's all folks!")
