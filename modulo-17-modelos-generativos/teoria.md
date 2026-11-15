# Teoría — Modelos generativos

## 1. Objetivo
Aprender p_θ(x) ≈ p_datos(x) para **muestrear** datos nuevos (y a veces evaluar su densidad). Familias:
| Familia | Verosimilitud | Muestreo | Ejemplo |
|---|---|---|---|
| Autoregresivos | exacta | lento (secuencial) | GPT, PixelCNN |
| VAE | cota (ELBO) | rápido | VAE, VQ-VAE |
| GAN | implícita | rápido | StyleGAN |
| Flujos | exacta | rápido | RealNVP, Glow |
| Difusión | cota | iterativo | DDPM, Stable Diffusion |

## 2. VAE
Modelo latente p(x) = ∫ p(x|z)p(z)dz, intratable. Introducimos un encoder q_φ(z|x) y maximizamos el **ELBO**:
log p(x) ≥ E_q[log p(x|z)] − KL(q(z|x) ‖ p(z)).
Reconstrucción + regularización del latente. Con q gaussiana y p(z)=N(0,I):
KL = −½ Σ(1 + log σ² − μ² − σ²).
**Reparametrización**: z = μ + σ⊙ε, ε~N(0,I): la aleatoriedad sale del grafo y se puede derivar respecto a μ y σ. β-VAE pondera la KL (más β → latentes más desenredados, reconstrucciones más borrosas). Con β muy grande ocurre el **colapso posterior**.

## 3. GAN
Juego: min_G max_D E[log D(x)] + E[log(1 − D(G(z)))].
- D óptimo: D*(x) = p_d/(p_d + p_g). Con él, G minimiza 2·JS(p_d‖p_g) − log 4.
- En la práctica G usa la pérdida **no saturante** −log D(G(z)) (gradientes fuertes al inicio).
- Problemas: inestabilidad, colapso de modos, sin métrica de progreso. Soluciones: WGAN(-GP) con distancia de Wasserstein, normalización espectral, arquitecturas DCGAN/StyleGAN.

## 4. Difusión (DDPM)
**Directo**: añadir ruido gaussiano en T pasos: q(x_t|x_{t−1}) = N(√(1−β_t)x_{t−1}, β_t I). Con α_t = 1−β_t y ᾱ_t = Πα_s se salta directo:
x_t = √ᾱ_t x₀ + √(1−ᾱ_t) ε.
**Inverso**: una red ε_θ(x_t, t) aprende a predecir el ruido. Pérdida simplificada: E‖ε − ε_θ(x_t,t)‖².
**Muestreo** (ancestral): x_{t−1} = (1/√α_t)(x_t − β_t/√(1−ᾱ_t)·ε_θ) + √β_t z.
Interpretación: ε_θ estima el **score** ∇log p(x_t) (difusión = score matching a múltiples niveles de ruido). DDIM muestrea en muchos menos pasos de forma determinista.
**Guía sin clasificador**: entrenar condicional e incondicional y extrapolar ε = (1+w)ε_cond − w ε_uncond; controla adherencia al prompt.
**Latent diffusion**: difundir en el latente de un autoencoder (8× más pequeño) — Stable Diffusion. El denoiser es una U-Net o un Transformer (DiT).
**Flow matching**: aprender un campo de velocidades que transporta ruido a datos en línea recta; base de modelos recientes (SD3, Flux).

## 5. Evaluación
**FID**: distancia de Fréchet entre gaussianas ajustadas a features de Inception de imágenes reales y generadas:
‖μ_r − μ_g‖² + Tr(Σ_r + Σ_g − 2(Σ_rΣ_g)^{1/2}). Menor es mejor. Precisión (calidad) y recall (diversidad) separan ambos aspectos.

## 6. En Mac
`mlx-examples` incluye Stable Diffusion/Flux en MLX; Apple publicó `ml-stable-diffusion` para Core ML. Con mucha memoria unificada puedes correr modelos grandes de imagen sin cuantizar.
