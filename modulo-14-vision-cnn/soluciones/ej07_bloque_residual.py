"""Ej 07 — Bloque residual de ResNet (He et al., 2016)."""
import torch
from torch import nn


class BloqueResidual(nn.Module):
    """y = ReLU(BN(conv(ReLU(BN(conv(x))))) + atajo(x)); atajo = conv1x1+BN si cambia canales o stride."""

    def __init__(self, c_in, c_out, stride=1):
        super().__init__()
        self.c1 = nn.Conv2d(c_in, c_out, 3, stride, 1, bias=False)
        self.b1 = nn.BatchNorm2d(c_out)
        self.c2 = nn.Conv2d(c_out, c_out, 3, 1, 1, bias=False)
        self.b2 = nn.BatchNorm2d(c_out)
        self.atajo = nn.Identity() if stride == 1 and c_in == c_out else nn.Sequential(nn.Conv2d(c_in, c_out, 1, stride, bias=False), nn.BatchNorm2d(c_out))

    def forward(self, x):
        """Aplica el bloque."""
        h = torch.relu(self.b1(self.c1(x)))
        return torch.relu(self.b2(self.c2(h)) + self.atajo(x))
