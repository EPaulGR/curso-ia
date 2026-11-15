# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-16-transformers

"""Ej 06 — Bloque Transformer pre-norm (estilo GPT-2)."""
from torch import nn
import importlib.util, pathlib
_spec = importlib.util.spec_from_file_location('mh', pathlib.Path(__file__).with_name('ej05_multihead.py'))
_mh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mh)

class Bloque(nn.Module):
    """x = x + MHA(LN(x)); x = x + MLP(LN(x)), MLP = Linear(d,4d) → GELU → Linear(4d,d)."""

    def __init__(self, d, h, dropout=0.0):
        raise NotImplementedError  # TODO

    def forward(self, x):
        """Aplica el bloque con conexiones residuales."""
        raise NotImplementedError  # TODO
