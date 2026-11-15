"""Ejercicio 04 — Heurísticas para el 8-puzzle (meta por defecto (1,2,3,4,5,6,7,8,0))."""

META_8 = (1, 2, 3, 4, 5, 6, 7, 8, 0)


def fuera_de_lugar(s, meta=META_8):
    """h1: fichas (sin contar el 0) que no están en su posición meta."""
    return sum(1 for a, b in zip(s, meta) if a != 0 and a != b)


def manhattan(s, meta=META_8, n=3):
    """h2: suma de distancias Manhattan de cada ficha a su posición meta."""
    pos = {v: divmod(i, n) for i, v in enumerate(meta)}; t = 0
    for i, v in enumerate(s):
        if v:
            f, c = divmod(i, n); fm, cm = pos[v]; t += abs(f - fm) + abs(c - cm)
    return t


def conflicto_lineal(s, meta=META_8, n=3):
    """Manhattan + 2 por cada par de fichas en su fila (o columna) meta que están invertidas entre sí."""
    pos = {v: divmod(i, n) for i, v in enumerate(meta)}; extra = 0
    for k in range(n):
        fila = [(pos[v][1], v) for c in range(n) for v in [s[k * n + c]] if v and pos[v][0] == k]
        col = [(pos[v][0], v) for f in range(n) for v in [s[f * n + k]] if v and pos[v][1] == k]
        for linea in (fila, col):
            extra += 2 * sum(linea[i][0] > linea[j][0] for i in range(len(linea)) for j in range(i + 1, len(linea)))
    return manhattan(s, meta, n) + extra
