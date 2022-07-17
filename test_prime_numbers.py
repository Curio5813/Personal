print('='*40)
print(f'{"SABER SE UM NÚMERO É PRIMO":^40}')
print('='*40)

s = 3
n = int(input('Digite um número: '))

if n == 2:
    print(f'O número {n} é primo')
if n == 3:
    print(f'O número {n} é primo')
if n != 2 and n % 2 == 0:
    print(f'O número {n} não é primo')
while n > s:
    if n % 2 == 1 and n % s == 0:
        print(f'O numero {n} não é primo')
        break
    if n % 2 == 1 and n % s != 0:
        s += 1
    if n == s and n % s == 0:
        print(f'O número {n} é primo')

