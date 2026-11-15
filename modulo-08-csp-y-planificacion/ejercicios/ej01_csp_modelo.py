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
        raise NotImplementedError  # TODO: implementa esta función

    def conflictos(self, asignacion, var, valor):
        """Número de vecinos asignados en conflicto con var=valor."""
        raise NotImplementedError  # TODO: implementa esta función


def coloreo_australia(colores=("R", "G", "B")):
    """CSP de coloreo del mapa de Australia (AIMA fig. 6.1): WA, NT, SA, Q, NSW, V, T.
    Regiones adyacentes deben tener colores distintos."""
    raise NotImplementedError  # TODO: implementa esta función


def n_reinas(n):
    """CSP de n reinas: variable = columna, valor = fila. No comparten fila ni diagonal."""
    raise NotImplementedError  # TODO: implementa esta función
