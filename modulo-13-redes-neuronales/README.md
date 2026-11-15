# Módulo 13 — Redes neuronales desde cero y PyTorch en Apple Silicon

**Fase 3 · Machine Learning** · Duración: 4 semanas (~50 h) · Prerrequisitos: 01 (cálculo, regla de la cadena), 02, 11

## Objetivos
- Entender una red neuronal como composición de funciones diferenciables.
- Derivar e implementar **backpropagation a mano en NumPy** y verificarlo con gradiente numérico.
- Construir un mini motor de **autograd** (como micrograd).
- Implementar optimizadores (Momentum, Adam) y regularización (dropout, L2, early stopping).
- Migrar a **PyTorch** y entrenar en la GPU de la Mac con `device="mps"`.

## Temario
1. Del perceptrón (Rosenblatt 1958) al MLP; el problema XOR (Minsky & Papert).
2. Activaciones: sigmoide, tanh, ReLU, GELU; softmax; saturación.
3. Funciones de pérdida: MSE, entropía cruzada, relación con máxima verosimilitud.
4. Backpropagation: grafo computacional, regla de la cadena en forma matricial.
5. Inicialización (Xavier, He) y el problema del gradiente que desaparece/explota.
6. Optimización: SGD, mini-batch, momentum, RMSProp, Adam, AdamW; schedules de learning rate.
7. Regularización: L2/weight decay, dropout, early stopping, data augmentation.
8. Normalización: BatchNorm, LayerNorm.
9. PyTorch: tensores, autograd, `nn.Module`, `DataLoader`, ciclo de entrenamiento, MPS.
10. Teorema de aproximación universal y por qué la profundidad ayuda.

## Lecturas
- Prince, *Understanding Deep Learning*, cap. 3–9.
- Goodfellow et al., *Deep Learning*, cap. 6, 7 y 8.
- Bishop & Bishop (2024), cap. 6–8.
- Russell & Norvig, AIMA 4ª ed., cap. 21 (Deep Learning).
- Negnevitsky, cap. 6 (Artificial neural networks) — perspectiva del temario BUAP.
- Video: Karpathy, *The spelled-out intro to neural networks and backpropagation: building micrograd*.

## Ejercicios
| # | Archivo | Tema |
|---|---|---|
| 01 | ej01_perceptron.py | Perceptrón |
| 02 | ej02_activaciones.py | Activaciones y derivadas, softmax estable |
| 03 | ej03_gradiente_numerico.py | Gradient checking |
| 04 | ej04_mlp_numpy.py | **MLP con backprop manual** (núcleo del módulo) |
| 05 | ej05_optimizadores.py | Momentum y Adam en Rosenbrock |
| 06 | ej06_autograd.py | Mini autograd escalar |
| 07 | ej07_pytorch_mps.py | MLP en PyTorch sobre MPS |
| 08 | ej08_regularizacion.py | Dropout, L2, early stopping |

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Lecturas 10 %. Aprobado ≥ 8.
