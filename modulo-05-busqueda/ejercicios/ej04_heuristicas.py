"""Ejercicio 04 — Heurísticas para el 8-puzzle (meta por defecto (1,2,3,4,5,6,7,8,0))."""
META_8 = (1, 2, 3, 4, 5, 6, 7, 8, 0)

def fuera_de_lugar(s, meta=META_8):
    """h1: fichas (sin contar el 0) que no están en su posición meta."""
    raise NotImplementedError  # TODO

def manhattan(s, meta=META_8, n=3):
    """h2: suma de distancias Manhattan de cada ficha a su posición meta."""
    raise NotImplementedError  # TODO

def conflicto_lineal(s, meta=META_8, n=3):
    """Manhattan + 2 por cada par de fichas en su fila (o columna) meta que están invertidas entre sí."""
    raise NotImplementedError  # TODO
