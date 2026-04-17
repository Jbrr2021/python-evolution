"""Módulo para simular as respostas do adolescente Bob."""


def response(hey_eyo):
    """Retorna a resposta do Bob baseada na frase de entrada."""
    phrase = hey_eyo.strip()

    if not phrase:
        return "Fine. Be that way!"

    is_shouting = phrase.isupper()
    is_question = phrase.endswith("?")

    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"
    if is_shouting:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."

    return "Whatever."
