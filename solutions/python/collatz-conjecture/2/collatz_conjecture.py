"""Módulo para calcular os passos da Conjectura de Collatz."""

def steps(number):
    """Calcula o número de passos para chegar a 1 seguindo as regras de Collatz.

    :param number: int - O número inicial (deve ser positivo).
    :return: int - Total de passos realizados.
    :raises ValueError: Se o número for zero ou negativo.
    """
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    while number != 1:
        if number % 2 == 0:
            number //= 2
        else:
            number = 3 * number + 1
        count += 1
    return count
    