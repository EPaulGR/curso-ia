# Proyecto 18b — Tu propio mini "modelo de razonamiento" con GRPO en Apple Silicon

## Objetivo
Tomar un LLM pequeño (0.5B–1.5B, p. ej. una variante *Instruct* de Qwen o SmolLM en formato MLX o Hugging Face) y mejorar su exactitud en aritmética de varios pasos con **GRPO y recompensas verificables**, corriendo en tu Mac (MLX o PyTorch con `device="mps"`).

## Etapas
1. **Dataset sintético verificable:** genera ≥ 5 000 problemas (expresiones de 2–4 operaciones, problemas verbales simples) con su respuesta exacta. Sepáralos en train, val y test sin solapamiento.
2. **Línea base:** evalúa el modelo base con el formato `... Respuesta: <número>`. Mide pass@1, pass@8 (con `ej08.pass_at_k`) y self-consistency@8.
3. **Recompensa:** 1 si `extraer_respuesta` coincide exactamente, +0.1 por respetar el formato, 0 en otro caso. Documenta cualquier intento de *reward hacking* que observes.
4. **GRPO:** implementa el bucle completo:
   - G = 4–8 respuestas por prompt, ventajas de grupo (`ej09.ventajas_grupo`), razón de probabilidades recortada y penalización KL contra el modelo de referencia congelado.
   - Si la memoria no alcanza, usa LoRA (módulo 18) en lugar de ajustar todos los pesos.
   - Opcional: usa librerías (p. ej. `trl` con GRPOTrainer, o implementaciones para MLX), pero **primero** tu versión mínima.
5. **Evaluación:** compara base vs. RL en el test: pass@1, pass@k para k ∈ {1, 4, 16, 64} (reproduce la curva del debate RLVR), longitud media de las respuestas y ejemplos de autocorrección.
6. **Cómputo en inferencia:** grafica la exactitud contra el número de muestras para el voto de mayoría, en el modelo base y en el entrenado.
7. **Reporte:** usa la plantilla del módulo 23. Incluye memoria pico, tokens por segundo, tiempo total y la configuración de la Mac.

## Entregables
`proyecto/` con código, `datos/` generados por script (no subas datos grandes), `reporte.md` con gráficas, y semillas fijas.

## Rúbrica (10 puntos)
| Criterio | Puntos |
|---|---|
| Dataset y verificador correctos, sin fuga entre splits | 1.5 |
| Línea base rigurosa (pass@k, self-consistency) | 1.5 |
| Implementación GRPO correcta (ventajas, clip, KL) y explicada | 2.5 |
| Mejora medible y estadísticamente defendida en test (bootstrap del módulo 23) | 1.5 |
| Análisis pass@k a k grande y postura argumentada en el debate RLVR | 1.5 |
| Ingeniería en Apple Silicon: memoria, velocidad, reproducibilidad | 1.0 |
| Calidad del reporte | 0.5 |

**Reto opcional:** reemplaza la recompensa exacta por un PRM simple (verifica cada paso intermedio "a op b = c") y compara.
