# Módulo 14 — Redes convolucionales y visión por computadora

**Fase 4 · Deep Learning** · Duración: 4 semanas (~45 h) · Prerrequisitos: 13

## Objetivos
- Implementar convolución, pooling e im2col desde cero y entender su costo.
- Dominar la aritmética de dimensiones, parámetros y campo receptivo.
- Entrenar CNNs en PyTorch/MPS, usar augmentation y transfer learning.
- Conocer arquitecturas clave (LeNet → AlexNet → VGG → ResNet → EfficientNet → ViT) y tareas (clasificación, detección, segmentación).

## Temario
1. Por qué convoluciones: conectividad local, pesos compartidos, equivarianza a traslación.
2. Convolución 2D, stride, padding, dilatación, canales; im2col y GEMM.
3. Pooling, convoluciones 1×1, depthwise-separable.
4. Arquitecturas históricas y conexiones residuales; BatchNorm.
5. Augmentation, regularización, mixup/cutmix.
6. Transfer learning y fine-tuning con `torchvision.models`.
7. Detección (IoU, NMS, anchors, YOLO/DETR) y segmentación (U-Net).
8. Vision Transformers (ViT) y modelos fundacionales visuales (CLIP, SAM) — puente al módulo 16.
9. Visión en Apple: Core ML, Vision framework.

## Lecturas
- Prince, *UDL*, cap. 10 (Convolutional networks) y 11 (Residual networks).
- Goodfellow et al., cap. 9.
- Bishop & Bishop (2024), cap. 10.
- Géron, cap. 14.
- Apuntes de Stanford CS231n (cs231n.github.io): módulos de ConvNets.
- Papers: LeCun et al. 1998 (LeNet); Krizhevsky et al. 2012 (AlexNet); He et al. 2016 (ResNet); Dosovitskiy et al. 2021 (ViT).

## Ejercicios
| # | Archivo | Tema |
|---|---|---|
| 01 | ej01_convolucion.py | Convolución 2D y filtro de Sobel |
| 02 | ej02_pooling.py | Max/avg pooling |
| 03 | ej03_dimensiones.py | Tamaños, parámetros, campo receptivo |
| 04 | ej04_im2col.py | Convolución multicanal vectorizada (validada contra PyTorch) |
| 05 | ej05_cnn_torch.py | CNN tipo LeNet en MPS |
| 06 | ej06_aumentacion.py | Data augmentation |
| 07 | ej07_bloque_residual.py | Bloque ResNet |
| 08 | ej08_deteccion.py | IoU y NMS |

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Lecturas 10 %. Aprobado ≥ 8.
