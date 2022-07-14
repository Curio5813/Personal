# A letra 'a' em meu nome


from math import log2, pi
print('='*30)
print(f'{"A LETRA a EM MEU NOME":^30}')
print('='*30)
n = 3.154000000000
a = (1 + (1/log2(n-1))**((n-2)*pi))
phi = (1 + (5**(1/2)))/2

my_dict = {'chave1': 'Olá, mundo', 'chave2': [2, 3, 5, 7, 11], 'chave3': a}
print(' ')
print(f'Todo número inteiro maior que 1 é a razão da letra a pela letra l dado por {a:.6f}')
print(f"Em qualquer dicionário latino a razão da letra 'a' em relação a letra 'l' é dado por {my_dict['chave3']:.6f}")
print(f'O número de ouro é igual a {phi:.6f}')
print(f'A diferença de "a" em meu nome pelo número de ouro é {(a - phi)*100:.2f}%')
print('Justamente o percentual de W e Z nos vocábulos latinos')
print(' ')
print('Isso explica por que que o céu é azul!'.upper())











