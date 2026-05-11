"""Module for converting numbers into raindrop sounds."""


def convert(number):
    """Convert a number into raindrop sounds."""

    # Começamos com uma string vazia.
    # Aqui vamos guardar os sons encontrados.
    sounds = ""

    # Se o número for divisível por 3,
    # adicionamos "Pling" ao resultado.
    if number % 3 == 0:
        sounds += "Pling"

    # Se o número for divisível por 5,
    # adicionamos "Plang" ao resultado.
    if number % 5 == 0:
        sounds += "Plang"

    # Se o número for divisível por 7,
    # adicionamos "Plong" ao resultado.
    if number % 7 == 0:
        sounds += "Plong"

    # Se nenhum som foi adicionado,
    # significa que o número não é divisível por 3, 5 ou 7.
    # Nesse caso, retornamos o próprio número como texto.
    if sounds == "":
        return str(number)

    # Caso tenha algum som, retornamos o resultado.
    return sounds
