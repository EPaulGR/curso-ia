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
    raise NotImplementedError  # TODO: implementa esta función


def tamano_modelo_mb(n_params, dtype):
    raise NotImplementedError  # TODO: implementa esta función


def plan_despliegue(n_params, ram_gb):
    raise NotImplementedError  # TODO: implementa esta función
