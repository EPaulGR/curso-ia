"""Ej 01 — Tokenización y vocabulario."""
import re
from collections import Counter


def tokenizar(texto):
    """Minúsculas y separa palabras (letras con acentos, ñ y dígitos) de signos de puntuación."""
    return re.findall(r"[a-záéíóúüñ0-9]+|[^\sa-záéíóúüñ0-9]", texto.lower())


def construir_vocab(textos, min_frec=1):
    """Devuelve dict token→id con '<pad>'=0, '<unk>'=1 y luego tokens por frecuencia descendente (empates alfabéticos)."""
    c = Counter(t for tx in textos for t in tokenizar(tx))
    vocab = {"<pad>": 0, "<unk>": 1}
    for t, f in sorted(c.items(), key=lambda kv: (-kv[1], kv[0])):
        if f >= min_frec:
            vocab[t] = len(vocab)
    return vocab


def codificar(texto, vocab):
    """Lista de ids; tokens desconocidos → id de '<unk>'."""
    return [vocab.get(t, 1) for t in tokenizar(texto)]
