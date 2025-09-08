import pygame
from time import sleep


def tocando_nininho():
    """
    Testando música com o pygame.
    :return:
    """
    pygame.mixer.init()
    pygame.mixer.music.load('musica_001.mp3')
    pygame.mixer.music.play()
    while True:
        string = ("Amigo Otto onde está você?\n"
                  "Aquilo que não nos mata nos torna mais forte.")
        for i in string:
            print(i, end="")
            sleep(0.2)
        print("")
        print("=============================================")



tocando_nininho()
