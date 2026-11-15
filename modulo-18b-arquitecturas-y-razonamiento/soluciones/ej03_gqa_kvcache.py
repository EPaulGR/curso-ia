"""Ejercicio 03 — Grouped-Query Attention (GQA) y KV cache.

En GQA hay n_q cabezas de consulta pero solo n_kv cabezas de clave/valor
(n_q % n_kv == 0); cada grupo de n_q/n_kv consultas comparte K,V.
MQA es el caso n_kv = 1; MHA es n_kv = n_q.
El KV cache guarda K,V de los pasos previos para decodificar un token a la vez.
"""
import numpy as np


def softmax(z, axis=-1):
    """Softmax numéricamente estable."""
    z = z - z.max(axis=axis, keepdims=True)
    e = np.exp(z)
    return e / e.sum(axis=axis, keepdims=True)


def atencion_gqa(q, k, v, causal=True):
    """q: (n_q, T, dh); k, v: (n_kv, S, dh). Devuelve (n_q, T, dh).

    Con causal=True la consulta t (alineada al final de S) solo ve s <= t + (S - T).
    """
    n_q, T, dh = q.shape
    n_kv, S, _ = k.shape
    rep = n_q // n_kv
    k = np.repeat(k, rep, axis=0)
    v = np.repeat(v, rep, axis=0)
    s = q @ k.transpose(0, 2, 1) / np.sqrt(dh)
    if causal:
        desfase = S - T
        mask = np.arange(S)[None, :] > (np.arange(T)[:, None] + desfase)
        s = np.where(mask[None], -np.inf, s)
    return softmax(s) @ v


class KVCache:
    """Acumula claves y valores por paso de decodificación."""

    def __init__(self):
        self.k = None
        self.v = None

    def agregar(self, k_nuevo, v_nuevo):
        """k_nuevo, v_nuevo: (n_kv, t, dh). Concatena en el eje temporal y devuelve (k, v)."""
        if self.k is None:
            self.k, self.v = k_nuevo, v_nuevo
        else:
            self.k = np.concatenate([self.k, k_nuevo], axis=1)
            self.v = np.concatenate([self.v, v_nuevo], axis=1)
        return self.k, self.v


def bytes_kv_cache(capas, n_kv, dh, T, bytes_por_valor=2):
    """Memoria del KV cache: 2 (K y V) * capas * n_kv * dh * T * bytes."""
    return 2 * capas * n_kv * dh * T * bytes_por_valor
