"""Módulo para simular as respostas do adolescente Bob."""


def response(hey_eyo):
    """Retorna a resposta do Bob baseada na frase de entrada."""
    # Remove espaços em branco, tabs e quebras de linha
    phrase = hey_eyo.strip()

    # Verifica se a frase está vazia (silêncio)
    if not phrase:
        return "Fine. Be that way!"

    # Verifica se há letras e se todas estão em maiúsculas (grito)
    is_shouting = phrase.isupper()
    # Verifica se o último caractere é um ponto de interrogação
    is_question = phrase.endswith("?")

    # Regra para pergunta gritada
    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"
    # Regra para apenas grito
    if is_shouting:
        return "Whoa, chill out!"
    # Regra para apenas pergunta
    if is_question:
        return "Sure."

    # Resposta padrão para qualquer outra situação
    return "Whatever."

