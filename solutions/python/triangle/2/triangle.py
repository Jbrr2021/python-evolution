"""Classifica triângulos como equilátero, isósceles ou escaleno."""

def _is_valid_triangle(sides):
    """Verifica se os lados formam um triângulo válido."""
    if any(side <= 0 for side in sides):
        return False

    shortest_side, middle_side, longest_side = sorted(sides)
    return shortest_side + middle_side >= longest_side


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