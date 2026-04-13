"""Verifica se um número é um número de Armstrong."""

def is_armstrong_number(numero):
    """Retorna True se o número for de Armstrong, senão False."""
    digitos = str(numero)
    quantidade_digitos = len(digitos)

    soma = 0
    for digito in digitos:
        soma += int(digito) ** quantidade_digitos

    return soma == numero