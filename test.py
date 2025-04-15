from math import log, e, factorial, sqrt
import decimal


lim = 0
for i in range(1, 172):
    lim += log((i ** 2 + factorial(i - 1)) / sqrt(i ** 2 + 1))
    print(lim)