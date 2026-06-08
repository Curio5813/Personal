from math import sqrt

a = 0
b = 1
c = 1
for i in range(1, 1_000_001):
    a += i
    b += (1/i)
    c += sqrt(i)
    print(a, b, c)
print(a/(c/b))

