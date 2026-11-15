# Módulo 16 — Atención y Transformers: construye tu propio mini-GPT

**Fase 4 · Deep Learning** · Duración: 5 semanas (~60 h) · Prerrequisitos: 13, 15

## Objetivos
- Derivar e implementar la atención de producto punto escalado, máscaras y multi-cabeza.
- Entender cada pieza del Transformer: codificación posicional, LayerNorm/RMSNorm, MLP, residuales, pre-norm.
- **Implementar y entrenar un mini-GPT a nivel de caracteres** en la GPU de la Mac.
- Conocer decodificación (temperatura, top-k, top-p) y las variantes encoder (BERT), decoder (GPT) y encoder–decoder (T5).

## Temario
1. De la atención de Bahdanau a "Attention Is All You Need".
2. Atención Q/K/V, escalado por √d, máscaras causal y de padding, complejidad O(T²).
3. Multi-cabeza; autoatención vs atención cruzada.
4. Posición: sinusoidal, aprendida, RoPE, ALiBi.
5. Bloque Transformer: pre-norm vs post-norm, MLP/GELU/SwiGLU, residuales.
6. Modelado de lenguaje autoregresivo, teacher forcing, pesos atados.
7. Decodificación: greedy, beam search, temperatura, top-k, top-p.
8. BERT (MLM), GPT (causal), T5; leyes de escalamiento (Kaplan, Chinchilla).
9. Eficiencia: KV-cache, FlashAttention, atención agrupada (GQA), contexto largo.

## Lecturas
- Vaswani et al. (2017), *Attention Is All You Need* — léelo completo.
- Prince, *UDL*, cap. 12 (Transformers).
- Bishop & Bishop (2024), cap. 12.
- Jurafsky & Martin 3ª ed., cap. 9–10 (Transformers y LLMs).
- Raschka, *Build a Large Language Model (From Scratch)*, cap. 2–5.
- Jay Alammar, *The Illustrated Transformer*; Karpathy, *Let's build GPT: from scratch, in code, spelled out*.
- Papers extra: Devlin et al. 2019 (BERT); Radford et al. 2019 (GPT-2); Su et al. 2021 (RoPE); Hoffmann et al. 2022 (Chinchilla).

## Ejercicios
| # | Archivo | Tema |
|---|---|---|
| 01 | ej01_atencion.py | Atención escalada (validada contra PyTorch) |
| 02 | ej02_mascara_causal.py | Máscaras causal y padding |
| 03 | ej03_posicional.py | Codificación sinusoidal |
| 04 | ej04_layernorm.py | LayerNorm y RMSNorm |
| 05 | ej05_multihead.py | Multi-cabeza causal |
| 06 | ej06_bloque.py | Bloque Transformer pre-norm |
| 07 | ej07_mini_gpt.py | **Mini-GPT de caracteres** |
| 08 | ej08_muestreo.py | Temperatura, top-k, top-p |

> ej06 y ej07 importan tus archivos anteriores (ej05, ej06) de la misma carpeta: complétalos en orden.

## Evaluación
Ejercicios 30 % · [Quiz](evaluacion/quiz.md) 30 % · [Proyecto](proyecto/README.md) 30 % · Lecturas 10 %. Aprobado ≥ 8.
