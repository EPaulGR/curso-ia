"""Ej 07 — Mini-GPT a nivel de caracteres (entrénalo en MPS con un libro completo)."""
import torch
from torch import nn
import importlib.util, pathlib

_spec = importlib.util.spec_from_file_location("bl", pathlib.Path(__file__).with_name("ej06_bloque.py"))
_bl = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(_bl)

device = "mps" if torch.backends.mps.is_available() else "cpu"


class TokenizadorCaracteres:
    """Mapea cada carácter distinto del texto a un entero."""

    def __init__(self, texto):
        self.chars = sorted(set(texto))
        self.stoi = {c: i for i, c in enumerate(self.chars)}

    def codificar(self, s):
        """str → lista de ids."""
        return [self.stoi[c] for c in s]

    def decodificar(self, ids):
        """lista de ids → str."""
        return "".join(self.chars[i] for i in ids)


class MiniGPT(nn.Module):
    """Embeddings de token + posición aprendida → n bloques → LayerNorm → cabeza lineal (pesos atados al embedding)."""

    def __init__(self, V, d=64, h=4, n=2, T=64, dropout=0.0):
        super().__init__()
        self.T = T
        self.tok = nn.Embedding(V, d)
        self.pos = nn.Embedding(T, d)
        self.bloques = nn.Sequential(*[_bl.Bloque(d, h, dropout) for _ in range(n)])
        self.ln = nn.LayerNorm(d)
        self.cabeza = nn.Linear(d, V, bias=False)
        self.cabeza.weight = self.tok.weight

    def forward(self, idx, objetivos=None):
        """idx (N,T') → (logits (N,T',V), pérdida o None)."""
        N, T = idx.shape
        x = self.tok(idx) + self.pos(torch.arange(T, device=idx.device))
        logits = self.cabeza(self.ln(self.bloques(x)))
        loss = None
        if objetivos is not None:
            loss = nn.functional.cross_entropy(logits.view(-1, logits.size(-1)), objetivos.view(-1))
        return logits, loss

    @torch.no_grad()
    def generar(self, idx, n_nuevos, temperatura=1.0):
        """Muestreo autoregresivo de n_nuevos tokens."""
        for _ in range(n_nuevos):
            logits, _ = self(idx[:, -self.T:])
            p = torch.softmax(logits[:, -1] / temperatura, -1)
            idx = torch.cat([idx, torch.multinomial(p, 1)], 1)
        return idx


def lotes(datos, T, N, gen):
    """Muestra N ventanas aleatorias de longitud T; devuelve (x, y) con y desplazado una posición."""
    i = torch.randint(len(datos) - T - 1, (N,), generator=gen)
    x = torch.stack([datos[j:j + T] for j in i])
    y = torch.stack([datos[j + 1:j + T + 1] for j in i])
    return x, y


def entrenar(texto, pasos=300, T=32, N=32, lr=3e-3, dispositivo=device, **kw):
    """Entrena con AdamW. Devuelve (modelo, tokenizador, historial_de_perdidas)."""
    torch.manual_seed(0)
    gen = torch.Generator().manual_seed(0)
    tok = TokenizadorCaracteres(texto)
    datos = torch.tensor(tok.codificar(texto))
    m = MiniGPT(len(tok.chars), T=T, **kw).to(dispositivo)
    opt = torch.optim.AdamW(m.parameters(), lr=lr)
    hist = []
    for _ in range(pasos):
        x, y = lotes(datos, T, N, gen)
        _, loss = m(x.to(dispositivo), y.to(dispositivo))
        opt.zero_grad()
        loss.backward()
        opt.step()
        hist.append(loss.item())
    return m, tok, hist
