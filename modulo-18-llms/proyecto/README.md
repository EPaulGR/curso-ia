# Proyecto 18 — Tu propio "tutor de IA" local

Construye y ajusta un modelo que responda preguntas sobre este curso.

## Entregables
1. Dataset propio de ≥ 300 pares pregunta/respuesta en `train.jsonl`/`valid.jsonl` (de los apuntes de los módulos 04–17).
2. Tokeniza tu corpus con TU BPE (ej. 1) y con el tokenizador del modelo; compara longitudes.
3. Fine-tuning LoRA con mlx-lm de un modelo de 1–3B. Gráfica de pérdida train/valid.
4. Evaluación: 30 preguntas no vistas, calificadas por ti (0–2) para el modelo base vs. el ajustado.
5. Cuantiza a 4-bit y mide tokens/s y memoria; compara con tu estimación del ej. 5.
6. Reporte (2–4 páginas) con conclusiones.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Calidad y tamaño del dataset | 20 |
| Entrenamiento correcto y curvas analizadas | 20 |
| Evaluación comparativa rigurosa | 25 |
| Mediciones de rendimiento vs. estimaciones | 15 |
| Reporte claro, reproducible | 20 |
