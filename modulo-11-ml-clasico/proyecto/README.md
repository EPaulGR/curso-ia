# Proyecto 11 — Proyecto de ML de punta a punta

## Descripción
Resuelve un problema real de datos tabulares con impacto social (eje transversal BUAP). Sugerencias: predicción de deserción escolar, calidad del aire en Puebla (datos SINAICA), riesgo de diabetes (datos abiertos de salud), precios de vivienda en México (INEGI/portales inmobiliarios).

## Requisitos
1. **EDA** documentado en notebook: distribuciones, faltantes, correlaciones, desbalance.
2. **Línea base** simple (media, regresión logística/lineal).
3. Al menos **5 modelos**: 2 propios del módulo (desde cero) y 3 de scikit-learn/XGBoost/LightGBM.
4. Todo el preprocesamiento en `Pipeline`/`ColumnTransformer`; validación cruzada estratificada; búsqueda de hiperparámetros (GridSearch o Optuna).
5. Conjunto de prueba reservado y evaluado una sola vez al final.
6. Análisis de errores e interpretabilidad (permutación + SHAP).
7. Reflexión ética: sesgos en los datos, a quién afecta un error.
8. Script reproducible `entrenar.py` y modelo guardado con `joblib`.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| EDA y entendimiento del problema | 15 |
| Metodología sin fugas y validación correcta | 25 |
| Modelos y ajuste de hiperparámetros | 20 |
| Interpretabilidad y análisis de errores | 15 |
| Ética y comunicación (informe 5–8 págs.) | 15 |
| Reproducibilidad | 10 |
