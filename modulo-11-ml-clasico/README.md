# Módulo 11 — Machine Learning clásico (aprendizaje supervisado)

**Duración estimada:** 5 semanas (≈ 60 h) · **Prerrequisitos:** 01, 02, 10
Corresponde a la materia consecuente BUAP "Aprendizaje Automático y Heurísticas".

## Objetivos
- Entender el aprendizaje como optimización de una pérdida con generalización.
- Implementar desde cero regresión lineal/logística, kNN, Naive Bayes, árboles, AdaBoost y SVM lineal.
- Dominar validación cruzada, métricas, sesgo–varianza y regularización.
- Usar scikit-learn de forma profesional (pipelines, búsqueda de hiperparámetros) y gradient boosting.

## Temario
1. Formulación: tareas, datos i.i.d., pérdida, riesgo empírico, generalización
2. Regresión lineal: mínimos cuadrados, ecuación normal, descenso de gradiente, regularización (ridge, lasso, elastic net)
3. Clasificación: regresión logística, softmax, kNN, Naive Bayes, análisis discriminante
4. Evaluación: train/val/test, k-fold, métricas (precision, recall, F1, ROC-AUC, PR-AUC, MAE, RMSE), calibración
5. Sesgo–varianza, sobreajuste, curvas de aprendizaje, teoría PAC y dimensión VC (intro)
6. Árboles de decisión (CART, ID3), poda
7. Ensambles: bagging, random forest, AdaBoost, gradient boosting, XGBoost/LightGBM/CatBoost
8. SVM: margen máximo, pérdida bisagra, dual, kernels (RBF, polinomial)
9. Ingeniería de características, datos faltantes, desbalance, fuga de datos (*data leakage*)
10. Interpretabilidad básica: importancia por permutación, SHAP

## Lecturas
- **Géron, *Hands-On ML* 3ª ed., caps. 1–7.**
- **James et al., *An Introduction to Statistical Learning with Python* 🆓: caps. 2–6, 8, 9.**
- AIMA 4ª ed., cap. 19 (Learning from Examples).
- Hastie, Tibshirani & Friedman, *Elements of Statistical Learning* 🆓: caps. 3, 4, 7, 9, 10, 15 (profundización).
- Negnevitsky 3ª ed., cap. 6 (redes neuronales artificiales, como preámbulo al módulo 13).

## Ejercicios
1. `ej01_regresion_lineal.py` — ecuación normal, ridge, descenso de gradiente, R²
2. `ej02_regresion_logistica.py` — sigmoide estable, entropía cruzada, entrenamiento
3. `ej03_knn_naive_bayes.py` — kNN vectorizado, Naive Bayes gaussiano
4. `ej04_arbol_decision.py` — Gini, entropía, CART recursivo
5. `ej05_metricas_validacion.py` — confusión, P/R/F1, AUC, k-fold
6. `ej06_ensembles.py` — AdaBoost con tocones; RF y GBoost en scikit-learn
7. `ej07_svm_pipeline.py` — Pegasos; Pipeline + GridSearchCV con SVC RBF

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Participación en una competencia de Kaggle (reporte de lo aprendido) 10 %.
