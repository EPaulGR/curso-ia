"""Ejercicio 03 — Poda alfa-beta (BUAP 3.3.2, AIMA 5.3).

α = mejor valor garantizado para MAX en el camino actual.
β = mejor valor garantizado para MIN en el camino actual.
Si en un nodo MAX v ≥ β → podar. En un nodo MIN si v ≤ α → podar.

Debe devolver exactamente el mismo valor que minimax pero visitando menos nodos.
"""


def alfabeta(juego, estado):
    """Devuelve (mejor_accion, valor, nodos_visitados)."""
    yo = juego.jugador(estado)
    nodos = 0
    INF = float("inf")

    def valor(s, alfa, beta):
        nonlocal nodos
        nodos += 1
        if juego.terminal(s):
            return juego.utilidad(s, yo)
        if juego.jugador(s) == yo:
            v = -INF
            for a in juego.acciones(s):
                v = max(v, valor(juego.resultado(s, a), alfa, beta))
                if v >= beta:
                    return v
                alfa = max(alfa, v)
            return v
        v = INF
        for a in juego.acciones(s):
            v = min(v, valor(juego.resultado(s, a), alfa, beta))
            if v <= alfa:
                return v
            beta = min(beta, v)
        return v

    mejor, alfa = None, -INF
    for a in juego.acciones(estado):
        v = valor(juego.resultado(estado, a), alfa, INF)
        if v > alfa:
            mejor, alfa = a, v
    return mejor, alfa, nodos
