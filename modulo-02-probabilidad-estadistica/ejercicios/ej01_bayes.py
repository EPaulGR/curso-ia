"""Ejercicio 01 — Teorema de Bayes."""

def posterior(prior, sensibilidad, especificidad):
    """P(enfermo | prueba positiva)."""
    raise NotImplementedError  # TODO

def posterior_repetida(prior, sensibilidad, especificidad, positivos):
    """Posterior tras `positivos` pruebas positivas independientes consecutivas."""
    raise NotImplementedError  # TODO

def bayes_discreto(priors: dict, verosimilitudes: dict) -> dict:
    """Posterior normalizado: priors[h] y verosimilitudes[h]=P(E|h). Devuelve dict h->P(h|E)."""
    raise NotImplementedError  # TODO
