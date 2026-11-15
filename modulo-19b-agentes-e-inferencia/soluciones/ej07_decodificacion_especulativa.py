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
    ctx = list(ctx)
    propuestos, qs = [], []
    for _ in range(gamma):
        qd = q(ctx + propuestos)
        propuestos.append(int(rng.choice(len(qd), p=qd)))
        qs.append(qd)
    nuevos = []
    for i, x in enumerate(propuestos):
        pd = p(ctx + nuevos)
        if rng.random() < min(1.0, pd[x] / qs[i][x]):
            nuevos.append(x)
        else:
            resid = np.maximum(pd - qs[i], 0)
            resid /= resid.sum()
            nuevos.append(int(rng.choice(len(resid), p=resid)))
            return nuevos, i
    pd = p(ctx + nuevos)
    nuevos.append(int(rng.choice(len(pd), p=pd)))
    return nuevos, gamma


def tasa_aceptacion_esperada(p_dist, q_dist):
    return float(np.minimum(p_dist, q_dist).sum())
