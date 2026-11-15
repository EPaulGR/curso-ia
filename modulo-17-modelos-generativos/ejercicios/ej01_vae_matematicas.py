# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-17-modelos-generativos

"""Ej 01 — Piezas matemáticas del VAE: truco de reparametrización y KL gaussiana."""
import numpy as np

def reparametrizar(mu, logvar, eps):
    """z = μ + σ·ε con σ = exp(logvar/2)."""
    raise NotImplementedError  # TODO

def kl_normal_estandar(mu, logvar):
    """KL(N(μ,σ²) ‖ N(0,1)) sumada sobre dimensiones: -½ Σ (1 + logvar - μ² - e^{logvar})."""
    raise NotImplementedError  # TODO

def elbo(log_verosimilitud, kl):
    """ELBO = E[log p(x|z)] - KL."""
    raise NotImplementedError  # TODO
