# Módulo 10 — Razonamiento bajo incertidumbre

**Duración estimada:** 3–4 semanas (≈ 40 h) · **Prerrequisitos:** 02 (probabilidad), 09
Cubre BUAP 2.1.1 (datos confiables, no confiables y variables en el tiempo) con herramientas formales.

## Objetivos
- Cuantificar incertidumbre con probabilidad y la regla de Bayes.
- Construir redes bayesianas e inferir de forma exacta y aproximada.
- Razonar en el tiempo con HMM y filtros de Kalman.
- Diseñar controladores con lógica difusa (Mamdani).
- Entender la teoría de la decisión (utilidad esperada) como puente a RL.

## Temario
1. Incertidumbre, probabilidad subjetiva, axiomas de Kolmogorov, regla de Bayes, independencia condicional, naive Bayes
2. Redes bayesianas: semántica, d-separación, manta de Markov, CPTs compactas (noisy-OR)
3. Inferencia exacta: enumeración, eliminación de variables, complejidad (poliárboles vs. general)
4. Inferencia aproximada: muestreo directo, rechazo, ponderación por verosimilitud, Gibbs/MCMC
5. Causalidad: redes causales, operador do, contrafactuales (Pearl)
6. Modelos temporales: Markov, filtrado, predicción, suavizado, Viterbi, HMM, Kalman, filtros de partículas, DBN
7. Decisiones: utilidad, redes de decisión, valor de la información
8. Lógica difusa: conjuntos difusos, operadores, inferencia Mamdani/Sugeno, defusificación
9. Programación probabilística (PyMC, NumPyro)

## Lecturas
- **AIMA 4ª ed., caps. 12, 13, 14, 15 y 16.1–16.6.**
- **Negnevitsky 3ª ed., caps. 3 (incertidumbre) y 4 (sistemas expertos difusos).**
- Murphy — *Probabilistic Machine Learning: An Introduction*, caps. 2–4 🆓.
- Pearl & Mackenzie — *The Book of Why* (divulgación sobre causalidad).
- Koller & Friedman — *Probabilistic Graphical Models* (referencia avanzada).

## Ejercicios
1. `ej01_bayes.py` — regla de Bayes, prueba médica, actualización secuencial
2. `ej02_red_bayesiana.py` — red de la alarma, conjunta, enumeración
3. `ej03_muestreo.py` — rechazo, ponderación por verosimilitud, Gibbs
4. `ej04_hmm.py` — filtrado, suavizado, Viterbi (paraguas)
5. `ej05_kalman.py` — filtro de Kalman
6. `ej06_logica_difusa.py` — pertenencias, Mamdani, problema de la propina

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Ensayo: "Probabilidad vs. lógica difusa" 10 %.
