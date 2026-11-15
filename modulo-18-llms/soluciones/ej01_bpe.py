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
    c = {}
    for p in zip(ids, ids[1:]):
        c[p] = c.get(p, 0) + 1
    return c


def fusionar(ids, par, nuevo_id):
    out, i = [], 0
    while i < len(ids):
        if i + 1 < len(ids) and (ids[i], ids[i + 1]) == par:
            out.append(nuevo_id)
            i += 2
        else:
            out.append(ids[i])
            i += 1
    return out


def entrenar_bpe(texto, n_fusiones):
    ids = list(texto.encode("utf-8"))
    fusiones = {}
    for k in range(n_fusiones):
        c = contar_pares(ids)
        if not c:
            break
        par = min(c, key=lambda p: (-c[p], p))
        fusiones[par] = 256 + k
        ids = fusionar(ids, par, 256 + k)
    return fusiones


def codificar(texto, fusiones):
    ids = list(texto.encode("utf-8"))
    for par, nid in fusiones.items():
        ids = fusionar(ids, par, nid)
    return ids


def decodificar(ids, fusiones):
    vocab = {i: bytes([i]) for i in range(256)}
    for (a, b), nid in fusiones.items():
        vocab[nid] = vocab[a] + vocab[b]
    return b"".join(vocab[i] for i in ids).decode("utf-8", errors="replace")
