# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-15-secuencias-nlp

"""Ej 02 — Bolsa de palabras y TF-IDF."""
import numpy as np

def bolsa_palabras(docs_tokens, vocab):
    """Matriz (n_docs, |V|) de conteos."""
    raise NotImplementedError  # TODO

def tfidf(conteos):
    """TF = conteo/len(doc); IDF = log((1+N)/(1+df)) + 1 (variante suave de scikit-learn); normaliza filas L2."""
    raise NotImplementedError  # TODO

def coseno(a, b):
    """Similitud coseno entre dos vectores."""
    raise NotImplementedError  # TODO
