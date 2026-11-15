"""Ejercicio 05 — Mixture of Experts (MoE) con router top-k.

Cada token elige k expertos por logits del router; la salida es la suma de
los expertos elegidos ponderada por softmax de sus logits (renormalizado).
Pérdida de balanceo (Switch Transformer): L = E * sum_e f_e * P_e, donde
f_e = fracción de tokens asignados (top-1) al experto e y P_e = prob. media del router.
"""
import numpy as np


def router_topk(logits, k):
    """logits: (N, E). Devuelve (indices (N,k), pesos (N,k)) con pesos que suman 1 por fila."""
    raise NotImplementedError  # TODO


def moe_forward(x, W_router, expertos, k=2):
    """x: (N, d); expertos: lista de funciones f(x)->(n, d_out). Devuelve (N, d_out)."""
    raise NotImplementedError  # TODO


def perdida_balanceo(logits):
    """Pérdida auxiliar de balanceo de carga (mínimo 1.0 cuando es uniforme)."""
    raise NotImplementedError  # TODO
