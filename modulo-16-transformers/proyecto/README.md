# Proyecto — Entrena tu GPT en español

## Requisitos
1. Corpus: obras en español de dominio público (Cervantes, Galdós, Darío… Proyecto Gutenberg), ≥ 5 MB.
2. Parte 1 — mini-GPT de caracteres (tu ej07) en `device="mps"`: d=384, 6 capas, 6 cabezas, contexto 256. Curvas de entrenamiento/validación y muestras de texto a varias temperaturas.
3. Parte 2 — mejoras modernas: tokenizador BPE propio (módulo 15), RoPE, RMSNorm, SwiGLU, KV-cache en `generar`. Mide perplejidad por carácter para comparar de forma justa.
4. Parte 3 — reimplementa el modelo en **MLX** y compara velocidad (tokens/s de entrenamiento e inferencia) contra PyTorch/MPS.
5. Visualiza mapas de atención de 2 cabezas e interpreta.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Mini-GPT funcional, texto coherente a nivel de palabras | 25 |
| Mejoras modernas implementadas y evaluadas (ablación) | 25 |
| Versión MLX y benchmark | 15 |
| Visualización e interpretación de atención | 15 |
| Reporte (curvas, costo en FLOPs, conclusiones) | 10 |
| Reproducibilidad | 10 |
