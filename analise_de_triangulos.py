print('='*22)
print('ANÁLISE DE TRIÂNGULOS')
print('='*22)

a = int(input('Digite o valor do primeiro segmenento: '))
b = int(input('Digite o valor do segundo segmento: '))
c = int(input('Digite o valor do ultimo segmento: '))

if (a + b > c) and (a + c > b) and (b + c > a):
    print('É possível formar triânguloes')
    if a == b == c:
        print('Formam triângulos equiláteros')
    if (a == b and a != c) or (a == c and a != b) or (b == c and b != a):
        print('Formam triângulos isóceles')
    if a != b and b != c and c != a:
        print('Formam triângulos escalenos')
else:
    print('Não é possível formar triângulos')



