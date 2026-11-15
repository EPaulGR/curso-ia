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
    raise NotImplementedError  # TODO: implementa esta función


def rag(pregunta, documentos, llm, k=2):
    raise NotImplementedError  # TODO: implementa esta función
