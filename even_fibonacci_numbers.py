a = 0
p = 1
s = 1
soma = 0
print('=-'*37)
print('Os primeiros números pares da sequência de Fibonacci menor que 5 trilhões')
print('=-'*37)
print()
while s <= 5000000000000:
    s = a
    a = p
    p = a + s
    if s > 5000000000000:
        break
    if s % 2 == 0:
        soma = soma + 1
        print(s, end='  ')
print()
print()
print(f'Total de números pares na Sequência de Fibonacci menor ou igual a 5 Trilhões é igual a {soma}')


