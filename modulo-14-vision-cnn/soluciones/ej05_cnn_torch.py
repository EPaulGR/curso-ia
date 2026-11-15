"""Ej 05 — CNN pequeña en PyTorch (estilo LeNet) entrenada en MPS."""
import torch
from torch import nn

device = "mps" if torch.backends.mps.is_available() else "cpu"


class CNN(nn.Module):
    """conv(1→8,3,p1)→ReLU→MaxPool2 → conv(8→16,3,p1)→ReLU→MaxPool2 → Flatten → Linear(16·(s/4)²→n_clases)."""

    def __init__(self, n_clases, tam=16):
        super().__init__()
        self.f = nn.Sequential(nn.Conv2d(1, 8, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2), nn.Conv2d(8, 16, 3, padding=1), nn.ReLU(), nn.MaxPool2d(2), nn.Flatten(), nn.Linear(16 * (tam // 4) ** 2, n_clases))

    def forward(self, x):
        """x (N,1,tam,tam) → logits (N, n_clases)."""
        return self.f(x)


def entrenar(X, y, n_clases, epocas=30, lr=3e-3, dispositivo=device):
    """Entrena con Adam en mini-batches de 32. Devuelve (modelo, exactitud)."""
    torch.manual_seed(0)
    m = CNN(n_clases, X.shape[-1]).to(dispositivo)
    opt = torch.optim.Adam(m.parameters(), lr=lr)
    X, y = X.to(dispositivo), y.to(dispositivo)
    for _ in range(epocas):
        perm = torch.randperm(len(X), device=dispositivo)
        for i in range(0, len(X), 32):
            b = perm[i:i + 32]
            opt.zero_grad()
            nn.functional.cross_entropy(m(X[b]), y[b]).backward()
            opt.step()
    with torch.no_grad():
        return m, (m(X).argmax(1) == y).float().mean().item()
