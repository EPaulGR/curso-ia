# Módulo 19 — RAG, agentes y evaluación de LLMs

**Duración:** 3–4 semanas (~45 h) · **Prerrequisitos:** 18

## Objetivos
- Construir sistemas de recuperación aumentada (RAG) completos: chunking, embeddings, índice vectorial, reranking, generación con citas.
- Diseñar agentes con herramientas (tool use) robustos: bucle, manejo de errores, límites.
- Evaluar sistemas LLM con métricas objetivas y con LLM-como-juez.

## Temario
1. Embeddings densos vs. dispersos (TF-IDF, BM25), búsqueda híbrida.
2. Bases vectoriales y ANN (HNSW, IVF, cuantización de producto).
3. Chunking, metadatos, reranking (cross-encoders), MMR.
4. RAG avanzado: reescritura de consultas, HyDE, GraphRAG, RAG agentivo.
5. Agentes: ReAct, tool use, planificación, memoria, multiagente, MCP (Model Context Protocol).
6. Evaluación: precisión@k, MRR, nDCG, EM/F1, fidelidad (faithfulness), LLM-as-judge, conjuntos dorados.
7. Seguridad: inyección de prompts, exfiltración por herramientas, permisos mínimos.

## Lecturas
- Chip Huyen, *AI Engineering*: caps. 3–6.
- Jurafsky & Martin, *SLP3*: cap. 14 (QA y recuperación de información).
- Papers: Lewis 2020 (RAG), Karpukhin 2020 (DPR), Yao 2022 (ReAct), Schick 2023 (Toolformer), Gao 2022 (HyDE), Zheng 2023 (LLM-as-a-judge), Malkov 2016 (HNSW).
- Documentación: Anthropic "Building effective agents"; API de Claude, sección tool use (modelo por defecto `claude-opus-5-5`); Ollama API.

## Ejercicios
| # | Archivo | Tema |
|---|---|---|
| 1 | ej01_embeddings.py | TF-IDF y coseno |
| 2 | ej02_indice_vectorial.py | Búsqueda exacta y MMR |
| 3 | ej03_chunking.py | Ventanas y párrafos |
| 4 | ej04_rag.py | Pipeline RAG con LLM intercambiable |
| 5 | ej05_agente.py | Bucle de agente con herramientas |
| 6 | ej06_metricas.py | Métricas de recuperación y QA |

Reto extra: sustituye el TF-IDF por `sentence-transformers` (corre en MPS) y el mock por Ollama o `mlx_lm`.

## Criterios
Tests (30 %), quiz (30 %), proyecto (30 %), análisis escrito de un fallo de RAG (10 %).
