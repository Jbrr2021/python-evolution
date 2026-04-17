"""Módulo otimizado para as respostas do Bob usando lógica aninhada."""


def response(hey_bob):
    """Retorna a resposta do Bob usando uma abordagem de decisão aninhada."""
    phrase = hey_bob.rstrip()

    if not phrase:
        return "Fine. Be that way!"

    is_shout = phrase.isupper()
    is_question = phrase.endswith("?")

    if is_shout:
        if is_question:
            return "Calm down, I know what I'm doing!"
        return "Whoa, chill out!"

    if is_question:
        return "Sure."

    return "Whatever."
