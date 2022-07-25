from math import pi, log2


def quadrilateralIncribeInACircle():
    """
    This function has as the return if a quadrilateral can or
    not can be inscribed in a circle given the ray of the circle
    and the sides of the quadrilateral.
    :return:
    """
    print("=" * 90)
    print(f"find if a quadrilateral can or not can be inscribed in a circle".center(90).upper())
    print("=" * 90)
    print("")
    ray = float(input("Enter the ray of the circle: "))
    side1 = float(input("Enter the first side: "))
    side2 = float(input("Enter the second side: "))
    if side1 > 2 * ray or side2 > 2 * ray:
        print("The quadrilateral can not be inscribed into the cricle")


quadrilateralIncribeInACircle()
