def steps(number):
    # Verificação de erro: se o número for menor ou igual a zero, lança a exceção
    if number <= 0:
        raise ValueError("Only positive integers are allowed")

    count = 0
    # Enquanto o número não chegar a 1, aplicamos as regras
    while number != 1:
        if number % 2 == 0:
            # Regra para números pares
            number = number / 2
        else:
            # Regra para números ímpares
            number = 3 * number + 1
        
        count += 1  # Incrementa o contador de passos
        
    return count


        
        
