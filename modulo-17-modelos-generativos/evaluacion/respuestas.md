# Respuestas — Módulo 17

1. Discriminativo modela p(y|x); generativo modela p(x) (o p(x,y)) y puede muestrear datos.
2. p(x) = ∫p(x|z)p(z)dz es una integral intratable en alta dimensión.
3. ELBO = E_q[log p(x|z)] − KL(q(z|x)‖p(z)): calidad de reconstrucción y cercanía del posterior aproximado al prior.
4. Permite derivar a través del muestreo: z = μ + σε con ε independiente de los parámetros.
5. ½(σ² + μ² − 1 − log σ²) = ½(1 + 1 − 1 − 0) = 0.5.
6. El decoder ignora z y q(z|x) ≈ p(z): KL ≈ 0 pero el latente no codifica información.
7. min_G max_D E_x[log D(x)] + E_z[log(1 − D(G(z)))].
8. D* = p_d/(p_d + p_g); G minimiza la divergencia de Jensen–Shannon (2·JS − log 4).
9. Al inicio D rechaza fácilmente y log(1−D(G(z))) se satura con gradientes ≈ 0; −log D(G(z)) da gradientes fuertes.
10. G produce pocas variedades que engañan a D; mitigación: WGAN-GP, minibatch discrimination, unrolled GAN, normalización espectral.
11. Entrenar con t aleatorio en un solo paso, sin simular toda la cadena.
12. El ruido ε añadido; L = E‖ε − ε_θ(√ᾱ x₀ + √(1−ᾱ) ε, t)‖².
13. ∇_x log q(x_t|x₀) = −ε/√(1−ᾱ_t): predecir ε equivale a estimar el score (con signo y escala).
14. Combina predicciones condicional e incondicional, ε̂ = (1+w)ε_c − wε_u, para aumentar la fidelidad al condicionamiento a cambio de diversidad.
15. Reduce mucho la dimensión (cómputo y memoria) conservando la información perceptual; el autoencoder maneja los detalles.
16. ‖μ₁ − μ₂‖² + Tr(Σ₁ + Σ₂ − 2(Σ₁Σ₂)^{1/2}).
17. VAE: estable, rápido, diverso, borroso. GAN: alta calidad, rápida, inestable, menos diversa. Difusión: máxima calidad y diversidad, estable, muestreo lento (mitigado con DDIM/destilación).
18. Esperado: VAE preentrenado (latente), DiT o U-Net pequeña condicionada con embeddings de texto (CLIP/T5 congelados), flow matching o DDPM con CFG, dataset de imágenes con subtítulos de dominio acotado, entrenamiento en MLX/MPS en bf16, evaluación con FID y CLIP-score.
