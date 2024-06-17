from math import factorial


def factorial_question_01():
    """
    Math Olympiad Question
    :return:
    """
    for i in range(0, 10000):
        if factorial(i) == factorial(10) / factorial(6):
            print(i)


factorial_question_01()
