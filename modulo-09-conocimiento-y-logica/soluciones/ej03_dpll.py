"""Ejercicio 03 — DPLL para SAT (AIMA 7.6.1).

Cláusulas en formato DIMACS: lista de listas de enteros (3 = x3, -3 = ¬x3).
DPLL = backtracking + propagación unitaria + literales puros.
    DPLL(cláusulas, modelo):
        simplificar con el modelo; si alguna cláusula vacía → falla; si no quedan → éxito
        si hay cláusula unitaria [l]: asignar l y recursar
        si hay literal puro l: asignar l y recursar
        elegir variable v: probar v=True, luego v=False
"""


def dpll(clausulas, modelo=None):
    """Devuelve dict var → bool que satisface todas las cláusulas, o None."""
    modelo = dict(modelo or {})

    def simplificar(cls, lit):
        out = []
        for c in cls:
            if lit in c:
                continue
            c2 = [x for x in c if x != -lit]
            out.append(c2)
        return out

    def rec(cls, modelo):
        if any(len(c) == 0 for c in cls):
            return None
        if not cls:
            return modelo
        for c in cls:
            if len(c) == 1:
                l = c[0]
                return rec(simplificar(cls, l), {**modelo, abs(l): l > 0})
        lits = {l for c in cls for l in c}
        for l in lits:
            if -l not in lits:
                return rec(simplificar(cls, l), {**modelo, abs(l): l > 0})
        v = abs(cls[0][0])
        for l in (v, -v):
            r = rec(simplificar(cls, l), {**modelo, v: l > 0})
            if r is not None:
                return r
        return None

    cls = [list(c) for c in clausulas]
    for v, val in modelo.items():
        cls = simplificar(cls, v if val else -v)
    r = rec(cls, modelo)
    if r is None:
        return None
    for c in clausulas:   # variables libres → False
        for l in c:
            r.setdefault(abs(l), False)
    return r
