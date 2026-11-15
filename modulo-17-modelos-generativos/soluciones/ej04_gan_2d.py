"""Ej 04 — GAN que aprende una distribución gaussiana 2D."""
import torch
from torch import nn

device = "mps" if torch.backends.mps.is_available() else "cpu"


def crear_redes(z=4, h=32):
    """Devuelve (G: z→2, D: 2→1 logit), MLPs con LeakyReLU."""
    G = nn.Sequential(nn.Linear(z, h), nn.LeakyReLU(0.2), nn.Linear(h, h), nn.LeakyReLU(0.2), nn.Linear(h, 2))
    D = nn.Sequential(nn.Linear(2, h), nn.LeakyReLU(0.2), nn.Linear(h, h), nn.LeakyReLU(0.2), nn.Linear(h, 1))
    return G, D


def entrenar_gan(muestrear_reales, pasos=1500, n=128, z=4, dispositivo=device):
    """Alterna un paso de D y uno de G (pérdida no saturante, Adam lr=1e-3, betas=(0.5,0.999)). Devuelve G."""
    torch.manual_seed(0)
    G, D = (r.to(dispositivo) for r in crear_redes(z))
    oG = torch.optim.Adam(G.parameters(), 1e-3, betas=(0.5, 0.999))
    oD = torch.optim.Adam(D.parameters(), 1e-3, betas=(0.5, 0.999))
    bce = nn.BCEWithLogitsLoss()
    uno, cero = torch.ones(n, 1, device=dispositivo), torch.zeros(n, 1, device=dispositivo)
    for _ in range(pasos):
        real = muestrear_reales(n).to(dispositivo)
        falso = G(torch.randn(n, z, device=dispositivo))
        lD = bce(D(real), uno) + bce(D(falso.detach()), cero)
        oD.zero_grad(); lD.backward(); oD.step()
        lG = bce(D(falso), uno)
        oG.zero_grad(); lG.backward(); oG.step()
    return G
