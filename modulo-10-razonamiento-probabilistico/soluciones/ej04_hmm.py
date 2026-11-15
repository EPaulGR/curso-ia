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
    f = np.asarray(pi, float)
    salida = []
    for o in obs:
        f = B[:, o] * (A.T @ f)
        f = f / f.sum()
        salida.append(f)
    return np.array(salida)


def suavizado(pi, A, B, obs):
    """Array (T, S): P(X_k | e_1:T) para k = 1..T."""
    F = filtrado(pi, A, B, obs)
    T, S = F.shape
    b = np.ones(S)
    out = np.zeros_like(F)
    for k in range(T - 1, -1, -1):
        s = F[k] * b
        out[k] = s / s.sum()
        b = A @ (B[:, obs[k]] * b)
    return out


def viterbi(pi, A, B, obs):
    """Lista con la secuencia de estados más probable (longitud T)."""
    T, S = len(obs), A.shape[0]
    m = B[:, obs[0]] * (A.T @ np.asarray(pi, float))
    ptr = np.zeros((T, S), int)
    for t in range(1, T):
        cand = m[:, None] * A          # cand[i, j] = m_i · P(j | i)
        ptr[t] = cand.argmax(axis=0)
        m = cand.max(axis=0) * B[:, obs[t]]
        m = m / m.sum()
    camino = [int(m.argmax())]
    for t in range(T - 1, 0, -1):
        camino.append(int(ptr[t, camino[-1]]))
    return camino[::-1]
