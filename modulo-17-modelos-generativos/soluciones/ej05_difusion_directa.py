"""Ej 05 — Proceso de difusión directo (DDPM, Ho et al., 2020)."""
import numpy as np


def calendario_lineal(T, b0=1e-4, b1=0.02):
    """Devuelve (betas, alphas, alpha_barras) de longitud T."""
    betas = np.linspace(b0, b1, T)
    alphas = 1 - betas
    return betas, alphas, np.cumprod(alphas)


def q_muestra(x0, t, alpha_barras, ruido):
    """x_t = √ᾱ_t·x0 + √(1-ᾱ_t)·ε (salto directo a cualquier t)."""
    a = alpha_barras[t]
    return np.sqrt(a) * x0 + np.sqrt(1 - a) * ruido


def snr(alpha_barras):
    """Relación señal/ruido ᾱ/(1-ᾱ)."""
    return alpha_barras / (1 - alpha_barras)
