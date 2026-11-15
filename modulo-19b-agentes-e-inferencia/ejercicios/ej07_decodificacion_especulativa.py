"""Ejercicio 07 — Decodificación especulativa (Leviathan et al., 2023).

Un modelo borrador barato q propone `gamma` tokens; el modelo objetivo p los
verifica. Cada token propuesto x se acepta con prob. min(1, p(x)/q(x)). Al primer
rechazo se muestrea de la distribución residual norm(max(0, p - q)) y se para.
Si se aceptan todos, se muestrea un token extra de p. Resultado: la salida tiene
EXACTAMENTE la distribución de p, pero con menos pasadas del modelo grande.

- p(ctx), q(ctx): funciones que devuelven np.array de probabilidades sobre el vocabulario.
- paso_especulativo(ctx, p, q, gamma, rng) -> (tokens_nuevos, n_aceptados)
- tasa_aceptacion_esperada(p_dist, q_dist) = sum(min(p, q)).
"""
import numpy as np


def paso_especulativo(ctx, p, q, gamma, rng):
    raise NotImplementedError  # TODO


def tasa_aceptacion_esperada(p_dist, q_dist):
    raise NotImplementedError  # TODO
