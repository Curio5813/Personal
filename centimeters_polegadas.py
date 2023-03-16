from math import sqrt


def centimetres_to_polegadas():
    """
    This function recive a values of the width
    and height in centimeters of a book or display
    and gives the length of diagonal in inch.
    :return:
    """
    while True:
        try:
            width = float(input("What is the width in centimeters: "))
            height = float(input("What is the height in centimeters: "))
            diagonal = sqrt(width ** 2 + height ** 2)
            # 1 inch = 2.54 cm
            inch = diagonal / 2.54
            print("")
            print(f"The book has {inch:.2f} inches.")
            print("")
        except:
            print("")
            print("This is all Folks!")
            break


centimetres_to_polegadas()
