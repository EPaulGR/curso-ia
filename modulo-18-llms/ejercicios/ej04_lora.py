"""Ejercicio 4 — LoRA (Low-Rank Adaptation) en NumPy.

Una capa lineal congelada W (d_out x d_in) se adapta con W' = W + (alpha/r) * B @ A,
con A (r x d_in) ~ N(0, 0.01) y B (d_out x r) = 0 al inicio.
Implementa la clase `LoRALineal`:
- `forward(x)`: x (n x d_in) -> (n x d_out).
- `paso_sgd(x, y, lr)`: un paso de descenso de gradiente sobre MSE actualizando SOLO A y B;
  devuelve la pérdida antes del paso.
- `fusionar()`: devuelve la matriz W' fusionada.
- `n_parametros_entrenables()`.
Paper: Hu et al. 2021, "LoRA: Low-Rank Adaptation of Large Language Models".
"""
import numpy as np


class LoRALineal:

    def __init__(self, W, r=4, alpha=8, seed=0):
        rng = np.random.default_rng(seed)
        self.W = np.asarray(W, float)
        d_out, d_in = self.W.shape
        self.A = rng.normal(0, 0.01, (r, d_in))
        self.B = np.zeros((d_out, r))
        self.s = alpha / r

    def forward(self, x):
        raise NotImplementedError  # TODO: implementa esta función

    def paso_sgd(self, x, y, lr=0.01):
        raise NotImplementedError  # TODO: implementa esta función

    def fusionar(self):
        raise NotImplementedError  # TODO: implementa esta función

    def n_parametros_entrenables(self):
        raise NotImplementedError  # TODO: implementa esta función
