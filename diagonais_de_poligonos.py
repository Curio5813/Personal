print('='*30)
print(f'{"DIAGONAIS DE POLÍGONOS":^30}')
print('='*30)
print(' ')
for i in range(3, 35):
    lados = i
    diagonais_por_vertices = lados - 3
    total_diagonais = (lados * diagonais_por_vertices)/2
    print(f'{total_diagonais:.0f}', end='  ')





