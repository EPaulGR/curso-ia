"""Ejercicio 6 — Métricas de evaluación de recuperación y generación.

- `precision_en_k(recuperados, relevantes, k)`.
- `recall_en_k(recuperados, relevantes, k)`.
- `mrr(lista_recuperados, lista_relevantes)`: Mean Reciprocal Rank sobre varias consultas.
- `ndcg_en_k(recuperados, relevancias: dict id->ganancia, k)`: DCG = sum g/log2(i+2).
- `exact_match(pred, ref)`: normaliza (minúsculas, sin puntuación ni espacios extra).
- `f1_tokens(pred, ref)`: F1 sobre tokens (estilo SQuAD).
"""
import math
import re
from collections import Counter


def precision_en_k(recuperados, relevantes, k):
    raise NotImplementedError  # TODO: implementa esta función


def recall_en_k(recuperados, relevantes, k):
    raise NotImplementedError  # TODO: implementa esta función


def mrr(lista_recuperados, lista_relevantes):
    raise NotImplementedError  # TODO: implementa esta función


def ndcg_en_k(recuperados, relevancias, k):
    raise NotImplementedError  # TODO: implementa esta función


def _norm(s):
    return " ".join(re.sub(r"[^\w\s]", "", s.lower()).split())


def exact_match(pred, ref):
    raise NotImplementedError  # TODO: implementa esta función


def f1_tokens(pred, ref):
    raise NotImplementedError  # TODO: implementa esta función
