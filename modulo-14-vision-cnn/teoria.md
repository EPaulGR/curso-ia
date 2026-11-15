# Teoría — CNNs y visión

## 1. Motivación
Una imagen 224×224×3 tiene 150 528 entradas; una capa densa de 1000 neuronas ya serían 150 M de pesos. Las convoluciones explotan dos priors: **localidad** (los píxeles cercanos se relacionan) y **estacionariedad** (el mismo patrón puede aparecer en cualquier lugar → pesos compartidos). Resultado: equivarianza a traslaciones y muchísimos menos parámetros.

## 2. La operación
En deep learning "convolución" es en realidad correlación cruzada: y[i,j] = Σ_{c,u,v} W[c,u,v]·x[c, i·s+u, j·s+v] + b.
Tamaño de salida: ⌊(n + 2p − d(k−1) − 1)/s⌋ + 1. Parámetros: C_out·C_in·k² + C_out.
**im2col** convierte cada parche en columna; la convolución se vuelve un producto de matrices (GEMM), que es lo que aceleran GPU/Apple AMX/MPS.

## 3. Campo receptivo
Crece con la profundidad: r_L = r_{L−1} + (k_L − 1)·Π_{i<L} s_i. Tres conv 3×3 ven 7×7 con menos parámetros y más no linealidad que una 7×7 (idea de VGG).

## 4. Pooling y alternativas
Max pooling da invariancia local y reduce resolución. Hoy a menudo se usa stride 2 en convoluciones. Global average pooling sustituye capas densas finales. Conv 1×1 mezcla canales (bottlenecks, Inception). Depthwise-separable (MobileNet) factoriza: depthwise k×k + pointwise 1×1.

## 5. Arquitecturas
- **LeNet-5 (1998)**: dígitos. **AlexNet (2012)**: ReLU, dropout, GPU — arranque del deep learning moderno.
- **VGG**: pilas de 3×3. **Inception**: ramas paralelas.
- **ResNet (2016)**: y = F(x) + x. El atajo permite que el gradiente fluya y que la red aprenda residuos; hizo posible entrenar 100+ capas.
- **EfficientNet**: escalado compuesto de ancho/profundidad/resolución.
- **ViT**: parte la imagen en parches de 16×16 y usa un Transformer. Con muchos datos supera a las CNNs; ConvNeXt mostró que CNNs modernizadas compiten.

## 6. BatchNorm
Normaliza por canal con estadísticas del batch, luego γ·x̂ + β. En inferencia usa medias móviles (`model.eval()`!). Permite learning rates mayores.

## 7. Datos y transfer learning
Augmentation (volteos, recortes, color jitter, RandAugment, mixup) es regularización clave. Transfer learning: carga pesos de ImageNet, reemplaza la cabeza, entrena primero solo la cabeza y después afina todo con lr pequeño. Normaliza con la media/desviación del preentrenamiento.

## 8. Más allá de clasificar
- **Detección**: predecir cajas + clases. IoU mide solapamiento; NMS elimina duplicados. Dos etapas (Faster R-CNN) vs una etapa (YOLO) vs Transformers (DETR). Métrica: mAP.
- **Segmentación**: etiqueta por píxel. U-Net (encoder-decoder con skip connections), Mask R-CNN, SAM.
- **Multimodal**: CLIP aprende un espacio común imagen–texto con aprendizaje contrastivo.

## 9. En Mac
`torchvision` funciona con MPS. Usa `channels_last` y lotes grandes. Para desplegar en iPhone/Mac convierte con `coremltools` (módulo 21) y aprovecha el Neural Engine.
