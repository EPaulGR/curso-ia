"""Ej 07 — Clasificador de secuencias con Embedding + LSTM en PyTorch."""
import torch
from torch import nn

device = "mps" if torch.backends.mps.is_available() else "cpu"


class ClasificadorLSTM(nn.Module):
    """Embedding(V, e, padding_idx=0) → LSTM(e, h, batch_first) → Linear(h, c) sobre el último estado oculto."""

    def __init__(self, V, e, h, c):
        super().__init__()
        self.emb = nn.Embedding(V, e, padding_idx=0)
        self.lstm = nn.LSTM(e, h, batch_first=True)
        self.out = nn.Linear(h, c)

    def forward(self, x):
        """x (N, T) ids → logits (N, c)."""
        _, (h, _) = self.lstm(self.emb(x))
        return self.out(h[-1])


def entrenar(X, y, V, c, epocas=40, lr=1e-2, dispositivo=device):
    """Adam + entropía cruzada, batch completo. Devuelve (modelo, exactitud)."""
    torch.manual_seed(0)
    m = ClasificadorLSTM(V, 16, 32, c).to(dispositivo)
    opt = torch.optim.Adam(m.parameters(), lr=lr)
    X, y = X.to(dispositivo), y.to(dispositivo)
    for _ in range(epocas):
        opt.zero_grad()
        nn.functional.cross_entropy(m(X), y).backward()
        opt.step()
    with torch.no_grad():
        return m, (m(X).argmax(1) == y).float().mean().item()
