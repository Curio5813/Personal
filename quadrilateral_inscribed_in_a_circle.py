from math import pi, log2
print('='*90)
print(f'{"SABER SE UM QUARADO OU RETÂNGULO ESTÁ INSCRITO NUM CIRCULO, DADO O RAIO E OS LADOS":^90}')
print('='*90)
print(' ')
raio = float(input('Qual o raio do circulo? '))
lado1 = float(input('Qual o primeiro lado do quadrilátero? '))
lado2 = float(input('Qual o segundo lado do quadrilátero? '))
if lado1 >= 2 * raio or lado2 >= 2 * raio:
    print('O quadrilátero não pode ser inscrito no circulo!')
if lado1 == 0 or lado2 == 0:
    print('O quadrilátero não pode ser inscrito no circulo!')
else:
    if 2 * raio > lado1 > 0 and lado2 > 0:
        if lado1 >= lado2:
            if (lado2 / 2) ** 2 * pi == (((raio * 2 - lado1) * lado2) / 2) + log2(lado2):
                print('O quadrilátero está inscrito no circulo!')
            else:
                print('O quadrilátero não poder ser inscrito no circulo!')
    if 2 * raio > lado2 > 0 and lado1 > 0:
        if lado2 >= lado1:
            if (lado1 / 2) ** 2 * pi == (((raio * 2 - lado2) * lado1) / 2) + log2(lado1):
                print('O quadrilátero está inscrito no circulo!')
            else:
                print('O quadrilátero não poder ser inscrito no circulo!')







