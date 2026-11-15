"""Ej 02 — Bolsa de palabras y TF-IDF."""
import numpy as np


def bolsa_palabras(docs_tokens, vocab):
    """Matriz (n_docs, |V|) de conteos."""
    M = np.zeros((len(docs_tokens), len(vocab)))
    for i, d in enumerate(docs_tokens):
        for t in d:
            if t in vocab:
                M[i, vocab[t]] += 1
    return M


def tfidf(conteos):
    """TF = conteo/len(doc); IDF = log((1+N)/(1+df)) + 1 (variante suave de scikit-learn); normaliza filas L2."""
    N = conteos.shape[0]
    tf = conteos / np.maximum(conteos.sum(1, keepdims=True), 1)
    df = (conteos > 0).sum(0)
    X = tf * (np.log((1 + N) / (1 + df)) + 1)
    return X / np.maximum(np.linalg.norm(X, axis=1, keepdims=True), 1e-12)


def coseno(a, b):
    """Similitud coseno entre dos vectores."""
    return float(a @ b / (np.linalg.norm(a) * np.linalg.norm(b) + 1e-12))
