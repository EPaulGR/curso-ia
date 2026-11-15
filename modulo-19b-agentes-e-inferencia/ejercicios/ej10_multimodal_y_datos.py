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
    raise NotImplementedError  # TODO


def _log_softmax(x):
    x = x - x.max(axis=1, keepdims=True)
    return x - np.log(np.exp(x).sum(axis=1, keepdims=True))


def perdida_clip(img_emb, txt_emb, temperatura=0.07):
    raise NotImplementedError  # TODO


def _ngramas(t, n):
    t = t.lower()
    return {t[i:i + n] for i in range(max(1, len(t) - n + 1))}


def deduplicar(textos, umbral=0.8, n=3):
    raise NotImplementedError  # TODO
