# Notas Musicais

from math import log2

print(' ')
print('='*70)
print(f'{"NOTA MUSICAL, OITAVA E FREQUÊNCIA DAS TECLAS DE UM PIANO":^70}')
print('='*70)
print('AS TECLAS DE UM PIANO TRADICIONAL VÃO DA 1° À 88° NOTA')
print(' ')
la = 27.5
notas = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B']
n = 1
q = 2
tecla = 1
while 1 <= tecla <= 88:
    print(' ')
    tecla = int(input('Digite uma tecla do piano entre 1° e a 88° tecla: '))
    while tecla < 1 or tecla > 88:
        print('O valor digitado não é um número válido da tecla de um piano!')
        tecla = int(input('Digite uma tecla do piano entre 1° e a 88° tecla: '))
    logaritmo = 1 + log2(2 ** ((tecla - 1) / 12))
    a = la * q ** (logaritmo - 1)
    b = 32.703
    c = 65.406
    print(f'A frequência da nota musical é {a:.3f} Hz.')
    while n <= 8:
        if tecla == 1:
            print('A nota está antes da 1° oitava do piano.')
            print('A nota é o A0.')
            break
        if tecla == 2:
            print('A nota está antes da 1° oitava do piano.')
            print('A nota é o A#0.')
            break
        if tecla == 3:
            print('A nota está antes da 1° oitava do piano.')
            print('A nota é o B0.')
            break
        if tecla == 88:
            print('A nota é o C8')
            break
        if b * (2 ** (n - 1)) <= a <= c * (2 ** (n - 1)):
            print(f'A nota está na {n}° oitava do piano.')
            print(f'A nota é o {notas[tecla - (4 * (1 + 3 * (n -1)))]}{n}.')
            break
        else:
            n += 1
    n = 0
    print(' ')
    continuar = input('Deseja Continuar [S/N]: ').upper()
    if 'S' not in continuar:
        break









