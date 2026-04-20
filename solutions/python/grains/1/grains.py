def square(number):
    # Verifica se o número da casa está dentro do intervalo permitido
    # O tabuleiro de xadrez vai da casa 1 até a casa 64
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")
    
    # Calcula a quantidade de grãos na casa informada
    # A cada casa, o valor dobra:
    # casa 1 = 2^(1-1) = 1
    # casa 2 = 2^(2-1) = 2
    # casa 3 = 2^(3-1) = 4
    # casa 4 = 2^(4-1) = 8
    return 2 ** (number - 1)


def total():
    # Calcula o total de grãos no tabuleiro inteiro
    # Fórmula da soma da progressão geométrica:
    # 1 + 2 + 4 + 8 + ... + 2^63
    # Resultado = 2^64 - 1
    return 2 ** 64 - 1


# Exemplos de uso
print("Grãos na casa 1:", square(1))
print("Grãos na casa 2:", square(2))
print("Grãos na casa 3:", square(3))
print("Grãos na casa 4:", square(4))
print("Total de grãos no tabuleiro:", total())