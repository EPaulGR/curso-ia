"""Ejercicio 02 — DPLL.
CNF como lista de cláusulas; cada cláusula es lista de enteros (estilo DIMACS): 3 = x3, -3 = ¬x3."""


def _simplificar(clausulas, lit):
    res = []
    for c in clausulas:
        if lit in c:
            continue
        res.append([l for l in c if l != -lit])
    return res


def dpll(clausulas, asignacion=None):
    """Devuelve dict var->bool que satisface la CNF, o None si es insatisfacible."""
    asignacion = dict(asignacion or {})
    while True:
        if any(len(c) == 0 for c in clausulas):
            return None
        if not clausulas:
            return asignacion
        unit = next((c[0] for c in clausulas if len(c) == 1), None)
        if unit is None:
            lits = {l for c in clausulas for l in c}
            unit = next((l for l in lits if -l not in lits), None)
        if unit is None:
            break
        asignacion[abs(unit)] = unit > 0
        clausulas = _simplificar(clausulas, unit)
    x = clausulas[0][0]
    for lit in (x, -x):
        r = dpll(_simplificar(clausulas, lit), {**asignacion, abs(lit): lit > 0})
        if r is not None:
            return r
    return None


def satisface(clausulas, asignacion):
    """True si la asignación satisface todas las cláusulas (variables faltantes = False)."""
    return all(any(asignacion.get(abs(l), False) == (l > 0) for l in c) for c in clausulas)
