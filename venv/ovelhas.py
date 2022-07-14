while True:
    print('=' * 110)
    titulo = 'CRIAÇÃO DE OVELHAS'
    print(titulo.center(110))
    print('=' * 110)
    print('')
    iniciar = str(input('Deseja iniciar análise? \n'
                        'S - Sim;\n'
                        'N - Não;\n'
                        'opção: '))
    if iniciar in 'Nn':
        print('')
        print('Fim do Programa!')
        break
    print('')
    qt = int(input('Quantas ovelhas você iniciou sua criação? '))
    anos = int(input('Quantos anos tem sua criação? '))
    print('')
    op = 1
    comp_burr = str(input('Comprou Burregas?\n'
                          'S - Sim\n'
                          'N - Não\n'
                          'opção: '))
    if comp_burr in 'Ss':
        comp_burr_qt = int(input('Quantas Burregas comprou? '))
    print('')
    while True:
        op = int(input('Digite uma opção:\n'
                       '1 - Número de Ovelhas;\n'
                       '2 - Número de Burregas;\n'
                       '3 - Valor Total das Ovelhas;\n'
                       '4 - Valor Total das Burregas;\n'
                       '5 - Número total de Ovelhas Vendidas;\n'
                       '6 - Número total de Burregas Vendidas;\n'
                       '7 - Número de Burregas até 1 ano;\n'
                       '8 - Número de Burregas até 2 anos;\n'
                       '9 - Número de Burregas com 3 anos;\n'
                       '10 - Valor Total das Vendas;\n'
                       '11 - Valor Médio de Ganho Anual;\n'
                       '12 - Valor Médio de Ganho Mensal;\n'
                       '13 - Número Total de Ovelhas e Burregas;\n'
                       '14 - Valor Total do Rebanho;\n'
                       '0 - Sair;\n'
                       'opção: '))

        if op == 0:
            print('')
            print('Fim da Análise!')
            break

        def criacaoOvelhas(qt, anos):
            ov, burr, burr_valor, venda_burr, venda_ov, cont, ind = \
                [], [], [], [], [], 0, 2
            if anos == 0:
                ov.append(qt)
                if comp_burr in 'Ss':
                    burr.append(comp_burr_qt)
            elif anos > 0:
                ov.append(qt)
                if comp_burr in 'Ss':
                    burr.append(comp_burr_qt)
                while cont < anos:
                    burr.append(2 * sum(ov))
                    cont += 1
                    if cont == 1 and len(burr) == 2:
                        ov.append(burr[0])
                        burr.pop(0)
                    if cont >= 3:
                        burr_valor.append(burr[0])
                        burr[0] = int(burr_valor[0] / 2)
                        venda_burr.append(burr[0])
                    if cont >= 4:
                        ov.append(burr[0])
                        burr.pop(0)
                while sum(ov) > 50:
                    venda_ov.append(ov[0])
                    ov.pop(0)
            print('')
            if op == 1:
                print(f'As quantidades de ovelhas é de {sum(ov)}')
            elif op == 2:
                print(f'A quantidade de burregas é de {sum(burr)}')
            elif op == 3:
                print(f'O valor total das ovelhas é de R${sum(ov) * 500:.2f}')
            elif op == 4:
                print(f'O valor total das burregas é de R${sum(burr) * 400:.2f}')
            elif op == 5:
                print(f'O número de ovelhas vendidas é(são) de {sum(venda_ov)}')
            elif op == 6:
                print(f'O número de burregas vendidas é(são) de {sum(venda_burr)}')
            elif op == 7:
                print(f'O número de burregas com até 1 ano é de {burr[0]}')
            elif op == 8:
                print(f'O número de burregas com 2 anos é de {burr[1]}')
            elif op == 9:
                print(f'O número de burregas com 3 anos {burr[2]}')
            elif op == 10:
                print(f'O valor total das vendas é de '
                      f'R${sum(venda_ov) * 500 + sum(venda_burr) * 400:.2f} em {anos} anos')
            elif op == 11 and comp_burr in 'Ss':
                print(f'Valor médio de ganho anual '
                      f'R${((sum(venda_ov) * 500 + sum(venda_burr) * 400) - (comp_burr_qt * 400))/ anos:.2f}')
            elif op == 11 and comp_burr in 'Nn':
                print(f'Valor médio de ganho anual '
                      f'R${(sum(venda_ov) * 500 + sum(venda_burr) * 400)/ anos:.2f}')
            elif op == 12 and comp_burr in 'Ss':
                print(f'Valor médio de ganho mensal '
                      f'R${((sum(venda_ov) * 500 + sum(venda_burr) * 400) - (comp_burr_qt * 400))/ (anos * 12):.2f}')
            elif op == 12 and comp_burr in 'Nn':
                print(f'Valor médio de ganho mensal '
                      f'R${(sum(venda_ov) * 500 + sum(venda_burr) * 400)/ (anos * 12):.2f}')
            elif op == 13:
                print(f'O número total de Ovinos é {sum(ov) + sum(burr)}')
            elif op == 14:
                print(f'O valor total do rebanho é de R${sum(ov) * 500 + sum(burr) * 400:.2f}')
            return ''


        print(criacaoOvelhas(qt, anos))
