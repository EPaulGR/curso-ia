"""Ejercicio 10 — Multimodalidad (parches → tokens, CLIP) y curación de datos.

1. parches_a_tokens(img, p, W): img (H, W_img, C) con H y W_img múltiplos de p.
   Divide en parches p×p (orden fila por fila), aplana cada uno (p*p*C) y
   proyecta con W (p*p*C, d). Devuelve (N, d). Así un ViT/VLM convierte imágenes
   en "tokens" que el Transformer procesa junto al texto.
2. perdida_clip(img_emb, txt_emb, temperatura): normaliza L2 ambos (N, d),
   logits = img @ txt.T / temperatura, y devuelve la media de la entropía
   cruzada imagen→texto y texto→imagen con etiquetas en la diagonal.
3. deduplicar(textos, umbral=0.8, n=3): elimina casi-duplicados usando similitud
   de Jaccard sobre n-gramas de caracteres. Conserva el primero de cada grupo.
   Devuelve los índices conservados.
"""
import numpy as np


def parches_a_tokens(img, p, W):
    H, Wi, C = img.shape
    parches = (img.reshape(H // p, p, Wi // p, p, C)
                  .transpose(0, 2, 1, 3, 4)
                  .reshape(-1, p * p * C))
    return parches @ W


def _log_softmax(x):
    x = x - x.max(axis=1, keepdims=True)
    return x - np.log(np.exp(x).sum(axis=1, keepdims=True))


def perdida_clip(img_emb, txt_emb, temperatura=0.07):
    a = img_emb / np.linalg.norm(img_emb, axis=1, keepdims=True)
    b = txt_emb / np.linalg.norm(txt_emb, axis=1, keepdims=True)
    logits = a @ b.T / temperatura
    idx = np.arange(len(a))
    l_i = -_log_softmax(logits)[idx, idx].mean()
    l_t = -_log_softmax(logits.T)[idx, idx].mean()
    return float((l_i + l_t) / 2)


def _ngramas(t, n):
    t = t.lower()
    return {t[i:i + n] for i in range(max(1, len(t) - n + 1))}


def deduplicar(textos, umbral=0.8, n=3):
    conservados, conjuntos = [], []
    for i, t in enumerate(textos):
        g = _ngramas(t, n)
        if all(len(g & h) / len(g | h) < umbral for h in conjuntos):
            conservados.append(i)
            conjuntos.append(g)
    return conservados
