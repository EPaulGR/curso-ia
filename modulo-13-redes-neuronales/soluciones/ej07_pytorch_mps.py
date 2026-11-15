"""Ej 07 — El mismo MLP en PyTorch usando la GPU de Apple (MPS)."""
import torch
from torch import nn

device = "mps" if torch.backends.mps.is_available() else "cpu"


def crear_modelo(d, h, c):
    """nn.Sequential: Linear(d,h) → ReLU → Linear(h,c)."""
    return nn.Sequential(nn.Linear(d, h), nn.ReLU(), nn.Linear(h, c))


def entrenar_torch(X, y, h=32, epocas=200, lr=1e-2, dispositivo=device):
    """Entrena con Adam y CrossEntropyLoss. X, y: tensores CPU. Devuelve (modelo, exactitud_entrenamiento)."""
    torch.manual_seed(0)
    X, y = X.to(dispositivo), y.to(dispositivo)
    m = crear_modelo(X.shape[1], h, int(y.max()) + 1).to(dispositivo)
    opt = torch.optim.Adam(m.parameters(), lr=lr)
    f = nn.CrossEntropyLoss()
    for _ in range(epocas):
        opt.zero_grad()
        loss = f(m(X), y)
        loss.backward()
        opt.step()
    with torch.no_grad():
        acc = (m(X).argmax(1) == y).float().mean().item()
    return m, acc
