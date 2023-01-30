from math import sqrt


def sizeBooks():
    """
    This function calculates the size of a book in inches and prints
    out what type this book should be based on its size.
    :return:
    """
    inch = 2.54
    width = int(input("How wide is the book in mm: "))
    height = int(input("how long is the book in mm: "))
    screen = round(((sqrt(width ** 2 + height ** 2))/10)/inch, 2)
    print(screen)
    if 8 <= screen <= 8.4:
        print(f"This is a Pocket Book. The best reading is in a screen with 8 inches.")
    elif 10 <= screen <= 10.12:
        print(f"This is a Romance Book. The best reading is in a screen with 10 inches.")
    elif 11 <= screen <= 11.4:
        print(f"This is a Childish Book. The best reading is in a screen with 11 inches.")
    elif 13.9 <= screen <= 14:
        print(f"This is a Art Book. The best reading is in a screen with 14 inches.")
    else:
        print("Miscellaneous book formats.")


sizeBooks()
