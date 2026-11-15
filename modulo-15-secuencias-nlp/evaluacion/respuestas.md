# Respuestas — Módulo 15

1. Palabra: semántica directa, pero vocabulario enorme y OOV. Carácter: sin OOV, vocabulario mínimo, secuencias largas. Subpalabra: equilibrio, vocabulario fijo sin OOV.
2. El orden y la estructura sintáctica.
3. Aparece en casi todos los documentos, df ≈ N, así que log(N/df) ≈ 0.
4. PP = exp(−(1/N) Σ log p(wᵢ|·)). El modelo está tan "confundido" como si eligiera uniformemente entre 50 palabras.
5. Cualquier n-grama no visto tendría probabilidad 0 y anularía toda la oración (perplejidad infinita).
6. (1+1)/(4+10) = 1/7.
7. Las palabras que aparecen en contextos similares tienen significados similares.
8. L = −log σ(u_o·v_c) − Σ_{k=1}^{K} log σ(−u_k·v_c).
9. Aprenden co-ocurrencias del corpus, que reflejan estereotipos presentes en los textos.
10. Backpropagation a través del tiempo: desenrollar la RNN en T pasos y aplicar backprop sobre el grafo resultante.
11. ∂h_T/∂h_t contiene Π (diag(tanh')·W_hᵀ); su norma se comporta como ρ(W_h)^{T−t}: crece o decrece exponencialmente.
12. Explosión: gradient clipping. Desaparición: LSTM/GRU (o residuales/atención).
13. Entrada i, olvido f, candidata g, salida o; c_t = f⊙c_{t−1} + i⊙g, h_t = o⊙tanh(c_t).
14. Toda la entrada se comprime en un único vector de tamaño fijo.
15. Inicia con caracteres; cuenta pares adyacentes; fusiona el más frecuente; repite hasta el tamaño de vocabulario deseado; aplica fusiones en orden al tokenizar.
16. F1 a nivel de entidad: la mayoría de tokens son "O" y la exactitud sería alta aunque no detecte entidades.
17. Esperado: línea base TF-IDF + regresión logística; después fine-tuning de un modelo pequeño en español (BETO/RoBERTuito) o embeddings de sentence-transformers + clasificador; manejo de emojis/hashtags, F1 macro, validación estratificada.
