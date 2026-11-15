"""Ejercicio 1 — Tokenizador BPE (Byte Pair Encoding) desde cero.

Implementa:
- `contar_pares(ids)`: dict {(a, b): frecuencia} de pares consecutivos.
- `fusionar(ids, par, nuevo_id)`: reemplaza cada aparición de `par` por `nuevo_id`.
- `entrenar_bpe(texto, n_fusiones)`: parte de los bytes UTF-8 (ids 0-255) y aplica
  `n_fusiones` fusiones del par más frecuente (desempate: el par menor). Devuelve
  dict {(a, b): nuevo_id} en orden, con nuevo_id = 256, 257, ...
- `codificar(texto, fusiones)` y `decodificar(ids, fusiones)` (ida y vuelta exacta).
Referencia: Sennrich et al. 2016; Karpathy, "Let's build the GPT Tokenizer".
"""


def contar_pares(ids):
    raise NotImplementedError  # TODO: implementa esta función


def fusionar(ids, par, nuevo_id):
    raise NotImplementedError  # TODO: implementa esta función


def entrenar_bpe(texto, n_fusiones):
    raise NotImplementedError  # TODO: implementa esta función


def codificar(texto, fusiones):
    raise NotImplementedError  # TODO: implementa esta función


def decodificar(ids, fusiones):
    raise NotImplementedError  # TODO: implementa esta función
