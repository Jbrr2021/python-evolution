def translate(text):
    # Separa o texto em palavras usando split()
    # Depois traduz cada palavra com translate_word()
    # Por fim, junta tudo novamente com espaço usando join()
    return " ".join(translate_word(word) for word in text.split())


def translate_word(word):
    # Define as vogais do inglês
    vowels = ("a", "e", "i", "o", "u")

    # REGRA 1:
    # Se a palavra começa com vogal,
    # ou começa com "xr" ou "yt",
    # apenas adicionamos "ay" no final
    if word.startswith(vowels) or word.startswith(("xr", "yt")):
        return word + "ay"

    # Percorre cada letra da palavra usando o índice i
    for i in range(len(word)):

        # REGRA 4:
        # Se encontrar a letra "y" depois de uma ou mais consoantes,
        # move tudo que vem antes do "y" para o final
        # e adiciona "ay"
        #
        # Exemplo:
        # my -> y + m + ay -> ymay
        # rhythm -> ythm + rh + ay -> ythmrhay
        if word[i] == "y" and i > 0:
            return word[i:] + word[:i] + "ay"

        # Verifica se a letra atual é uma vogal
        if word[i] in vowels:

            # REGRA 3:
            # Caso especial para palavras com "qu"
            # Se a vogal atual for "u" e antes dela tiver "q",
            # movemos tudo até o "u" para o final
            #
            # Exemplo:
            # quick -> ick + qu + ay -> ickquay
            # square -> are + squ + ay -> aresquay
            if word[i] == "u" and i > 0 and word[i - 1] == "q":
                return word[i + 1:] + word[:i + 1] + "ay"

            # REGRA 2:
            # Se encontrou uma vogal normal,
            # move as consoantes iniciais para o final
            # e adiciona "ay"
            #
            # Exemplo:
            # pig -> ig + p + ay -> igpay
            # chair -> air + ch + ay -> airchay
            return word[i:] + word[:i] + "ay"

    # Caso nenhuma regra anterior seja aplicada,
    # apenas adiciona "ay" no final da palavra
    return word + "ay"
