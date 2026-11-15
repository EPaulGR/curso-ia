"""Ejercicio 01 — Regla de Bayes y actualización de creencias (AIMA cap. 12).

    P(H | e) = P(e | H) · P(H) / P(e),   P(e) = Σ_h P(e | h) P(h)
"""


def normalizar(d):
    """Devuelve un dict con los mismos valores escalados para sumar 1."""
    raise NotImplementedError  # TODO: implementa esta función


def posterior(prior, verosimilitud):
    """prior: dict h → P(h); verosimilitud: dict h → P(e | h). Devuelve P(h | e)."""
    raise NotImplementedError  # TODO: implementa esta función


def actualizacion_secuencial(prior, verosimilitudes):
    """Aplica posterior() con cada evidencia (supuestas condicionalmente independientes
    dada h) en orden. Devuelve la lista de distribuciones tras cada evidencia."""
    raise NotImplementedError  # TODO: implementa esta función


def prueba_medica(prevalencia, sensibilidad, especificidad):
    """P(enfermo | prueba positiva)."""
    raise NotImplementedError  # TODO: implementa esta función
