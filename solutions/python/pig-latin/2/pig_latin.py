"""Module for translating English text into Pig Latin."""


def translate(text):
    """Translate a text from English to Pig Latin."""
    return " ".join(translate_word(word) for word in text.split())


def translate_word(word):
    """Translate a single word from English to Pig Latin."""
    vowels = ("a", "e", "i", "o", "u")

    # Regra 1:
    # Se a palavra começa com vogal, "xr" ou "yt",
    # apenas adicionamos "ay" no final.
    if word.startswith(vowels) or word.startswith(("xr", "yt")):
        return word + "ay"

    # Percorre cada letra da palavra.
    # O enumerate retorna a posição e a letra ao mesmo tempo.
    for position, letter in enumerate(word):

        # Regra 4:
        # Se encontrar "y" depois de uma ou mais consoantes,
        # o "y" funciona como som de vogal.
        if letter == "y" and position > 0:
            return word[position:] + word[:position] + "ay"

        # Verifica se a letra atual é uma vogal.
        if letter in vowels:

            # Regra 3:
            # Caso especial para palavras com "qu".
            # Exemplo:
            # quick -> ickquay
            # square -> aresquay
            if letter == "u" and position > 0 and word[position - 1] == "q":
                return word[position + 1:] + word[:position + 1] + "ay"

            # Regra 2:
            # Move as consoantes iniciais para o final
            # e adiciona "ay".
            return word[position:] + word[:position] + "ay"

    # Caso nenhuma regra seja aplicada,
    # apenas adiciona "ay" no final.
    return word + "ay"
