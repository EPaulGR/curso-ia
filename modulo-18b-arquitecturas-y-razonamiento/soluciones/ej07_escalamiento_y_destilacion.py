"""Ejercicio 07 — Leyes de escalamiento (Chinchilla) y destilación.

Ley de potencias: L(N) = A * N^(-alpha). En log: log L = log A - alpha log N,
un ajuste lineal. Chinchilla (Hoffmann et al., 2022): con cómputo C ≈ 6 N D,
lo óptimo es ~20 tokens por parámetro (D ≈ 20 N).
Destilación (Hinton et al., 2015): KL(softmax(t/T) || softmax(s/T)) * T^2.
"""
import numpy as np


def ajustar_ley_potencias(N, L):
    """Devuelve (A, alpha) ajustando log L = log A - alpha log N por mínimos cuadrados."""
    pend, inter = np.polyfit(np.log(N), np.log(L), 1)
    return float(np.exp(inter)), float(-pend)


def chinchilla_optimo(C, tokens_por_parametro=20.0):
    """Con C = 6 N D y D = r N: N = sqrt(C / (6 r)). Devuelve (N, D)."""
    N = np.sqrt(C / (6.0 * tokens_por_parametro))
    return float(N), float(tokens_por_parametro * N)


def _softmax(z):
    z = z - z.max(axis=-1, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=-1, keepdims=True)


def perdida_destilacion(logits_alumno, logits_maestro, T=2.0):
    """KL(p_maestro || p_alumno) con temperatura T, promediada por fila y multiplicada por T^2."""
    p = _softmax(logits_maestro / T)
    q = _softmax(logits_alumno / T)
    kl = np.sum(p * (np.log(p + 1e-12) - np.log(q + 1e-12)), axis=-1)
    return float(kl.mean() * T * T)
