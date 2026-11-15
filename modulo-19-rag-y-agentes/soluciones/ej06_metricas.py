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
    return sum(r in relevantes for r in recuperados[:k]) / k


def recall_en_k(recuperados, relevantes, k):
    return sum(r in relevantes for r in recuperados[:k]) / len(relevantes)


def mrr(lista_recuperados, lista_relevantes):
    tot = 0.0
    for rec, rel in zip(lista_recuperados, lista_relevantes):
        tot += next((1 / (i + 1) for i, r in enumerate(rec) if r in rel), 0.0)
    return tot / len(lista_recuperados)


def ndcg_en_k(recuperados, relevancias, k):
    dcg = sum(relevancias.get(r, 0) / math.log2(i + 2) for i, r in enumerate(recuperados[:k]))
    ideal = sorted(relevancias.values(), reverse=True)[:k]
    idcg = sum(g / math.log2(i + 2) for i, g in enumerate(ideal))
    return dcg / idcg if idcg else 0.0


def _norm(s):
    return " ".join(re.sub(r"[^\w\s]", "", s.lower()).split())


def exact_match(pred, ref):
    return _norm(pred) == _norm(ref)


def f1_tokens(pred, ref):
    p, r = _norm(pred).split(), _norm(ref).split()
    comunes = sum((Counter(p) & Counter(r)).values())
    if comunes == 0:
        return 0.0
    prec, rec = comunes / len(p), comunes / len(r)
    return 2 * prec * rec / (prec + rec)
