"""Ejercicio 4 — Pipeline RAG (Retrieval-Augmented Generation).

`llm` es cualquier función str -> str (en los tests, un mock; en la práctica Ollama,
mlx-lm o la API de Claude con model="claude-opus-5-5").
- `construir_prompt(pregunta, contextos)`: incluye cada contexto numerado como "[1] ...",
  la instrucción de responder SOLO con el contexto y citar las fuentes, y la pregunta.
- `rag(pregunta, documentos, llm, k=2)`: TF-IDF (ej01) sobre documentos, recupera top-k,
  construye prompt, llama a llm. Devuelve dict {"respuesta", "fuentes": [índices]}.
"""
import importlib.util
from pathlib import Path

_spec = importlib.util.spec_from_file_location("ej01", Path(__file__).with_name("ej01_embeddings.py"))
ej01 = importlib.util.module_from_spec(_spec)
_spec.loader.exec_module(ej01)


def construir_prompt(pregunta, contextos):
    ctx = "\n".join(f"[{i + 1}] {c}" for i, c in enumerate(contextos))
    return ("Responde usando SOLO el contexto. Cita las fuentes como [n]. "
            "Si no está en el contexto, di que no lo sabes.\n\n"
            f"Contexto:\n{ctx}\n\nPregunta: {pregunta}\nRespuesta:")


def rag(pregunta, documentos, llm, k=2):
    vocab, idf = ej01.calcular_idf(documentos)
    M = [ej01.vectorizar(d, vocab, idf) for d in documentos]
    q = ej01.vectorizar(pregunta, vocab, idf)
    sims = [ej01.similitud_coseno(q, m) for m in M]
    fuentes = sorted(range(len(documentos)), key=lambda i: -sims[i])[:k]
    prompt = construir_prompt(pregunta, [documentos[i] for i in fuentes])
    return {"respuesta": llm(prompt), "fuentes": fuentes}
