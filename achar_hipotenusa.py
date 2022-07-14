from math import sqrt

def acharHipotenusa():
    """
    Esta função retorna o valor da hipotenusa de um triangulo
    retângulo, dados os dois catetos.
    :return:
    """
    a = float(input('Cateto A: '))
    b = float(input('Cateto B: '))
    c = sqrt(a ** 2 + b ** 2)
    print('')
    return print(f'Hipotenusa: {c:.1f}')


acharHipotenusa()
