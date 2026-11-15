# Proyecto 01 — Compresión de imágenes con SVD y visualizador de optimizadores

**Parte A – SVD (50 %)**
1. Carga una imagen en escala de grises como matriz (matplotlib `imread`).
2. Comprime con k = 5, 20, 50, 100; muestra las imágenes y la razón de compresión $k(m+n+1)/(mn)$.
3. Grafica la energía retenida vs k.

**Parte B – Optimizadores (50 %)**
1. Con tus implementaciones (ej07), visualiza en un contour plot las trayectorias de GD, momentum y Adam sobre Rosenbrock y sobre una cuadrática mal condicionada.
2. Experimenta con 3 tasas de aprendizaje; documenta divergencia/convergencia.
3. Implementa además el método de Newton y compáralo.

## Rúbrica (10 pts)
| Criterio | Pts |
|---|---|
| SVD correcta y análisis de compresión | 3 |
| Visualización de trayectorias clara | 3 |
| Newton implementado y comparado | 2 |
| Conclusiones con fundamento matemático | 2 |
