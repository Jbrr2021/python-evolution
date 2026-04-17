"""Module to simulate Bob's responses."""

def response(hey_eyo):
    # Remove espaços em branco (inclusive tabs e quebras de linha)
    phrase = hey_eyo.strip()

    # 1. Silêncio
    if not phrase:
        return "Fine. Be that way!"

    # 2. Critérios de Grito e Pergunta
    is_shouting = phrase.isupper()
    is_question = phrase.endswith('?')

    # 3. Regras de decisão
    if is_shouting and is_question:
        return "Calm down, I know what I'm doing!"
    if is_shouting:
        return "Whoa, chill out!"
    if is_question:
        return "Sure."
    
    # 4. Padrão
    return "Whatever."

