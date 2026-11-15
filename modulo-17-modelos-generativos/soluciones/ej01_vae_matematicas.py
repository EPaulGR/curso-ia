"""Ej 01 — Piezas matemáticas del VAE: truco de reparametrización y KL gaussiana."""
import numpy as np


def reparametrizar(mu, logvar, eps):
    """z = μ + σ·ε con σ = exp(logvar/2)."""
    return mu + np.exp(0.5 * logvar) * eps


def kl_normal_estandar(mu, logvar):
    """KL(N(μ,σ²) ‖ N(0,1)) sumada sobre dimensiones: -½ Σ (1 + logvar - μ² - e^{logvar})."""
    return -0.5 * np.sum(1 + logvar - mu ** 2 - np.exp(logvar), axis=-1)


def elbo(log_verosimilitud, kl):
    """ELBO = E[log p(x|z)] - KL."""
    return log_verosimilitud - kl
