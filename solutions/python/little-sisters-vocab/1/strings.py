"""Functions for practicing prefixes, suffixes, and string manipulation."""


def add_prefix_un(word):
    """Add the prefix 'un' to the given word."""

    # Junta o prefixo "un" com a palavra recebida.
    return "un" + word


def make_word_groups(vocab_words):
    """Apply a prefix to a group of words and return them separated by ' :: '."""

    # A primeira posição da lista é o prefixo.
    prefix = vocab_words[0]

    # Usa join para juntar as palavras.
    # Exemplo:
    # ["en", "close", "joy"] vira:
    # "en :: enclose :: enjoy"
    return f" :: {prefix}".join(vocab_words)


def remove_suffix_ness(word):
    """Remove the suffix 'ness' from a word."""

    # Remove os últimos 4 caracteres da palavra: "ness".
    root_word = word[:-4]

    # Se a palavra ficou terminando com "i",
    # isso significa que provavelmente veio de uma palavra terminada em "y".
    # Exemplo:
    # happiness -> happi -> happy
    if root_word.endswith("i"):
        return root_word[:-1] + "y"

    # Caso contrário, retorna apenas a palavra sem "ness".
    return root_word


def adjective_to_verb(sentence, index):
    """Extract an adjective from a sentence and turn it into a verb."""

    # Divide a frase em palavras.
    words = sentence.split()

    # Pega a palavra na posição indicada.
    adjective = words[index]

    # Remove o ponto final, se existir.
    adjective = adjective.strip(".")

    # Adiciona o sufixo "en".
    return adjective + "en"