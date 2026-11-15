# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-16-transformers

"""Ej 07 — Mini-GPT a nivel de caracteres (entrénalo en MPS con un libro completo)."""
import torch
from torch import nn
import importlib.util, pathlib
_spec = importlib.util.spec_from_file_location('bl', pathlib.Path(__file__).with_name('ej06_bloque.py'))
_bl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_bl)
device = 'mps' if torch.backends.mps.is_available() else 'cpu'

class TokenizadorCaracteres:
    """Mapea cada carácter distinto del texto a un entero."""

    def __init__(self, texto):
        raise NotImplementedError  # TODO

    def codificar(self, s):
        """str → lista de ids."""
        raise NotImplementedError  # TODO

    def decodificar(self, ids):
        """lista de ids → str."""
        raise NotImplementedError  # TODO

class MiniGPT(nn.Module):
    """Embeddings de token + posición aprendida → n bloques → LayerNorm → cabeza lineal (pesos atados al embedding)."""

    def __init__(self, V, d=64, h=4, n=2, T=64, dropout=0.0):
        raise NotImplementedError  # TODO

    def forward(self, idx, objetivos=None):
        """idx (N,T') → (logits (N,T',V), pérdida o None)."""
        raise NotImplementedError  # TODO

    @torch.no_grad()
    def generar(self, idx, n_nuevos, temperatura=1.0):
        """Muestreo autoregresivo de n_nuevos tokens."""
        raise NotImplementedError  # TODO

def lotes(datos, T, N, gen):
    """Muestra N ventanas aleatorias de longitud T; devuelve (x, y) con y desplazado una posición."""
    raise NotImplementedError  # TODO

def entrenar(texto, pasos=300, T=32, N=32, lr=0.003, dispositivo=device, **kw):
    """Entrena con AdamW. Devuelve (modelo, tokenizador, historial_de_perdidas)."""
    raise NotImplementedError  # TODO
