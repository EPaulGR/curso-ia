# Respuestas — Módulo 13

1. XOR no es linealmente separable y el perceptrón solo traza un hiperplano.
2. Se vuelve una transformación lineal (afín) única, sin importar cuántas capas tenga.
3. ∂L/∂zᵢ = pᵢ − 1[i = y].
4. ∂L/∂W = aᵀδ; ∂L/∂b = Σ_batch δ; ∂L/∂a = δWᵀ.
5. Cada nodo se visita una vez en reversa y su derivada local cuesta lo mismo que su operación forward.
6. Los gradientes se multiplican por derivadas < 1 a través de muchas capas y tienden a 0; ReLU (derivada 1 en la zona activa), conexiones residuales y normalización lo mitigan.
7. Todas las neuronas de una capa recibirían el mismo gradiente y seguirían siendo idénticas (simetría).
8. Xavier: Var = 1/n_in (o 2/(n_in+n_out)) para tanh/sigmoide; He: 2/n_in para ReLU, compensando que ReLU anula la mitad.
9. Las medias móviles inician en 0 y están sesgadas hacia 0 al principio; dividir por (1−βᵗ) lo corrige.
10. Con Adam, L2 en la pérdida queda escalado por el paso adaptativo; AdamW aplica θ ← θ − ηλθ directamente, regularizando de forma uniforme.
11. Para que el valor esperado de la activación sea igual en entrenamiento e inferencia.
12. Una red de una capa oculta suficientemente ancha puede aproximar cualquier función continua; no dice cuántas neuronas, ni que se pueda aprender con gradiente, ni que generalice.
13. Sobreajustar un mini-batch, revisar la pérdida inicial (≈ log C en clasificación), gradient checking.
14. `device = "mps" if torch.backends.mps.is_available() else "cpu"`; evitar float64.
15. Sobreajuste.
16. Directo propaga derivadas de entrada a salida (barato si pocas entradas); reverso propaga de salida a entradas (barato si pocas salidas). Redes: una pérdida escalar y millones de parámetros → reverso.
