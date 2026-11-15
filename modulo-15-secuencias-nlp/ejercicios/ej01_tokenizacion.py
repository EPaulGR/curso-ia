# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-15-secuencias-nlp

"""Ej 01 — Tokenización y vocabulario."""
import re
from collections import Counter

def tokenizar(texto):
    """Minúsculas y separa palabras (letras con acentos, ñ y dígitos) de signos de puntuación."""
    raise NotImplementedError  # TODO

def construir_vocab(textos, min_frec=1):
    """Devuelve dict token→id con '<pad>'=0, '<unk>'=1 y luego tokens por frecuencia descendente (empates alfabéticos)."""
    raise NotImplementedError  # TODO

def codificar(texto, vocab):
    """Lista de ids; tokens desconocidos → id de '<unk>'."""
    raise NotImplementedError  # TODO
