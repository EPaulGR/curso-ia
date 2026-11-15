# Proyecto 19 — Asistente RAG + agente sobre los apuntes del curso

## Requisitos
1. Indexa todos los `teoria.md` y `README.md` del curso (chunking por secciones, metadatos de módulo).
2. Recuperación híbrida (BM25/TF-IDF + embeddings) con reranking o MMR.
3. Generación con LLM local (Ollama/mlx-lm) y opción de API de Claude (`claude-opus-5-5`), con citas.
4. Agente con ≥ 3 herramientas: buscar_apuntes, ejecutar_tests(modulo), calculadora.
5. Conjunto dorado de 50 preguntas; reporta P@5, MRR, fidelidad y EM/F1.
6. Prueba al menos 3 ataques de inyección de prompt y documenta las defensas.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Pipeline de recuperación y ablaciones (denso vs. híbrido vs. rerank) | 25 |
| Generación con citas fiables | 15 |
| Agente robusto (errores, límites, permisos) | 20 |
| Evaluación con conjunto dorado | 25 |
| Seguridad y reporte | 15 |
