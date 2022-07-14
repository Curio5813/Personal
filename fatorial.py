print('-'*30)
print(f'{"CALCULANDO FATORIAL":^30}')
print('-'*30)

fatorial = int(input('Calucule o fatorial de: '))
n = 1
fat = 1
while n <= fatorial:
    fat = fat * n
    n += 1
print(fat)


