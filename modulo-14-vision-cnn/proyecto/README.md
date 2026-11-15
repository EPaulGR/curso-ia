# Proyecto — Clasificador de imágenes propio con transfer learning en MPS

Dataset sugerido: CIFAR-10, o mejor, un dataset propio (fotos tomadas por ti, ≥ 5 clases, ≥ 100 imágenes por clase).

## Requisitos
1. Línea base: CNN propia desde cero (≥ 3 bloques conv) en `device="mps"`.
2. ResNet-18 pequeña implementada con tu `BloqueResidual`, entrenada desde cero.
3. Transfer learning con un modelo de `torchvision` preentrenado; fine-tuning en dos fases.
4. Estudio de ablación de augmentation.
5. Grad-CAM sobre 10 ejemplos (aciertos y errores).
6. Bonus: exportar el mejor modelo a Core ML y probarlo en la Mac.

## Rúbrica (100 pts)
| Criterio | Pts |
|---|---|
| Tres modelos entrenados y comparados correctamente | 25 |
| Pipeline de datos y augmentation justificados | 15 |
| Ablación con conclusiones | 15 |
| Interpretabilidad (Grad-CAM) y análisis de errores | 20 |
| Reporte claro con métricas por clase | 15 |
| Reproducibilidad | 10 |
| Bonus Core ML | +10 |
