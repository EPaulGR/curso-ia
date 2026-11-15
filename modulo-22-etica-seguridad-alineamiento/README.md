# Módulo 22 — Ética, seguridad, interpretabilidad y alineamiento

**Duración:** 3 semanas (~40 h) · **Prerrequisitos:** 11, 13, 18
Corresponde al eje transversal BUAP de *Formación Humana y Social* y *ensayos éticos*.

## Objetivos
- Medir y mitigar sesgos de modelos con métricas de equidad formales.
- Explicar predicciones (Shapley/SHAP, saliencia, gradientes integrados) e introducirte a la interpretabilidad mecanicista.
- Atacar y defender modelos (ejemplos adversariales, inyección de prompts, red teaming).
- Entender el problema del alineamiento y las técnicas actuales de seguridad en LLMs.
- Conocer la regulación (EU AI Act, NIST AI RMF, contexto mexicano).

## Temario
1. Ética aplicada: daños, privacidad, consentimiento, impacto ambiental del cómputo.
2. Equidad: paridad demográfica, igualdad de oportunidades, odds igualados; teoremas de imposibilidad.
3. Interpretabilidad: LIME, SHAP, saliencia, IG, sondas lineales, circuitos, autoencoders dispersos.
4. Robustez: FGSM, PGD, entrenamiento adversarial; envenenamiento de datos.
5. Seguridad de LLMs: jailbreaks, inyección de prompts directa e indirecta, exfiltración en agentes.
6. Calibración e incertidumbre: ECE, escalado de temperatura, conformal prediction.
7. Alineamiento: especificación de objetivos, reward hacking, RLHF, Constitutional AI, supervisión escalable, evaluaciones de capacidades peligrosas.
8. Gobernanza y regulación.

## Lecturas
- Barocas, Hardt & Narayanan, *Fairness and Machine Learning* 🆓 caps. 1–3.
- Molnar, *Interpretable Machine Learning* 🆓 caps. 5–10.
- Brian Christian, *The Alignment Problem*; Stuart Russell, *Human Compatible*; Boden, *Inteligencia artificial* (cap. final).
- Russell & Norvig, cap. 27 (filosofía, ética y seguridad de la IA).
- Papers: Goodfellow 2015 (FGSM), Madry 2018 (PGD), Lundberg 2017 (SHAP), Sundararajan 2017 (IG), Guo 2017 (calibración), Bai 2022 (Constitutional AI), Amodei 2016 (*Concrete Problems in AI Safety*), Greshake 2023 (inyección indirecta), Anthropic 2024 (*Scaling Monosemanticity*).

## Ejercicios
| # | Archivo | Tema |
|---|---|---|
| 1 | ej01_equidad.py | Métricas de equidad |
| 2 | ej02_shap.py | Shapley exacto |
| 3 | ej03_fgsm.py | FGSM y entrenamiento adversarial |
| 4 | ej04_saliencia.py | Saliencia y gradientes integrados |
| 5 | ej05_red_teaming.py | Arnés de red teaming |
| 6 | ej06_calibracion.py | ECE y escalado de temperatura |

## Criterios
Tests (30 %), quiz (30 %), proyecto (30 %), **ensayo ético** de 1500 palabras con citas (10 %).
