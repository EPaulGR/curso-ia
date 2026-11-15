"""Ejercicio 01 — Regla de Bayes y actualización de creencias (AIMA cap. 12).

    P(H | e) = P(e | H) · P(H) / P(e),   P(e) = Σ_h P(e | h) P(h)
"""


def normalizar(d):
    """Devuelve un dict con los mismos valores escalados para sumar 1."""
    s = sum(d.values())
    return {k: v / s for k, v in d.items()}


def posterior(prior, verosimilitud):
    """prior: dict h → P(h); verosimilitud: dict h → P(e | h). Devuelve P(h | e)."""
    return normalizar({h: prior[h] * verosimilitud[h] for h in prior})


def actualizacion_secuencial(prior, verosimilitudes):
    """Aplica posterior() con cada evidencia (supuestas condicionalmente independientes
    dada h) en orden. Devuelve la lista de distribuciones tras cada evidencia."""
    hist, p = [], prior
    for v in verosimilitudes:
        p = posterior(p, v)
        hist.append(p)
    return hist


def prueba_medica(prevalencia, sensibilidad, especificidad):
    """P(enfermo | prueba positiva)."""
    return posterior({"enf": prevalencia, "sano": 1 - prevalencia},
                     {"enf": sensibilidad, "sano": 1 - especificidad})["enf"]
