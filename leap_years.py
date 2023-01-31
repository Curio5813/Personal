def leapYears():
    """
    This function calculate the leap years.
    :return:
    """
    year = int(input("Digit a year: "))
    if year % 400 == 0 or year % 4 == 0 and year % 100 != 0:
        print("Its year is a leap year.")
    else:
        print("Its nothing a leap year.")


leapYears()
