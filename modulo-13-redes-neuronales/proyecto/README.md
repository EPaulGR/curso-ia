# Proyecto — Clasificador de dígitos en dos versiones: NumPy y PyTorch/MPS

Dataset: MNIST o Fashion-MNIST (`torchvision.datasets`).

## Requisitos
1. **Versión NumPy**: MLP de 2 capas ocultas con tu backprop (ej04 extendido), mini-batches, Adam propio, dropout y early stopping. Meta: ≥ 97 % en MNIST test.
2. **Versión PyTorch** en `device="mps"`, misma arquitectura. Compara exactitud y tiempo por época CPU vs MPS (usa `torch.mps.synchronize()`).
3. Experimentos: efecto de la inicialización, del learning rate (barrido logarítmico) y de dropout. Gráficas de curvas de entrenamiento/validación.
4. Informe con matriz de confusión y análisis de errores.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Backprop NumPy correcto (gradient check incluido) | 25 |
| Meta de exactitud alcanzada en ambas versiones | 15 |
| Benchmark CPU vs MPS bien medido | 15 |
| Experimentos de hiperparámetros con conclusiones | 20 |
| Visualizaciones y análisis de errores | 15 |
| Código limpio y reproducible | 10 |
