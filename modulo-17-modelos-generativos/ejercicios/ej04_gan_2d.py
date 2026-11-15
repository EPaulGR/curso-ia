# EJERCICIO: implementa cada función marcada con TODO.
# Verifica con: pytest modulo-17-modelos-generativos

"""Ej 04 — GAN que aprende una distribución gaussiana 2D."""
import torch
from torch import nn
device = 'mps' if torch.backends.mps.is_available() else 'cpu'

def crear_redes(z=4, h=32):
    """Devuelve (G: z→2, D: 2→1 logit), MLPs con LeakyReLU."""
    raise NotImplementedError  # TODO

def entrenar_gan(muestrear_reales, pasos=1500, n=128, z=4, dispositivo=device):
    """Alterna un paso de D y uno de G (pérdida no saturante, Adam lr=1e-3, betas=(0.5,0.999)). Devuelve G."""
    raise NotImplementedError  # TODO
