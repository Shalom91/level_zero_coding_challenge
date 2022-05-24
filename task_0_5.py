import math


def area_of_triangle(length_side_1, length_side_2, length_side_3):
    """
    calculate the area of a triangle using the
    length of each side
    """
    semiperimeter = (1 / 2) * (length_side_1 + length_side_2 + length_side_3)
    area = math.sqrt(
        semiperimeter
        * (semiperimeter - length_side_1)
        * (semiperimeter - length_side_2)
        * (semiperimeter - length_side_3)
    )

    return int(area)
