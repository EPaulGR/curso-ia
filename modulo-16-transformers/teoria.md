# Teoría — Transformers

## 1. La idea
Las RNN procesan secuencialmente (no paralelizable) y olvidan dependencias lejanas. El Transformer reemplaza la recurrencia con **atención**: cada token mira directamente a todos los demás. Todo se paraleliza en GPU → se puede escalar a billones de tokens.

## 2. Atención escalada
Attention(Q,K,V) = softmax(QKᵀ / √d_k) V.
- Q (consultas): "qué busco"; K (claves): "qué ofrezco"; V (valores): "qué entrego".
- ¿Por qué √d_k? Si q,k tienen componentes de varianza 1, q·k tiene varianza d_k; sin escalar, el softmax se satura y los gradientes desaparecen.
- **Máscara causal**: en modelos de lenguaje el token i solo ve j ≤ i (se pone −∞ antes del softmax). **Padding**: no atender a relleno.
- Costo O(T²·d) en tiempo y O(T²) en memoria: el límite del contexto largo.

## 3. Multi-cabeza
h cabezas con d_k = d/h; cada una aprende un tipo de relación (sintaxis, correferencia, posición). Se concatenan y proyectan con W_O. Mismo costo que una cabeza de dimensión d.

## 4. Posición
La atención es invariante a permutaciones, así que hay que inyectar orden:
- Sinusoidal: PE(pos,2i)=sin(pos/10000^{2i/d}), PE(pos,2i+1)=cos(·). Las posiciones relativas son transformaciones lineales.
- Aprendida (GPT-2).
- **RoPE** (Llama, Qwen): rota q y k según la posición; el producto punto depende solo de la distancia relativa. Estándar actual.

## 5. El bloque
Pre-norm (GPT-2 en adelante):
x ← x + MHA(LN(x)); x ← x + MLP(LN(x)).
El MLP (4× más ancho, GELU o SwiGLU) es donde está la mayoría de parámetros y se cree que guarda "conocimiento". Los residuales forman un "flujo residual" que cada capa lee y modifica. Pre-norm entrena más estable que post-norm. RMSNorm es más barata que LayerNorm.

## 6. GPT
Embedding de tokens + posición → N bloques → LN final → proyección al vocabulario (a menudo con pesos atados al embedding). Entrenamiento: predecir el siguiente token con entropía cruzada en todas las posiciones a la vez (teacher forcing). Pérdida inicial esperada ≈ ln V.
Número de parámetros aproximado: 12·N·d² (sin embeddings). Costo de entrenamiento ≈ 6·P·D FLOPs (P parámetros, D tokens).

## 7. Decodificación
- Greedy: argmax; repetitivo.
- Beam search: bueno en traducción, malo en texto abierto.
- Temperatura t: softmax(z/t); t→0 greedy, t grande uniforme.
- Top-k: solo los k más probables. Top-p (nucleus): el conjunto mínimo con masa ≥ p; se adapta a la confianza del modelo.

## 8. Familias
- **Encoder (BERT)**: atención bidireccional, preentrenado con Masked LM; ideal para clasificar/embeddings.
- **Decoder (GPT, Llama, Claude)**: causal; generación.
- **Encoder–decoder (T5, Whisper)**: atención cruzada; traducción, voz.
**Leyes de escalamiento**: la pérdida baja como ley de potencias con parámetros, datos y cómputo. Chinchilla: ≈ 20 tokens por parámetro para un óptimo de cómputo.

## 9. Eficiencia en inferencia
- **KV-cache**: guardar K y V de los tokens previos; cada nuevo token cuesta O(T) en vez de O(T²). La memoria del KV-cache domina con contextos largos — aquí la memoria unificada de la Mac Studio es una gran ventaja.
- GQA/MQA: varias cabezas de consulta comparten K/V.
- FlashAttention: atención exacta por bloques sin materializar T×T (en Mac: `scaled_dot_product_attention` de PyTorch y `mx.fast.scaled_dot_product_attention` de MLX).
