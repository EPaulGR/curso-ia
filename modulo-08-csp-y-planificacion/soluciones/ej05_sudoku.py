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
    dom = {i: ({int(ch)} if ch not in "0." else set(range(1, 10))) for i, ch in enumerate(tablero)}

    def propagar(dom):
        cambio = True
        while cambio:
            cambio = False
            for i in range(81):
                if len(dom[i]) == 1:
                    v = next(iter(dom[i]))
                    for j in VECINOS[i]:
                        if v in dom[j]:
                            dom[j] = dom[j] - {v}
                            if not dom[j]:
                                return False
                            cambio = True
        return True

    def bt(dom):
        if not propagar(dom):
            return None
        if all(len(d) == 1 for d in dom.values()):
            return dom
        i = min((k for k in dom if len(dom[k]) > 1), key=lambda k: len(dom[k]))
        for v in sorted(dom[i]):
            d2 = {k: set(s) for k, s in dom.items()}
            d2[i] = {v}
            r = bt(d2)
            if r:
                return r
        return None

    r = bt(dom)
    return None if r is None else "".join(str(next(iter(r[i]))) for i in range(81))
