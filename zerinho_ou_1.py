from random import randint
print('-'*35)
print('JOGO DA ADVINHAÇÃO DO ZERINHO OU 1')
print('-'*35)
escolhap = int(input('Pedro escolhe: '))
if escolhap == 0:
    escolhapc = 1
    print(f'Computador escolhe {escolhapc}')
if escolhap == 1:
    escolhapc = 0
    print(f'Computador escolhe {escolhapc}')
jogadap = int(input('Pedro joga: '))
jogadapc = randint(0, 1)
while escolhap == 0:
    if jogadap == 0 and jogadapc == 0:
        print(f'Computador jogou {jogadapc}. Pedro venceu!!!')
        break
    if (jogadap == 0 and jogadapc == 1) or (jogadap == 1 and jogadapc == 0):
        print(f'Computador jogou {jogadapc}. Ninguém venceu!!!')
        break
    if jogadap == 1 and jogadapc == 1:
        print(f'Computador jogou {jogadapc}. O computador venceu')
        break
while escolhap == 1:
    if jogadap == 1 and jogadapc == 1:
        print(f'Computador jogou {jogadapc}. Pedro venceu!!!')
        break
    if (jogadap == 1 and jogadapc == 0) or (jogadap == 0 and jogadapc == 1):
        print(f'Computador jogou {jogadapc}. Ninguém venceu!!!')
        break
    if jogadap == 0 and jogadapc == 0:
        print(f'Computado jogou {jogadapc}. Computador venceu!!!')
        break
