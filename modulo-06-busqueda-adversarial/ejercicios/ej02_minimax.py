"""Ejercicio 02 — MINIMAX (BUAP 3.3.1, AIMA 5.2).

Implementa minimax genérico sobre cualquier objeto `juego` con la interfaz
jugador / acciones / resultado / terminal / utilidad.

    función MINIMAX(s):
        jugador ← JUGADOR(s)
        devolver argmax_{a ∈ ACCIONES(s)} VALOR-MIN(RESULTADO(s, a))

La utilidad se mide desde el punto de vista del jugador que mueve en la raíz.
Debes contar los nodos visitados (cada llamada a la función de valor cuenta 1).
"""


def minimax(juego, estado):
    """Devuelve (mejor_accion, valor, nodos_visitados).
    En empates de valor elige la primera acción en el orden de juego.acciones()."""
    raise NotImplementedError  # TODO: implementa esta función
