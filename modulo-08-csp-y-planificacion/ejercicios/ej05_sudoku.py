"""Ejercicio 05 — Sudoku como CSP: AC-3 + backtracking con MRV (AIMA 6.2.6).

Entrada: cadena de 81 caracteres, '0' o '.' = vacío, por filas.
81 variables, dominio {1..9}, restricciones AllDiff en filas, columnas y cajas 3×3
(expresadas como 27 restricciones binarias ≠ por celda).
"""


def _vecinos():
    """DADO: dict celda → conjunto de celdas que comparten fila, columna o caja."""
    vec = {}
    for i in range(81):
        f, c = divmod(i, 9)
        s = {f * 9 + k for k in range(9)} | {k * 9 + c for k in range(9)}
        bf, bc = 3 * (f // 3), 3 * (c // 3)
        s |= {(bf + a) * 9 + bc + b for a in range(3) for b in range(3)}
        s.discard(i)
        vec[i] = s
    return vec


VECINOS = _vecinos()


def resolver_sudoku(tablero):
    """Devuelve la cadena de 81 dígitos resuelta, o None si no tiene solución."""
    raise NotImplementedError  # TODO: implementa esta función
