"""Ejercicio 02 — Búsqueda con retroceso (backtracking) y heurísticas (AIMA 6.3).

- MRV (mínimos valores restantes): elegir la variable con dominio actual más pequeño
  (desempate: mayor grado = más vecinos sin asignar).
- LCV (valor menos restrictivo): probar primero el valor que elimina menos opciones a los vecinos.
- Forward checking: al asignar X=x, borrar de los dominios de los vecinos no asignados
  los valores incompatibles; si alguno queda vacío → retroceder.
"""


def backtracking(csp, mrv=True, lcv=True, forward_checking=True):
    """Devuelve (asignacion dict o None, nodos) donde nodos = número de asignaciones probadas.
    No debe dejar modificados los dominios del csp al terminar."""
    raise NotImplementedError  # TODO: implementa esta función
