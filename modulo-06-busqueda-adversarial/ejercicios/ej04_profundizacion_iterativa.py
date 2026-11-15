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
    raise NotImplementedError  # TODO: implementa esta función


def profundizacion_iterativa(juego, estado, profundidad_max, evaluar):
    """Ejecuta alfabeta_limitado con d=1..profundidad_max, poniendo la mejor jugada
    previa primero. Devuelve (mejor_accion, valor, historial) donde historial es la
    lista de mejores acciones por iteración."""
    raise NotImplementedError  # TODO: implementa esta función
