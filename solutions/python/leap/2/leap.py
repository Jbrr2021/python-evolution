"""Verifica se um ano é bissexto no calendário gregoriano."""
def leap_year(year):
    """Retorna True se o ano for bissexto, False caso contrário."""
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)
