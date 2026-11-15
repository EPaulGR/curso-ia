"""Ejercicio 03 — Poda alfa-beta (BUAP 3.3.2, AIMA 5.3).

α = mejor valor garantizado para MAX en el camino actual.
β = mejor valor garantizado para MIN en el camino actual.
Si en un nodo MAX v ≥ β → podar. En un nodo MIN si v ≤ α → podar.

Debe devolver exactamente el mismo valor que minimax pero visitando menos nodos.
"""


def alfabeta(juego, estado):
    """Devuelve (mejor_accion, valor, nodos_visitados)."""
    raise NotImplementedError  # TODO: implementa esta función
