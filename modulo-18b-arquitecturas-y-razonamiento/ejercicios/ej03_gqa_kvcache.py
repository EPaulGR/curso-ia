"""Ejercicio 03 — Grouped-Query Attention (GQA) y KV cache.

En GQA hay n_q cabezas de consulta pero solo n_kv cabezas de clave/valor
(n_q % n_kv == 0); cada grupo de n_q/n_kv consultas comparte K,V.
MQA es el caso n_kv = 1; MHA es n_kv = n_q.
El KV cache guarda K,V de los pasos previos para decodificar un token a la vez.
"""
import numpy as np


def softmax(z, axis=-1):
    """Softmax numéricamente estable."""
    raise NotImplementedError  # TODO


def atencion_gqa(q, k, v, causal=True):
    """q: (n_q, T, dh); k, v: (n_kv, S, dh). Devuelve (n_q, T, dh).

    Con causal=True la consulta t (alineada al final de S) solo ve s <= t + (S - T).
    """
    raise NotImplementedError  # TODO


class KVCache:
    """Acumula claves y valores por paso de decodificación."""

    def __init__(self):
        self.k = None
        self.v = None

    def agregar(self, k_nuevo, v_nuevo):
        """k_nuevo, v_nuevo: (n_kv, t, dh). Concatena en el eje temporal y devuelve (k, v)."""
        raise NotImplementedError  # TODO


def bytes_kv_cache(capas, n_kv, dh, T, bytes_por_valor=2):
    """Memoria del KV cache: 2 (K y V) * capas * n_kv * dh * T * bytes."""
    raise NotImplementedError  # TODO
