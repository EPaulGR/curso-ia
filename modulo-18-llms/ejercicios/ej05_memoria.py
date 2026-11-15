"""Ejercicio 5 — Estimar memoria para correr/ajustar LLMs (planear tu M5 Ultra).

- `memoria_pesos_gb(n_params, bits)`: n_params * bits/8 / 1e9.
- `memoria_kv_cache_gb(n_capas, d_modelo, contexto, batch=1, bytes_=2, n_kv_heads=None, n_heads=None)`:
  2 (K y V) * capas * contexto * batch * d_kv * bytes / 1e9, donde d_kv = d_modelo * n_kv_heads/n_heads
  si se dan (GQA), si no d_modelo.
- `memoria_inferencia_gb(...)`: pesos + kv, todo * 1.2 de sobrecarga.
- `memoria_full_finetune_gb(n_params)`: Adam en fp32 mixto ≈ 16 bytes/param.
- `cabe(memoria_gb, ram_gb, reserva_so=0.25)`: True si memoria <= ram*(1-reserva).
"""


def memoria_pesos_gb(n_params, bits):
    raise NotImplementedError  # TODO: implementa esta función


def memoria_kv_cache_gb(n_capas, d_modelo, contexto, batch=1, bytes_=2, n_kv_heads=None, n_heads=None):
    raise NotImplementedError  # TODO: implementa esta función


def memoria_inferencia_gb(n_params, bits, n_capas, d_modelo, contexto, **kw):
    raise NotImplementedError  # TODO: implementa esta función


def memoria_full_finetune_gb(n_params):
    raise NotImplementedError  # TODO: implementa esta función


def cabe(memoria_gb, ram_gb, reserva_so=0.25):
    raise NotImplementedError  # TODO: implementa esta función
