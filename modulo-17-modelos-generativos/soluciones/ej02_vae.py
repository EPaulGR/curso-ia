"""Ej 02 — Autoencoder variacional en PyTorch."""
import torch
from torch import nn

device = "mps" if torch.backends.mps.is_available() else "cpu"


class VAE(nn.Module):
    """Encoder MLP → (μ, logvar) de dim z; decoder MLP → reconstrucción."""

    def __init__(self, d, z=2, h=64):
        super().__init__()
        self.enc = nn.Sequential(nn.Linear(d, h), nn.ReLU(), nn.Linear(h, 2 * z))
        self.dec = nn.Sequential(nn.Linear(z, h), nn.ReLU(), nn.Linear(h, d))

    def forward(self, x):
        """Devuelve (x_rec, mu, logvar)."""
        mu, logvar = self.enc(x).chunk(2, -1)
        z = mu + torch.exp(0.5 * logvar) * torch.randn_like(mu)
        return self.dec(z), mu, logvar


def perdida_vae(x, x_rec, mu, logvar, beta=1.0):
    """MSE sumada por muestra + β·KL, promediada en el batch."""
    rec = ((x - x_rec) ** 2).sum(-1)
    kl = -0.5 * (1 + logvar - mu ** 2 - logvar.exp()).sum(-1)
    return (rec + beta * kl).mean()


def entrenar(X, pasos=500, lr=3e-3, beta=0.05, dispositivo=device):
    """Entrena con Adam usando perdida_vae con el β dado; devuelve (modelo, historial)."""
    torch.manual_seed(0)
    m = VAE(X.shape[1]).to(dispositivo)
    opt = torch.optim.Adam(m.parameters(), lr=lr)
    X = X.to(dispositivo)
    hist = []
    for _ in range(pasos):
        loss = perdida_vae(X, *m(X), beta=beta)
        opt.zero_grad()
        loss.backward()
        opt.step()
        hist.append(loss.item())
    return m, hist
