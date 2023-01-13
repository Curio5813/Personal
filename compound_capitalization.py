from math import e


def compoundCapitalization():
    """
    This function return the average earning in an investment by
    compound capitalization using the Euler Number as the rate
    investment.
    :return:
    """
    print('='*50)
    print(f'{"PROBABLE INVESTMENT REMUNERATION RATE".center(50)}')
    print('='*50)
    print('')
    print(f"Euler's Number is {e:.4f}. It's used to determinate the payment rate.")
    print('')
    rate = e / 100
    print(f"the rate is {rate:.4f}% per month")
    capital = float(input("How much capital do you want to invest? "))
    time = int(input('For how long do you want it invested? '))
    print('')
    amount = 0
    for i in range(time):
        amount += capital * (1 + rate / 100)
        capital = amount
    print(f"The amount earned is {amount:.2f} R$")


compoundCapitalization()
text = 'Canterbury never fall!'
print('')
print(text)
