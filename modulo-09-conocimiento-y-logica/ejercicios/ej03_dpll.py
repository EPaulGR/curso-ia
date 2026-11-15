"""Ejercicio 03 — DPLL para SAT (AIMA 7.6.1).

Cláusulas en formato DIMACS: lista de listas de enteros (3 = x3, -3 = ¬x3).
DPLL = backtracking + propagación unitaria + literales puros.
    DPLL(cláusulas, modelo):
        simplificar con el modelo; si alguna cláusula vacía → falla; si no quedan → éxito
        si hay cláusula unitaria [l]: asignar l y recursar
        si hay literal puro l: asignar l y recursar
        elegir variable v: probar v=True, luego v=False
"""


def dpll(clausulas, modelo=None):
    """Devuelve dict var → bool que satisface todas las cláusulas, o None."""
    raise NotImplementedError  # TODO: implementa esta función
