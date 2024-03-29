from time import sleep

def zenosParadox():
    """
    This function treat about the Zeno's Paradox.
    :return:
    """
    distance, zeno, turtle, cont = 100, 0, 93, 0
    while zeno < turtle:
        distance /= 2
        turtle += 1
        zeno += distance
        cont += 1
        if cont == 1_000_000_000_000:
            text1 = "This is a convergent geometric progression, and its value converges to 100."
            for i in text1:
                print(i, end="")
                sleep(0.1)
            print("")
            sleep(3)
            return print(f"Zeno will never reach the turtle. Altogether Zeno ran {zeno} metres.")
    return print(f"Zeno needs {cont} leaps to reach the turtle and will reach the "
                 f"turtle at the distance {zeno} metres.")


zenosParadox()
print("")
print("It's all folks!")
