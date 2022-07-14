print('='*45)
print('TAXA DE REMUNERÇÃO PROVÁVEL DE INVESTIMENTOS')
print('='*45)
print(' ')
n = 1000000000
e = (1 + (1/n))**n
capital = float(input('Qual o capital a ser investido? R$'))
periodo = int(input('Quantos meses será a aplicação? '))
print(' ')
montante = capital*(1 + (e/100))**periodo
juros = montante - capital
print(f'O valor acumulado é de R${montante:.2f}')
print(f'O valor dos com ganhos de juros da aplicação é de R${juros:.2f}')
print(' ')
print(f'O número de Euler {e}')







