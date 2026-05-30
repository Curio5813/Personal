import math


def tijolo_de_euler():
    """
    Cálculo dos inteiros das arestas e diagonais de um paralelepipado regular.
    :return:
    """
    h = 115
    r = 15

    volume_cilindro = math.pi * r ** 2 * h
    volume_cone = math.pi * r ** 2 + math.pi * r * math.sqrt(r ** 2 + h ** 2)
    volume_cubo = (2 / 3) * volume_cilindro
    diagonal_espacial_cubo = volume_cubo ** (1 / 3) * math.sqrt(3)
    volume_esfera_inscrita_cubo = (math.pi / 6) * volume_cubo
    raio_semicirculo_da_esfera = diagonal_espacial_cubo / 2 * math.sqrt(3)
    area_semicirculo_da_esfera = (math.pi * r ** 2) / 2
    aresta_cubo = volume_cubo ** (1 / 3)
    diagonal_menor_tijolo = (2 / 3) * aresta_cubo
    diagonal_maior_tijolo = (5 / 3) * diagonal_menor_tijolo
    digonal_intermediaria_tijolo = (50 * math.pi) / 15
    a = math.sqrt(diagonal_menor_tijolo ** 2 + digonal_intermediaria_tijolo ** 2 - diagonal_maior_tijolo ** 2)
    b = math.sqrt(diagonal_menor_tijolo ** 2 + diagonal_maior_tijolo ** 2 - digonal_intermediaria_tijolo ** 2)
    c = math.sqrt(digonal_intermediaria_tijolo ** 2 + diagonal_maior_tijolo ** 2 - diagonal_menor_tijolo ** 2)
    g = math.sqrt(diagonal_menor_tijolo ** 2 + digonal_intermediaria_tijolo ** 2 + diagonal_maior_tijolo ** 2)
    print(a, b, c, g)


tijolo_de_euler()
