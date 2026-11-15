# Capstone — Proyecto final del curso

Un proyecto que demuestre dominio de IA "de arriba a abajo". Debe integrar **al menos tres fases** del curso (p. ej. búsqueda/metaheurísticas + deep learning + LLMs/RL).

## Ejemplos de temas
1. **Optimizador híbrido**: un LLM que propone heurísticas y un AG/NSGA-II (módulo 07) las evoluciona para ruteo de vehículos en Puebla (estilo FunSearch).
2. **Agente de juego** tipo AlphaZero para un juego de tablero propio (06 + 13 + 20).
3. **Asistente médico/legal en español** con RAG, LLM ajustado con LoRA en MLX, evaluación de fidelidad y auditoría ética (18 + 19 + 22).
4. **Visión para el campo**: detección de plagas en cultivos con CNN/ViT cuantizada a Core ML en iPhone (14 + 21).
5. **Reproducción + extensión** de un paper reciente con una pregunta nueva.

## Fases
| Semana | Entregable |
|---|---|
| 1 | Propuesta (`plantillas/propuesta.md`) |
| 2–3 | Datos, baseline y conjunto de evaluación |
| 4–7 | Método principal, experimentos multi-semilla |
| 8 | Ablaciones, pruebas estadísticas, análisis de errores |
| 9 | Auditoría ética/robustez (módulo 22) |
| 10 | Reporte final, repositorio público, charla de 15 min (grábala) |

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Relevancia y claridad del problema | 10 |
| Profundidad técnica e integración de ≥ 3 fases | 25 |
| Rigor experimental (baselines, semillas, estadística, ablaciones) | 25 |
| Reproducibilidad (código, entorno, instrucciones) | 15 |
| Ética, limitaciones, impacto | 10 |
| Comunicación (reporte y charla) | 15 |

**Aprobado como "experto":** ≥ 85 pts y que alguien más pueda reproducir tus resultados siguiendo tu README.
