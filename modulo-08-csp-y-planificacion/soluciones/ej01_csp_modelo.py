"""Ejercicio 01 — Modelado de problemas de satisfacción de restricciones (AIMA 6.1).

Un CSP binario es (X, D, C): variables, dominios y restricciones entre pares.
Representación usada en todo el módulo:
    csp.variables : lista
    csp.dominios  : dict var → lista de valores (se modifica durante la inferencia)
    csp.vecinos   : dict var → lista de variables con las que comparte restricción
    csp.restriccion(A, a, B, b) → True si A=a y B=b son compatibles
"""


class CSP:
    def __init__(self, variables, dominios, vecinos, restriccion):
        """DADO."""
        self.variables = list(variables)
        self.dominios = {v: list(dominios[v]) for v in self.variables}
        self.vecinos = vecinos
        self.restriccion = restriccion

    def consistente(self, asignacion, var, valor):
        """True si var=valor no viola ninguna restricción con las variables ya asignadas."""
        return all(self.restriccion(var, valor, w, asignacion[w])
                   for w in self.vecinos[var] if w in asignacion)

    def conflictos(self, asignacion, var, valor):
        """Número de vecinos asignados en conflicto con var=valor."""
        return sum(1 for w in self.vecinos[var]
                   if w in asignacion and not self.restriccion(var, valor, w, asignacion[w]))


def coloreo_australia(colores=("R", "G", "B")):
    """CSP de coloreo del mapa de Australia (AIMA fig. 6.1): WA, NT, SA, Q, NSW, V, T.
    Regiones adyacentes deben tener colores distintos."""
    ady = {"WA": ["NT", "SA"], "NT": ["WA", "SA", "Q"], "SA": ["WA", "NT", "Q", "NSW", "V"],
           "Q": ["NT", "SA", "NSW"], "NSW": ["Q", "SA", "V"], "V": ["SA", "NSW"], "T": []}
    return CSP(list(ady), {v: list(colores) for v in ady}, ady, lambda A, a, B, b: a != b)


def n_reinas(n):
    """CSP de n reinas: variable = columna, valor = fila. No comparten fila ni diagonal."""
    vs = list(range(n))
    vec = {v: [w for w in vs if w != v] for v in vs}
    return CSP(vs, {v: list(range(n)) for v in vs}, vec,
               lambda A, a, B, b: a != b and abs(a - b) != abs(A - B))
