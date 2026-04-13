"""Grains exercise solution."""

def square(number):
    """Return the number of grains on a given square."""
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    return 2 ** (number - 1)


def total():
    """Return the total number of grains on the chessboard."""
    return 2 ** 64 - 1

# Exemplos de uso
print("Grãos na casa 1:", square(1))
print("Grãos na casa 2:", square(2))
print("Grãos na casa 3:", square(3))
print("Grãos na casa 4:", square(4))
print("Total de grãos no tabuleiro:", total())