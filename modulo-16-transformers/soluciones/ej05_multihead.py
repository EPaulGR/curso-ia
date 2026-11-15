"""Ej 05 — Atención multi-cabeza causal en PyTorch."""
import math
import torch
from torch import nn


class AtencionMultiCabeza(nn.Module):
    """Proyección qkv conjunta, h cabezas, máscara causal, proyección de salida."""

    def __init__(self, d, h, dropout=0.0):
        super().__init__()
        assert d % h == 0
        self.h, self.dk = h, d // h
        self.qkv = nn.Linear(d, 3 * d)
        self.proy = nn.Linear(d, d)
        self.drop = nn.Dropout(dropout)

    def forward(self, x):
        """x (N, T, d) → (N, T, d)."""
        N, T, d = x.shape
        q, k, v = self.qkv(x).split(d, dim=-1)
        q, k, v = (t.view(N, T, self.h, self.dk).transpose(1, 2) for t in (q, k, v))
        s = q @ k.transpose(-2, -1) / math.sqrt(self.dk)
        causal = torch.tril(torch.ones(T, T, dtype=torch.bool, device=x.device))
        s = s.masked_fill(~causal, float("-inf"))
        p = self.drop(torch.softmax(s, -1))
        y = (p @ v).transpose(1, 2).reshape(N, T, d)
        return self.proy(y)
