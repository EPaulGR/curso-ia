# Módulo 19b — Agentes modernos, inferencia avanzada y multimodalidad

**Fase 5 · IA moderna** · Duración: 4–5 semanas (≈ 60 h) · Prerrequisitos: módulos 16, 18 y 19

El módulo 19 construyó el bucle básico de un agente y un sistema RAG. Este módulo sube al estado del arte de 2025–2026: agentes que se conectan a herramientas mediante **MCP**, que planifican, recuerdan y se coordinan entre sí, que programan y usan la computadora, y que se evalúan y aseguran con rigor. La segunda mitad trata la **ingeniería de inferencia**, que hace rápidos a los LLMs (decodificación especulativa, KV cache paginado, batching continuo, cuantización), y la **multimodalidad**.

## Objetivos
Al terminar podrás:
1. Implementar un servidor y un cliente MCP (JSON-RPC 2.0) y conectar herramientas propias a cualquier LLM.
2. Diseñar agentes con memoria, planes con dependencias y patrones multi-agente (orquestador-trabajadores).
3. Construir un agente de código con bucle editar → ejecutar → probar, y explicar cómo funcionan los agentes de *computer use*.
4. Evaluar agentes con pass@k, pass^k y métricas de trayectoria, e interpretar benchmarks (SWE-bench, OSWorld, OSWorld-MCP, τ-bench).
5. Identificar y mitigar *prompt injection*, exfiltración de datos y abusos de herramientas (sandbox, allowlists, spotlighting).
6. Implementar la decodificación especulativa y demostrar que preserva la distribución del modelo grande.
7. Explicar e implementar PagedAttention (KV cache paginado) y el batching continuo.
8. Elegir el formato de cuantización y el servidor adecuados en Mac (MLX, GGUF/llama.cpp, Ollama).
9. Explicar cómo un modelo de visión y lenguaje convierte imágenes en tokens, y entrenar la pérdida contrastiva de CLIP.
10. Curar datos y generar datos sintéticos de forma responsable (deduplicación, filtrado, decontaminación).

## Temario
| Semana | Tema | Ejercicio |
|---|---|---|
| 1 | Model Context Protocol: arquitectura, transportes, herramientas/recursos/prompts, SDK oficial | ej01 |
| 1 | Bucle de agente, memoria a corto y largo plazo, planificación con dependencias | ej02 |
| 2 | Multi-agente: orquestador-trabajadores, paralelismo, tolerancia a fallos | ej03 |
| 2 | Agentes de código y *computer use* | ej04 |
| 3 | Evaluación de agentes: pass@k, pass^k, trayectorias, benchmarks | ej05 |
| 3 | Seguridad: *prompt injection* directa e indirecta, permisos, sandbox | ej06 |
| 4 | Decodificación especulativa | ej07 |
| 4 | KV cache paginado y batching continuo; cuantización moderna; servir LLMs en Mac | ej08, ej09 |
| 5 | Multimodalidad (ViT, CLIP, VLMs), datos sintéticos y curación | ej10 |
| 5 | Proyecto | proyecto/ |

## Lecturas
- Especificación oficial de MCP: modelcontextprotocol.io (arquitectura, *lifecycle*, *tools*, seguridad).
- Anthropic, "Building effective agents" (2024): patrones de flujo y de agente.
- Yao et al., *ReAct* (2022); Shinn et al., *Reflexion* (2023); Park et al., *Generative Agents* (memoria, 2023).
- Jimenez et al., *SWE-bench* (2023); Xie et al., *OSWorld* (2024); Jia et al., *OSWorld-MCP* (ICLR 2026); Yao et al., *τ-bench* (2024, introduce pass^k).
- Chen et al., *Evaluating LLMs Trained on Code* (2021, estimador pass@k).
- Greshake et al., *Not what you've signed up for: indirect prompt injection* (2023); Hines et al., *Spotlighting* (2024).
- Leviathan et al., *Fast Inference from Transformers via Speculative Decoding* (2023); Chen et al., *Speculative sampling* (2023).
- Kwon et al., *PagedAttention / vLLM* (2023); Yu et al., *Orca* (batching continuo, 2022).
- Lin et al., *AWQ* (2023); Frantar et al., *GPTQ* (2022); documentación de GGUF (llama.cpp) y de cuantización de MLX.
- Dosovitskiy et al., *ViT* (2020); Radford et al., *CLIP* (2021); Liu et al., *LLaVA* (2023).
- Lee et al., *Deduplicating Training Data Makes LMs Better* (2021); Chip Huyen, *AI Engineering* caps. 6–9.
- Raschka, *Build a LLM from Scratch*, apéndices sobre inferencia.

## Evaluación
| Componente | Peso |
|---|---|
| Ejercicios (`pytest modulo-19b-agentes-e-inferencia`) | 30 % |
| Quiz ([evaluacion/quiz.md](evaluacion/quiz.md)) | 30 % |
| Proyecto ([proyecto/README.md](proyecto/README.md)) | 30 % |
| Lecturas: resumen de una página de OSWorld-MCP o de PagedAttention | 10 % |

```bash
pytest modulo-19b-agentes-e-inferencia
```
