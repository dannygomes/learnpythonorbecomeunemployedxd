def equilateral(sides):
    a, b, c = sides
    if not is_valid_triangle(a, b, c):
        return False

    return a == b and b == c


def isosceles(sides):
    a, b, c = sides
    if not is_valid_triangle(a, b, c):
        return False

    return a == b or b == c or a == c


def scalene(sides):
    a, b, c = sides
    if not is_valid_triangle(a, b, c):
        return False

    return a != b and b != c and c != a


def is_valid_triangle(a, b, c):
    return a + b >= c and b + c >= a and a + c >= b and a > 0 and b > 0 and c > 0
