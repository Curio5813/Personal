print('='*60)
print(f'{"ACHAR A MATRIZ INVERSA DE UMA MATRIZ QUADRADA DADA":^60}')
print('='*60)

matrix = []
list0 = []
list1 = []
n = 2
while len(list0) < 2:
    elementos = float(input(f'Digite um número inteiro para a matriz {n} x {n}: '))
    list0.append(elementos)
while len(list1) < 2:
    elementos = float(input(f'Digite um número inteiro para a matriz {n} x {n}: '))
    list1.append(elementos)
matrix.append(list0)
matrix.append(list1)
print(list0)
print(list1)
lst_inversa1 = []
lst_inversa2 = []
inversa = []
print(' ')
numero1 = float(input('Digite um número: '))
numero2 = float(input('Digite outro número: '))
numero3 = float(input('Digite mais número: '))
numero4 = float(input('Digite o ultimo número: '))
while numero1 * matrix[0][0] + numero2 * matrix[1][0] != 1 or numero1 * matrix[0][1] + numero2 * matrix[1][1] != 0:
    print('Tente novamente!')
    numero1 = float(input('Digite um número: '))
    numero2 = float(input('Digite outro número: '))
while numero3 * matrix[0][0] + numero4 * matrix[1][0] != 0 or numero3 * matrix[0][1] + numero4 * matrix[1][1] != 1:
    print('Tente novamente!')
    numero3 = float(input('Digite mais número: '))
    numero4 = float(input('Digite o ultimo número: '))
lst_inversa1.append(numero1)
lst_inversa1.append(numero2)
lst_inversa2.append(numero3)
lst_inversa2.append(numero4)
print('A matriz inversa é!')
print(lst_inversa1)
print(lst_inversa2)














