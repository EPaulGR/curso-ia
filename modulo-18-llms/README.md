# Módulo 18 — Modelos de Lenguaje Grandes (LLMs)

**Duración:** 4–5 semanas (~60 h) · **Prerrequisitos:** módulos 13, 15, 16

## Objetivos
- Entender el ciclo de vida de un LLM: datos → tokenización → preentrenamiento → ajuste (SFT, RLHF/DPO) → cuantización → inferencia.
- Implementar desde cero: BPE, muestreo, cuantización y LoRA.
- Ajustar (fine-tuning LoRA) un modelo real en tu Mac con **MLX** y servirlo con **Ollama**.
- Estimar memoria y decidir qué modelos caben en tu hardware (M5 Ultra).

## Temario
1. Leyes de escalamiento (Kaplan 2020, Chinchilla/Hoffmann 2022).
2. Tokenización: BPE, WordPiece, SentencePiece, tokens a nivel byte.
3. Preentrenamiento: objetivo autoregresivo, perplejidad, mezcla de datos.
4. Arquitecturas actuales: RoPE, RMSNorm, SwiGLU, GQA, Mixture of Experts.
5. Ajuste: SFT, instrucción, RLHF, DPO; PEFT (LoRA, QLoRA).
6. Inferencia: KV cache, muestreo, decodificación especulativa, cuantización (int8, 4-bit, GGUF, MLX).
7. Práctica en Apple Silicon: mlx-lm, llama.cpp, Ollama.

## Lecturas
- Raschka, *Build a LLM from Scratch*: caps. 2–7 (todo el libro).
- Jurafsky & Martin, *SLP3*: cap. 3 (n-gramas), cap. 10–12 (LLMs, ajuste).
- Russell & Norvig, *AIMA* 4ª ed.: cap. 24–25.
- Papers: Vaswani 2017 (*Attention is All You Need*), Radford 2019 (GPT-2), Brown 2020 (GPT-3), Hoffmann 2022 (Chinchilla), Hu 2021 (LoRA), Dettmers 2023 (QLoRA), Touvron 2023 (Llama 2), Ouyang 2022 (InstructGPT), Rafailov 2023 (DPO).
- Video: Karpathy, *Let's build GPT* y *Let's build the GPT Tokenizer*.

## Ejercicios
| # | Archivo | Tema |
|---|---|---|
| 1 | ej01_bpe.py | Tokenizador BPE |
| 2 | ej02_muestreo.py | Temperatura, top-k, top-p |
| 3 | ej03_cuantizacion.py | int8 y 4-bit por grupos |
| 4 | ej04_lora.py | LoRA con gradientes a mano |
| 5 | ej05_memoria.py | Calculadora de memoria |
| 6 | ej06_bigramas.py | Modelo de bigramas y perplejidad |
| 7 | guia-mlx-ollama.md | Fine-tuning real con mlx-lm (práctica guiada) |

```bash
pytest modulo-18-llms
```

## Criterios de aprobación
Tests en verde (30 %), quiz ≥ 8 (30 %), proyecto (30 %), resumen escrito de LoRA y Chinchilla (10 %).
