"""Ej 06 — Bloque Transformer pre-norm (estilo GPT-2)."""
from torch import nn
import importlib.util, pathlib

_spec = importlib.util.spec_from_file_location("mh", pathlib.Path(__file__).with_name("ej05_multihead.py"))
_mh = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_mh)


class Bloque(nn.Module):
    """x = x + MHA(LN(x)); x = x + MLP(LN(x)), MLP = Linear(d,4d) → GELU → Linear(4d,d)."""

    def __init__(self, d, h, dropout=0.0):
        super().__init__()
        self.ln1 = nn.LayerNorm(d)
        self.att = _mh.AtencionMultiCabeza(d, h, dropout)
        self.ln2 = nn.LayerNorm(d)
        self.mlp = nn.Sequential(nn.Linear(d, 4 * d), nn.GELU(), nn.Linear(4 * d, d), nn.Dropout(dropout))

    def forward(self, x):
        """Aplica el bloque con conexiones residuales."""
        x = x + self.att(self.ln1(x))
        return x + self.mlp(self.ln2(x))
