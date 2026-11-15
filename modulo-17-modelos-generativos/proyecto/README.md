# Proyecto — Tres generadores sobre el mismo dataset

Dataset: MNIST/Fashion-MNIST (28×28) o CelebA reducido a 32×32.

## Requisitos
1. **VAE convolucional**: interpolaciones en el espacio latente y efecto de β.
2. **DCGAN**: documenta inestabilidades y cómo las resolviste.
3. **DDPM** con U-Net pequeña (reusa bloques del módulo 14) en `device="mps"`; compara muestreo DDPM (1000 pasos) vs DDIM (50 pasos).
4. Versión **condicional** por clase con guía sin clasificador.
5. Evalúa los tres con FID (usa tu ej07 con features de un clasificador entrenado por ti) y una cuadrícula de muestras.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Tres modelos funcionales | 30 |
| Difusión condicional con CFG | 15 |
| Evaluación cuantitativa (FID) correcta | 15 |
| Análisis comparativo (calidad, diversidad, costo) | 20 |
| Visualizaciones | 10 |
| Reproducibilidad | 10 |
