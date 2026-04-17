"""Solução para o desafio de Mitigação de Colapso"""
def is_criticality_balanced(temperature, neutrons_emitted):
    """Verificar se o reator está balanceado em criticidade."""
    produto = temperature * neutrons_emitted
    return (temperature < 800 and 
           neutrons_emitted > 500 and
           produto < 500000)
    
def reactor_efficiency(voltage, current, theoretical_max_power):
    """Determina a faixa de eficiência de saída do reator."""
    generated_power = voltage * current
    efficiency = (generated_power / theoretical_max_power) * 100
    if efficiency >= 80:
        return 'green'
    elif efficiency >= 60:
        return 'orange'
    elif efficiency >= 30:
        return 'red'
    else:
        return 'black'

def fail_safe(temperature, neutrons_produced_per_second, threshold):
    """Mecanismo à prova de falha para evitar sobrecarga."""
    valor_atual = temperature * neutrons_produced_per_second

    # 90% do limite
    limite_baixo = 0.9 * threshold
    # Faixa normal: entre 90% e 110% do limite (threshol +/- 10%)
    limite_alto = 1.1 * threshold

    if valor_atual < limite_baixo:
        return 'LOW'
    elif limite_baixo <= valor_atual <= limite_alto:
        return 'NORMAL'
    else:
        return 'DANGER'