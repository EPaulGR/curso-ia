# Respuestas — Módulo 16

1. Procesamiento secuencial no paralelizable y dificultad para dependencias largas.
2. softmax(QKᵀ/√d_k)V. Q: consultas de cada posición, K: claves con las que se comparan, V: contenido que se mezcla según los pesos.
3. El producto punto crece en varianza con d_k; escalar evita saturar el softmax.
4. Se suma −∞ (o se rellena) en posiciones j > i antes del softmax; −∞ da peso exactamente 0 tras el softmax, mientras que un 0 en los puntajes seguiría dando peso positivo.
5. O(T²) en tiempo y memoria (por capa y cabeza).
6. Atender a distintos tipos de relaciones en subespacios distintos simultáneamente.
7. La atención es equivariante a permutaciones: sin posición, "perro muerde hombre" = "hombre muerde perro".
8. El producto punto entre q y k rotados depende solo de la posición relativa; extrapola mejor.
9. x ← x + Attn(LN(x)); x ← x + MLP(LN(x)).
10. LayerNorm centra y escala (μ, σ, γ, β); RMSNorm solo escala por la raíz media cuadrática (sin centrar ni β).
11. ln 65 ≈ 4.17.
12. Durante el entrenamiento se alimenta la secuencia real (no las predicciones) y se predice cada siguiente token en paralelo.
13. 12·24·1024² ≈ 302 M.
14. Conserva la masa de probabilidad mínima ≥ p; el número de candidatos se adapta: pocos cuando el modelo está seguro, más cuando está indeciso.
15. Guardar K y V de tokens anteriores para no recalcularlos; consume memoria proporcional a capas × T × d (× batch).
16. BERT: encoder bidireccional, Masked LM. GPT: decoder causal, siguiente token. T5: encoder–decoder con atención cruzada, objetivo de "span corruption" texto-a-texto.
17. Para un presupuesto de cómputo dado, escalar parámetros y tokens en proporción similar (~20 tokens/parámetro).
18. Esperado: tokenizador BPE, RoPE, RMSNorm, SwiGLU, mixed precision (bf16), `scaled_dot_product_attention`, gradient accumulation, schedule coseno con warmup, dataset de ~2 B tokens, checkpointing, posiblemente MLX para aprovechar la memoria unificada.
