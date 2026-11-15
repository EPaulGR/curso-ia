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
    raise NotImplementedError  # TODO

def satisface(clausulas, asignacion):
    """True si la asignación satisface todas las cláusulas (variables faltantes = False)."""
    raise NotImplementedError  # TODO
