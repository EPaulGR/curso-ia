# Módulo 01 — Matemáticas: álgebra lineal, cálculo y optimización

**Duración:** 5–6 semanas (60–80 h) · **Fase 0** · Requisito para ML/DL (módulos 11+)

## Objetivos
- Pensar en vectores y matrices como transformaciones geométricas.
- Calcular y entender descomposiciones (eigen, SVD) y su uso en IA (PCA, compresión, embeddings).
- Derivar gradientes de funciones vectoriales y aplicar la regla de la cadena (base de backpropagation).
- Implementar descenso de gradiente y sus variantes (momentum, Adam) y entender convexidad.

## Temario
1. Vectores, normas (L1, L2, L∞), producto punto, ángulo, proyecciones.
2. Matrices: producto, transpuesta, inversa, rango, determinante, sistemas lineales (eliminación gaussiana).
3. Espacios vectoriales, bases, independencia lineal, ortogonalidad, Gram-Schmidt.
4. Valores y vectores propios, matrices simétricas, definida positiva.
5. SVD y aproximación de rango bajo.
6. Cálculo diferencial: derivadas, derivadas parciales, gradiente, jacobiano, hessiano.
7. Regla de la cadena multivariable y grafos computacionales.
8. Optimización: condiciones de óptimo, convexidad, descenso de gradiente, tasa de aprendizaje, momentum, Adam, método de Newton.
9. Multiplicadores de Lagrange (intro a SVM).

## Lecturas
- Deisenroth, Faisal & Ong, *Mathematics for Machine Learning* 🆓 — Caps. 2 (álgebra lineal), 3 (geometría analítica), 4 (descomposiciones), 5 (cálculo vectorial), 7 (optimización continua).
- Strang, *Introduction to Linear Algebra* — Caps. 1–7 (o videos MIT 18.06).
- 3Blue1Brown, *Essence of Linear Algebra* y *Essence of Calculus* (YouTube).
- Goodfellow et al., *Deep Learning* 🆓 — Caps. 2 y 4.

## Ejercicios
| Archivo | Tema |
|---|---|
| ej01_vectores.py | normas, ángulos, proyecciones |
| ej02_eliminacion_gauss.py | resolver Ax=b desde cero |
| ej03_gram_schmidt.py | ortonormalización / QR |
| ej04_metodo_potencia.py | eigenvalor dominante |
| ej05_svd_compresion.py | aproximación de rango bajo |
| ej06_gradiente_numerico.py | diferencias finitas y verificación de gradientes |
| ej07_descenso_gradiente.py | GD, momentum y Adam |
| ej08_regresion_minimos_cuadrados.py | ecuaciones normales vs GD |

## Evaluación
Tests `pytest modulo-01-matematicas` · quiz · proyecto. Aprobación ≥ 8/10.
