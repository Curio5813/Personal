print('='*80)
print('Dados três segmentos saber se formam triângulos e se são triângulos retângulos')
print('='*80)

a = int(input('Digite o valor do primeiro cateto: '))
b = int(input('Digite o valor do segundo cateto: '))
c = int(input('Digite o valor da hipotenusa: '))
if (a + b > c) and (a + c > b) and (b + c > a):
    print('Formam triângulos')
    if ((a**2) + (b**2)) == (c**2):
        print('Formam triângulo retângulo')
    if ((a**2)) + (b**2) != (c**2):
        print('Não formam triângulo retângulo')
else:
    print('Não formam triângulos')
