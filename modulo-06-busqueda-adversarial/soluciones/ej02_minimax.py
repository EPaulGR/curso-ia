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
    yo = juego.jugador(estado)
    nodos = 0

    def valor(s):
        nonlocal nodos
        nodos += 1
        if juego.terminal(s):
            return juego.utilidad(s, yo)
        vals = [valor(juego.resultado(s, a)) for a in juego.acciones(s)]
        return max(vals) if juego.jugador(s) == yo else min(vals)

    mejor, mejor_v = None, float("-inf")
    for a in juego.acciones(estado):
        v = valor(juego.resultado(estado, a))
        if v > mejor_v:
            mejor, mejor_v = a, v
    return mejor, mejor_v, nodos
