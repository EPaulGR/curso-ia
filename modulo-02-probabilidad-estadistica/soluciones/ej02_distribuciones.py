"""Ejercicio 02 — Distribuciones desde cero (solo math)."""
import math


def binomial_pmf(k, n, p):
    """P(X=k) para Binomial(n,p)."""
    return math.comb(n, k) * p ** k * (1 - p) ** (n - k)


def poisson_pmf(k, lam):
    """P(X=k) para Poisson(lam)."""
    return math.exp(-lam) * lam ** k / math.factorial(k)


def normal_pdf(x, mu=0.0, sigma=1.0):
    """Densidad normal."""
    return math.exp(-((x - mu) ** 2) / (2 * sigma ** 2)) / (math.sqrt(2 * math.pi) * sigma)


def normal_cdf(x, mu=0.0, sigma=1.0):
    """CDF normal usando math.erf."""
    return 0.5 * (1 + math.erf((x - mu) / (sigma * math.sqrt(2))))


def media_varianza(valores, probs):
    """(E[X], Var[X]) de una variable discreta."""
    m = sum(v * p for v, p in zip(valores, probs))
    return m, sum((v - m) ** 2 * p for v, p in zip(valores, probs))
