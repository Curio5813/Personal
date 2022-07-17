from time import sleep
print('Conta a lenda que o xadrez foi inventado na Índia, há mais de 1500 anos.')
sleep(3)
print('O rei ficou tão fascinado com a invenção e as infinitas variações de movimentos, que resolveu recompensar o inventor.')
sleep(3)
print('O rei perguntou: O que você quer de recompensa?')
sleep(3)
print('Inventor: Quero um grão de arroz para a primeira casa, dois grãos para a segunda casa, 4 para a terceira, e assim sucessivamente.')
sleep(3)
print('“Só isso?”, o rei retrucou.')
sleep(3)
print('Então, o rei pediu para os matemáticos do reino fazerem as contas.')
sleep(3)
print('Quantos grãos de arroz eram necessários?')
a = 1
q = 2
b = a * q ** (64 - 1)
sleep(5)
print(f'São necessários {b} grãos de arroz para o preencher as 64 casas do tabuleiro')
sleep(3)
print('Se o inventor pedisse um número de casas do tabuleiro diferente, quantos grãos de arroz são necessários para o número de casas pedida? ')
casas = int(input('Para o número de casas igual a: '))
a = 1
q = 2
b = a * q ** (casas - 1)
print(f'O número de grãos de arroz é igual a {b}')




