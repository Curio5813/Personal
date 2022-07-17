print('='*25)
print('FÔRMULA DE BÁSKARA')
print('='*25)
print('EQUAÇÃO GERAL DO 2º GRAU: ax² + bx + c = 0')
print(' ')

a = float(input('Digite um número para o coeficiente a: '))
b = float(input('Digite um número para o coeficiente b: '))
c = float(input('Digite um número para o coeficiente c: '))

delta = b ** 2 - 4 * a * c
if delta >= 0:
    if delta == 0:
        print('Existe apenas uma raiz real!')
    if delta > 0:
        print('Existem duas raizes reais!')
else:
    print('Não existem raizes reais!')

if delta >= 0:
    if delta == 0:
        x1 = - b / 2 * a
        print(f'A única raiz real é {x1}')
    if delta > 0:
        x1 = (- b - (delta ** (1/2)))/2 * a
        x2 = (- b + (delta ** (1/2)))/2 * a
        print(f'As duas raizes reais são: {x1:.1f} e {x2:.1f}')



