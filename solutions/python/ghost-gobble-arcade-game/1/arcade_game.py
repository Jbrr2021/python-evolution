"""Regras básicas do jogo Pac-Man."""

def eat_ghost(power_pellet_active, touching_ghost):
    """Retorna True se o Pac-Man puder comer o fantasma."""
    return power_pellet_active and touching_ghost


def score(touching_power_pellet, touching_dot):
    """Retorna True se o Pac-Man marcar pontos."""
    return touching_power_pellet or touching_dot


def lose(power_pellet_active, touching_ghost):
    """Retorna True se o Pac-Man perder o jogo."""
    return touching_ghost and not power_pellet_active


def win(has_eaten_all_dots, power_pellet_active, touching_ghost):
    """Retorna True se o Pac-Man vencer o jogo."""
    return has_eaten_all_dots and not lose(power_pellet_active, touching_ghost)