"""Ejercicio 09 — GRPO (Group Relative Policy Optimization) en juguete.

GRPO (DeepSeekMath, 2024; DeepSeek-R1, 2025) elimina el crítico de PPO:
para cada prompt se muestrean G respuestas, y la ventaja de cada una es
    A_i = (r_i - mean(r)) / (std(r) + eps)
con r_i una recompensa VERIFICABLE (¿la respuesta es correcta?).

Juguete: prompts = sumas a+b con a,b en 0..4; la "política" es tabular:
logits[prompt, respuesta] sobre respuestas 0..8. Gradiente de política:
    grad log pi(y|x) = onehot(y) - pi(.|x)
"""
import numpy as np


def ventajas_grupo(recompensas, eps=1e-8):
    """Normaliza recompensas dentro del grupo."""
    r = np.asarray(recompensas, dtype=float)
    return (r - r.mean()) / (r.std() + eps)


def recompensa_suma(a, b, y):
    """1.0 si y == a + b, 0.0 si no."""
    return 1.0 if y == a + b else 0.0


def politica(logits_fila):
    """Softmax de una fila de logits."""
    z = logits_fila - logits_fila.max()
    p = np.exp(z)
    return p / p.sum()


def entrenar_grpo(pasos=300, G=8, lr=0.5, semilla=0):
    """Entrena la política tabular con GRPO y devuelve logits (25, 9).

    En cada paso: elige un prompt al azar, muestrea G respuestas, calcula ventajas
    de grupo y actualiza logits[prompt] += lr * mean_i A_i * (onehot(y_i) - pi).
    """
    rng = np.random.default_rng(semilla)
    logits = np.zeros((25, 9))
    for _ in range(pasos):
        p_idx = rng.integers(25)
        a, b = divmod(p_idx, 5)
        pi = politica(logits[p_idx])
        ys = rng.choice(9, size=G, p=pi)
        A = ventajas_grupo([recompensa_suma(a, b, y) for y in ys])
        grad = np.zeros(9)
        for y, ai in zip(ys, A):
            oh = np.zeros(9)
            oh[y] = 1.0
            grad += ai * (oh - pi)
        logits[p_idx] += lr * grad / G
    return logits


def exactitud(logits):
    """Fracción de prompts donde argmax de la política es la suma correcta."""
    return float(np.mean([np.argmax(logits[i]) == sum(divmod(i, 5)) for i in range(25)]))
