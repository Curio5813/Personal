from math import pi, e, sqrt


def admissao_numerica():
    """
    Relacionando os cojuntos dos numeros inteiros, racionais e irracionais
    com série infinita de soma de frações. Deduz se que o numeros trnascedentais
    acham numa soma de serie infinita de frações. O limite de uma função polinomial
    não permite soluções quando coeficeintes racionais pois o cojunto dos numeros
    reais é um corpo completo não algebricamente fechado. Para além dos numeros
    complexos criaria o conjunto dos numeros ordenados, como produtos cartesiano entre
    os numeros reais e o numeros complexos.
    :return:
    """
    a, soma, primo, denominador = 3, 1, 5659022821, 10396981210
    add_num = (((primo/denominador) * pi)/sqrt(e))
    # Soma da série de frações dos inversos dos cubos de 3. (1 + 1/3³ + 1/27³ + 1/19683³ ...)
    # A Série converge para 1.037138647
    for i in range(1, 10):
        soma += i/(a ** 3)
        a = a ** 3
    print(27 ** 3)
    print(f"{soma:.50f} {add_num:.50f}")


if __name__ == '__main__':
    admissao_numerica()
