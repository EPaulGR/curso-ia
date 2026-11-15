"""Ejercicio 04 — Modelos ocultos de Markov (AIMA cap. 14).

Parámetros (estados 0..S-1, observaciones 0..O-1), arrays numpy:
    pi[S]       distribución inicial  P(X0)   (antes de la primera observación)
    A[S,S]      transición            A[i,j] = P(X_{t+1}=j | X_t=i)
    B[S,O]      sensor/emisión        B[i,o] = P(E_t=o | X_t=i)

Filtrado (forward):     f_{1:t+1} = α · B[:, e_{t+1}] ⊙ (Aᵀ f_{1:t}),  f_0 = pi
Suavizado (forward–backward): b_{k+1:t} = A (B[:, e_{k+1}] ⊙ b_{k+2:t}),  b = 1 al final
Viterbi: secuencia de estados más probable (programación dinámica con max y punteros).
"""
import numpy as np


def filtrado(pi, A, B, obs):
    """Array (T, S): P(X_t | e_1:t) para t = 1..T."""
    raise NotImplementedError  # TODO: implementa esta función


def suavizado(pi, A, B, obs):
    """Array (T, S): P(X_k | e_1:T) para k = 1..T."""
    raise NotImplementedError  # TODO: implementa esta función


def viterbi(pi, A, B, obs):
    """Lista con la secuencia de estados más probable (longitud T)."""
    raise NotImplementedError  # TODO: implementa esta función
