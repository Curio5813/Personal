# Sequência de Fibonacci

a = 0
p = 1
s = 1
print('='*47)
print('Sequência de Fibonacci (Os 20 primeiros termos)')
print('='*47)
print()
for i in range(1, 20):
    s = a
    a = p
    p = a + s
    print(s, end=' ->  ')
print()


