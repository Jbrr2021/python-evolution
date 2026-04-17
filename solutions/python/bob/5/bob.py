"""Módulo otimizado para as respostas do Bob usando lógica aninhada."""


def response(hey_bob):
    """
    Retorna a resposta do Bob usando uma abordagem de decisão aninhada
    para maximizar a performance e evitar repetições.
    """
    # rstrip() é suficiente aqui, pois apenas o espaço à direita afeta o '?'
    phrase = hey_bob.rstrip()

    if not phrase:
        return "Fine. Be that way!"

    is_shout = phrase.isupper()
    is_question = phrase.endswith("?")

    # Abordagem aninhada: mais rápida por evitar verificações redundantes
    if is_shout:
        if is_question:
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"

    if is_question:
        return "Sure."

    return "Whatever."

