"""Ejercicio 5 — Selección de dispositivo y conversión (PyTorch MPS, MLX, Core ML).

- `elegir_dispositivo(prefer="auto")`: devuelve "mps" si PyTorch está instalado y MPS disponible,
  si no "cpu". Con prefer="cpu" devuelve "cpu". No debe fallar si torch no está instalado.
- `tamano_modelo_mb(n_params, dtype)`: dtype en {"float32", "float16", "bfloat16", "int8", "int4"}.
- `plan_despliegue(n_params, ram_gb)`: elige la precisión más alta (float16 > int8 > int4) cuyo
  tamaño quepa en 60 % de la RAM; si ninguna cabe devuelve None.
Práctica (fuera de tests): exportar un modelo PyTorch a Core ML con coremltools
(`ct.convert(torch.jit.trace(m, x), inputs=[ct.TensorType(shape=x.shape)])`).
"""
import importlib.util

_BYTES = {"float32": 4, "float16": 2, "bfloat16": 2, "int8": 1, "int4": 0.5}


def elegir_dispositivo(prefer="auto"):
    if prefer == "cpu" or importlib.util.find_spec("torch") is None:
        return "cpu"
    import torch
    return "mps" if torch.backends.mps.is_available() else "cpu"


def tamano_modelo_mb(n_params, dtype):
    return n_params * _BYTES[dtype] / 1e6


def plan_despliegue(n_params, ram_gb):
    for d in ("float16", "int8", "int4"):
        if tamano_modelo_mb(n_params, d) / 1e3 <= 0.6 * ram_gb:
            return d
    return None
