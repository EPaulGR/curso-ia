# Módulo 17 — Modelos generativos: VAE, GAN y difusión

**Fase 4 · Deep Learning** · Duración: 4 semanas (~50 h) · Prerrequisitos: 02 (probabilidad), 13, 14

## Objetivos
- Entender el modelado generativo como aprendizaje de p(x) y sus tres grandes familias.
- Derivar el ELBO y el truco de reparametrización; implementar un VAE.
- Entender el juego minimax de las GANs, sus inestabilidades y entrenar una.
- Derivar y programar un **modelo de difusión (DDPM)** desde cero.
- Evaluar generadores (FID, precisión/recall) y conocer el estado del arte (latent diffusion, flow matching).

## Temario
1. Discriminativo vs generativo; verosimilitud explícita vs implícita.
2. Autoencoders y VAE: ELBO, KL, reparametrización, β-VAE, espacio latente.
3. GAN: juego minimax, discriminador óptimo, JS-divergencia, colapso de modos, WGAN, DCGAN, StyleGAN.
4. Modelos autoregresivos (PixelCNN, GPT como generativo).
5. Flujos normalizantes (cambio de variable).
6. Difusión: proceso directo, calendarios, predicción de ruido, muestreo DDPM/DDIM, guía sin clasificador.
7. Latent diffusion (Stable Diffusion), flow matching, modelos de consistencia.
8. Evaluación: FID, IS, precisión/recall; riesgos (deepfakes, derechos) → módulo 22.
9. En Mac: Stable Diffusion con MLX / Core ML.

## Lecturas
- Prince, *UDL*, cap. 14 (introducción), 15 (GANs), 16 (flujos), 17 (VAE), 18 (difusión) — excelente.
- Bishop & Bishop (2024), cap. 16–20.
- Murphy, *Probabilistic ML: Advanced Topics*, cap. 20–25.
- Goodfellow et al., cap. 20.
- Papers: Kingma & Welling 2014 (VAE); Goodfellow et al. 2014 (GAN); Ho et al. 2020 (DDPM); Song et al. 2021 (DDIM, score SDE); Rombach et al. 2022 (Latent Diffusion); Lipman et al. 2023 (Flow Matching).
- Blog: Lilian Weng, *What are Diffusion Models?*

## Ejercicios
| # | Archivo | Tema |
|---|---|---|
| 01 | ej01_vae_matematicas.py | Reparametrización, KL, ELBO |
| 02 | ej02_vae.py | VAE en PyTorch |
| 03 | ej03_gan_perdidas.py | Pérdidas GAN y discriminador óptimo |
| 04 | ej04_gan_2d.py | GAN sobre una gaussiana 2D |
| 05 | ej05_difusion_directa.py | Calendario y proceso directo |
| 06 | ej06_ddpm.py | **DDPM completo**: entrenamiento y muestreo |
| 07 | ej07_fid.py | Distancia de Fréchet (FID) |

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Lecturas 10 %. Aprobado ≥ 8.
