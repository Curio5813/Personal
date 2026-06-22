from math import e


def capitalizacoes_instantaneas_vs_composta():
    """
    O programafaz uma comparação entre uma Capitalização Composta sobre Capitalizações
    Instantaneas, e a diferença do retorno aplicado. Lembrando que na capitalização instatanea
    os prazos sao infinitessimais, os rendimentos acontecem em milisegunedos de milisegindo, sem
    parar.
    :return:
    """
    largura = 70
    titulo = "CAPITALIZAÇÃO COMPOSTAS VS. CAPITALIZAÇÃO INSTATÂNEAS"
    print("=" * largura)
    print(titulo.center(largura))
    print("=" * largura)

    v = float(input("Qual o valor da aplicação (R$): ".upper()))
    r = float(input("Qual a taxa de juros da aplicação (%): ".upper()))
    t = int(input("Qual o prazo da aplicação: ".upper()))
    n = int(input("Qual a forma de capitalização: ".upper()))
    tipo = input("Tipo: ")

    r /= 100

    composta = v * (1 + (r/n))**(n*t)
    instantaneas = v * e**(r*t)

    print("\n")
    print("=" * largura)
    print(titulo.center(largura))
    print("=" * largura)
    print(f"CAPITALIZAÇÃO COMPOSTA {tipo.upper()}: R$ {composta:.2f}")
    print(f"CAPITALIZAÇÃO INSTANTANEA: R$ {instantaneas:.2f}")

    print(f"A diferença da instatânea para a composta é de: R$ {instantaneas - composta:.2f}".upper())


capitalizacoes_instantaneas_vs_composta()
