"""Ejercicio 05 — Mixture of Experts (MoE) con router top-k.

Cada token elige k expertos por logits del router; la salida es la suma de
los expertos elegidos ponderada por softmax de sus logits (renormalizado).
Pérdida de balanceo (Switch Transformer): L = E * sum_e f_e * P_e, donde
f_e = fracción de tokens asignados (top-1) al experto e y P_e = prob. media del router.
"""
import numpy as np


def router_topk(logits, k):
    """logits: (N, E). Devuelve (indices (N,k), pesos (N,k)) con pesos que suman 1 por fila."""
    idx = np.argsort(-logits, axis=1)[:, :k]
    sel = np.take_along_axis(logits, idx, axis=1)
    sel = sel - sel.max(axis=1, keepdims=True)
    w = np.exp(sel)
    return idx, w / w.sum(axis=1, keepdims=True)


def moe_forward(x, W_router, expertos, k=2):
    """x: (N, d); expertos: lista de funciones f(x)->(n, d_out). Devuelve (N, d_out)."""
    idx, w = router_topk(x @ W_router, k)
    salida = None
    for e, f in enumerate(expertos):
        filas, pos = np.nonzero(idx == e)
        if len(filas) == 0:
            continue
        y = f(x[filas]) * w[filas, pos][:, None]
        if salida is None:
            salida = np.zeros((x.shape[0], y.shape[1]))
        np.add.at(salida, filas, y)
    return salida


def perdida_balanceo(logits):
    """Pérdida auxiliar de balanceo de carga (mínimo 1.0 cuando es uniforme)."""
    N, E = logits.shape
    z = logits - logits.max(axis=1, keepdims=True)
    p = np.exp(z)
    p /= p.sum(axis=1, keepdims=True)
    f = np.bincount(np.argmax(logits, axis=1), minlength=E) / N
    return E * float(np.sum(f * p.mean(axis=0)))
