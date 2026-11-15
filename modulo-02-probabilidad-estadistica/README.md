# Módulo 02 — Probabilidad, estadística y teoría de la información

**Duración:** 4–5 semanas (50–60 h) · **Fase 0** · Base de los módulos 10, 11, 17, 18

## Objetivos
- Razonar con probabilidad condicional y el teorema de Bayes.
- Conocer las distribuciones principales y simular con Monte Carlo.
- Estimar parámetros (MLE, MAP) y cuantificar incertidumbre (intervalos, bootstrap, pruebas de hipótesis).
- Dominar entropía, entropía cruzada y divergencia KL: las funciones de pérdida de la IA moderna.

## Temario
1. Espacios muestrales, axiomas, probabilidad condicional, independencia, regla de la cadena.
2. Teorema de Bayes, razonamiento diagnóstico, falacia de la tasa base.
3. Variables aleatorias discretas y continuas: Bernoulli, binomial, Poisson, categórica, uniforme, normal, exponencial, Beta, Dirichlet.
4. Esperanza, varianza, covarianza, correlación; normal multivariada.
5. Ley de los grandes números, teorema del límite central.
6. Estimación: máxima verosimilitud (MLE), máximo a posteriori (MAP), conjugadas (Beta–Bernoulli).
7. Inferencia: intervalos de confianza, bootstrap, pruebas de hipótesis, p-valores, pruebas A/B.
8. Monte Carlo: estimación de integrales, muestreo por rechazo, introducción a MCMC (Metropolis–Hastings).
9. Teoría de la información: entropía, entropía cruzada, KL, información mutua.

## Lecturas
- Blitzstein & Hwang, *Introduction to Probability* 🆓 — Caps. 1–7, 10.
- Deisenroth et al., *Mathematics for ML* — Cap. 6.
- Murphy, *Probabilistic ML: An Introduction* 🆓 — Caps. 2–4 y 6.
- Goodfellow et al. — Cap. 3.

## Ejercicios
| Archivo | Tema |
|---|---|
| ej01_bayes.py | Bayes y pruebas diagnósticas |
| ej02_distribuciones.py | PMF/PDF desde cero |
| ej03_monte_carlo.py | estimación de π e integrales |
| ej04_mle_map.py | MLE/MAP y conjugadas |
| ej05_bootstrap.py | intervalos por bootstrap |
| ej06_informacion.py | entropía, cross-entropy, KL, información mutua |
| ej07_metropolis.py | MCMC Metropolis–Hastings |

Aprobación ≥ 8/10.
