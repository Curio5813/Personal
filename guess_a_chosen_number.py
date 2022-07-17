from random import randint


def guessTheNumber():
    """
    This function return a pseudoaleatory number generate by the
    library random imported and using the randint module. This
    function implement a kind of guess game.
    :return:
    """
    asw = "YES"
    while asw == "YES":
        print('='*65)
        print("try to guess the number whom the computer chosen from 1 to 10".upper().center(65))
        print('='*65)
        pc = randint(1, 10)
        print('')
        player = int(input("Choose a number from 1 to 10: "))
        print('')
        if player == pc:
            print(f"Congratulations! You guessed the Computer chosen number, tha is {pc}")
            print('')
        elif player != pc:
            print(f"I'm sorry... You didn't guessed the computer chosen number, that was {pc}")
            print('')
        asw = str(input("Do you want play again? ")).upper()
        if asw == "YES":
            print("Great! Let's start the game!")
            print('')
        else:
            print("Ok, Have a nice day!")
            print("")
            break


guessTheNumber()
