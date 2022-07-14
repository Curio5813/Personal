"""
Faça um programa que dado um número criar o Triangulo de Pascal.
"""


def binomio_de_newton(n=int(input('Digite um número igual ou maior que 1: '))):
    fat_n = 1
    fat_k = 1
    k = 0
    while n <= 0:
        print('')
        print('Número inválido!')
        n = int(input('Digite um número igual ou maior que 1: '))
    while n >= 1:
        fat_n *= n
        n -= 1



