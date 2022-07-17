from datetime import datetime, timedelta
from time import sleep


def agesDifference():
    """
    This fucntion return the difference of ages between two people.
    :return:
    """
    ano_nasc = 1977
    ano_atual = datetime.now().year
    my_age = ano_atual - ano_nasc
    print("Hi, what's your name? ")
    sleep(2)
    nome = str(input('Hi there, my name is '))
    sleep(1.5)
    print(f"Cool {nome}! How old are you? ")
    sleep(2)
    your_age = int(input("I'm "))
    sleep(1.5)
    if my_age > your_age:
        return print(f'Hummm... you are {abs(my_age - your_age)} year(s) old newer than me.')
    if my_age == your_age:
        return print(f'Hooo! we have the same age.')
    if my_age < your_age:
        return print(f'Hummm... you are {abs(my_age - your_age)} year(s) older than me.')


agesDifference()
