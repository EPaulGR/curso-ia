"""Ejercicio 04 — Alfa-beta con corte de profundidad, función de evaluación,
ordenamiento de jugadas y profundización iterativa (BUAP 3.2, 3.5, 3.6; AIMA 5.4).

En juegos grandes no se llega a hojas: se corta a profundidad d y se usa
EVAL(s, jugador) ≈ utilidad esperada. El orden de exploración importa: con orden
perfecto alfa-beta visita O(b^(d/2)) nodos en vez de O(b^d).

Profundización iterativa: buscar con d = 1, 2, ..., D y, en cada iteración,
explorar primero la mejor jugada de la iteración anterior.
"""


def alfabeta_limitado(juego, estado, profundidad, evaluar, orden=None):
    """Alfa-beta con corte. `evaluar(s, jugador)` se usa en el corte; en estados
    terminales se usa juego.utilidad multiplicado por 1000.
    `orden`: lista opcional de acciones de la raíz a explorar primero.
    Devuelve (mejor_accion, valor, nodos)."""
    yo = juego.jugador(estado)
    nodos = 0
    INF = float("inf")

    def valor(s, d, alfa, beta):
        nonlocal nodos
        nodos += 1
        if juego.terminal(s):
            return 1000 * juego.utilidad(s, yo)
        if d == 0:
            return evaluar(s, yo)
        maxi = juego.jugador(s) == yo
        v = -INF if maxi else INF
        for a in juego.acciones(s):
            w = valor(juego.resultado(s, a), d - 1, alfa, beta)
            if maxi:
                v = max(v, w)
                if v >= beta:
                    return v
                alfa = max(alfa, v)
            else:
                v = min(v, w)
                if v <= alfa:
                    return v
                beta = min(beta, v)
        return v

    acciones = juego.acciones(estado)
    if orden:
        acciones = [a for a in orden if a in acciones] + [a for a in acciones if a not in orden]
    mejor, alfa = acciones[0], -INF
    for a in acciones:
        v = valor(juego.resultado(estado, a), profundidad - 1, alfa, INF)
        if v > alfa:
            mejor, alfa = a, v
    return mejor, alfa, nodos


def profundizacion_iterativa(juego, estado, profundidad_max, evaluar):
    """Ejecuta alfabeta_limitado con d=1..profundidad_max, poniendo la mejor jugada
    previa primero. Devuelve (mejor_accion, valor, historial) donde historial es la
    lista de mejores acciones por iteración."""
    mejor, v, historial = None, None, []
    for d in range(1, profundidad_max + 1):
        mejor, v, _ = alfabeta_limitado(juego, estado, d, evaluar, orden=[mejor] if mejor is not None else None)
        historial.append(mejor)
    return mejor, v, historial
