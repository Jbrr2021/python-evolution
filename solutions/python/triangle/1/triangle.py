"""Classifica triângulos como equilátero, isósceles ou escaleno."""

def _is_valid_triangle(sides):
    """Verifica se os lados formam um triângulo válido."""
    a, b, c = sides
    return (
        a > 0 and b > 0 and c > 0
        and a + b >= c
        and b + c >= a
        and a + c >= b
    )


def equilateral(sides):
    """Retorna True se o triângulo for equilátero."""
    if not _is_valid_triangle(sides):
        return False
    return sides[0] == sides[1] == sides[2]


def isosceles(sides):
    """Retorna True se o triângulo for isósceles."""
    if not _is_valid_triangle(sides):
        return False
    return (
        sides[0] == sides[1]
        or sides[1] == sides[2]
        or sides[0] == sides[2]
    )


def scalene(sides):
    """Retorna True se o triângulo for escaleno."""
    if not _is_valid_triangle(sides):
        return False
    return (
        sides[0] != sides[1]
        and sides[1] != sides[2]
        and sides[0] != sides[2]
    )