"""Ej 06 — DDPM mínimo: red que predice el ruido sobre datos 2D, entrenamiento y muestreo."""
import torch
from torch import nn

device = "mps" if torch.backends.mps.is_available() else "cpu"


class Denoiser(nn.Module):
    """MLP que recibe (x_t, t/T) y predice ε."""

    def __init__(self, d=2, h=128):
        super().__init__()
        self.f = nn.Sequential(nn.Linear(d + 1, h), nn.SiLU(), nn.Linear(h, h), nn.SiLU(), nn.Linear(h, d))

    def forward(self, x, t_norm):
        """x (N,d), t_norm (N,1)."""
        return self.f(torch.cat([x, t_norm], -1))


def entrenar_ddpm(X, T=100, pasos=2000, lr=2e-3, dispositivo=device):
    """Pérdida simple: ‖ε - ε_θ(x_t, t)‖². Devuelve (modelo, betas, alpha_barras)."""
    torch.manual_seed(0)
    betas = torch.linspace(1e-4, 0.05, T)
    ab = torch.cumprod(1 - betas, 0)
    m = Denoiser(X.shape[1]).to(dispositivo)
    opt = torch.optim.Adam(m.parameters(), lr)
    X, abd = X.to(dispositivo), ab.to(dispositivo)
    for _ in range(pasos):
        x0 = X[torch.randint(len(X), (256,), device=dispositivo)]
        t = torch.randint(T, (256,), device=dispositivo)
        eps = torch.randn_like(x0)
        a = abd[t][:, None]
        xt = a.sqrt() * x0 + (1 - a).sqrt() * eps
        loss = ((m(xt, t[:, None].float() / T) - eps) ** 2).mean()
        opt.zero_grad(); loss.backward(); opt.step()
    return m, betas, ab


@torch.no_grad()
def muestrear(m, betas, ab, n, d=2, dispositivo=device):
    """Muestreo ancestral DDPM: x_{t-1} = (x_t - β_t/√(1-ᾱ_t)·ε_θ)/√α_t + √β_t·z."""
    T = len(betas)
    x = torch.randn(n, d, device=dispositivo)
    for t in reversed(range(T)):
        b, a_bar = betas[t].item(), ab[t].item()
        eps = m(x, torch.full((n, 1), t / T, device=dispositivo))
        x = (x - b / (1 - a_bar) ** 0.5 * eps) / (1 - b) ** 0.5
        if t > 0:
            x = x + b ** 0.5 * torch.randn_like(x)
    return x
