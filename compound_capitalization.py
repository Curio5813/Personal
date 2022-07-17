def compoundCapitalization():
    """
    This function return the average earning in a investiment by
    compound capitalization using the Euler Number as the rate
    investiment.
    :return:
    """
    print('='*50)
    print(f'{"PROBABLE INVESTMENT REMUNERATION RATE".center(50)}')
    print('='*50)
    print('')
    aprox_euler_numeber = 1_000_000
    n = aprox_euler_numeber
    e = (1 + (1 / n)) ** n
    print(f"Euler's Number is {e:.4f}. It's used to determinated the payment rate.")
    print('')
    rate = ((1 + (e / 100)) - 1) * 100
    print(f"the rate is {rate:.4f} % per month")
    capital = float(input("How much capital do you want to invest? "))
    time = int(input('For how long do you want it invested? '))
    print('')
    amount = capital * (1 + (rate / 100)) ** time
    interest = amount - capital
    print(f"The amount earned is {amount:.2f} R$")
    print(f'The interest earned on the aplication is {interest:.2f} R$')


compoundCapitalization()
text = 'Canterbury never fall!'
