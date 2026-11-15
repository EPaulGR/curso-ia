# Proyecto 22 — Auditoría completa de un modelo

Toma un modelo de un módulo previo (clasificador tabular, CNN o el LLM ajustado) y entrega un **informe de auditoría**:
1. **Model card** (Mitchell et al. 2019): uso previsto, datos, métricas, limitaciones.
2. Equidad: métricas por grupo (usa un dataset con atributo sensible, p. ej. Adult/Folktables) y una mitigación con su costo en exactitud.
3. Explicabilidad: SHAP global y 5 explicaciones locales; verifica una con Shapley exacto.
4. Robustez: curva exactitud vs. ε para FGSM/PGD; entrenamiento adversarial.
5. Calibración: diagrama de confiabilidad y ECE antes/después de escalado de temperatura.
6. Si es un LLM: red teaming con ≥ 50 casos, tasas de rechazo correcto y sobre-rechazo, 3 inyecciones indirectas.
7. Ensayo ético (1500 palabras) con referencias.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Model card | 10 |
| Equidad y mitigación | 20 |
| Explicabilidad | 15 |
| Robustez | 15 |
| Calibración / red teaming | 20 |
| Ensayo ético argumentado y citado | 20 |
