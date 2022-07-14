from random import randint
print('='*65)
print(f'{"Tente advinhar o numero que o computador escolheu de 1 até 10":^65}')
print('='*65)
Computador = randint(1, 10)
Jogador = int(input('Escolha um número de 1 á 10: '))
if Jogador == Computador:
    print(f'Você venceu!!! Advinhou o número. O compuatdor jogou {Computador}')
if Jogador != Computador:
    print(f'Você perdeu!!! O compuatdor jogou {Computador}')






