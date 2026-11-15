# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-15-secuencias-nlp

"""Ej 04 — Word2Vec skip-gram con negative sampling (NumPy)."""
import numpy as np

def pares_skipgram(ids, ventana):
    """Lista de (centro, contexto) para cada posición y cada vecino a distancia ≤ ventana."""
    raise NotImplementedError  # TODO

def entrenar_sgns(pares, V, dim=16, negativos=5, epocas=5, lr=0.05, semilla=0):
    """Pérdida: -log σ(u_o·v_c) - Σ log σ(-u_k·v_c). Devuelve la matriz de embeddings de centro (V, dim)."""
    raise NotImplementedError  # TODO

def mas_similares(E, i, k=3):
    """Índices de los k vectores más similares (coseno) a E[i], excluyendo i."""
    raise NotImplementedError  # TODO
