"""Ejercicio 01 — Teorema de Bayes."""


def posterior(prior, sensibilidad, especificidad):
    """P(enfermo | prueba positiva)."""
    fp = 1 - especificidad
    return sensibilidad * prior / (sensibilidad * prior + fp * (1 - prior))


def posterior_repetida(prior, sensibilidad, especificidad, positivos):
    """Posterior tras `positivos` pruebas positivas independientes consecutivas."""
    p = prior
    for _ in range(positivos):
        p = posterior(p, sensibilidad, especificidad)
    return p


def bayes_discreto(priors: dict, verosimilitudes: dict) -> dict:
    """Posterior normalizado: priors[h] y verosimilitudes[h]=P(E|h). Devuelve dict h->P(h|E)."""
    nums = {h: priors[h] * verosimilitudes[h] for h in priors}
    z = sum(nums.values())
    return {h: v / z for h, v in nums.items()}
