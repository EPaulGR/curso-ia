# Módulo 18b — Arquitecturas modernas de LLM y modelos de razonamiento

> Actualización 2025–2026. Va **después del módulo 18** (LLMs) y antes del 19. Requiere 16 (Transformers), 17 (generativos) y 20 (RL) a nivel conceptual. Si aún no haces el 20, lee al menos MDP y gradiente de política antes de los ejercicios 08–09.

**Duración:** 4–5 semanas (12–15 h/semana).

## Objetivos
1. Explicar e implementar las piezas que separan un Transformer de 2017 de un LLM actual: RoPE, RMSNorm, SwiGLU, GQA/MQA, KV cache, atención eficiente, MoE.
2. Entender alternativas a la atención (modelos de espacio de estados / Mamba) y el problema del contexto largo.
3. Usar leyes de escalamiento (Chinchilla) para decidir tamaño de modelo y datos con un presupuesto de cómputo, y destilar modelos grandes en pequeños.
4. Dominar el paradigma de **razonamiento**: chain-of-thought, cómputo en inferencia (self-consistency, best-of-N, verificadores), RL con recompensas verificables (RLVR) y GRPO, process reward models.
5. Actualizar difusión con **flow matching / rectified flow**.
6. Entrenar en tu Mac (MLX o PyTorch-MPS) un mini modelo de razonamiento con GRPO.

## Temario
| # | Tema | Ejercicio |
|---|---|---|
| 1 | Codificación posicional rotatoria (RoPE), extensión de contexto (PI, NTK, YaRN) | ej01 |
| 2 | RMSNorm, pre-norm, SwiGLU | ej02 |
| 3 | MHA → MQA → GQA, KV cache y su costo de memoria; MLA (DeepSeek-V2) conceptual | ej03 |
| 4 | Atención eficiente: online softmax, FlashAttention 1/2/3, atención por ventana, sparse | ej04 |
| 5 | Mixture of Experts: router top-k, balanceo de carga, expertos compartidos | ej05 |
| 6 | Modelos de espacio de estados: S4, Mamba (scan selectivo), híbridos atención+SSM | ej06 |
| 7 | Leyes de escalamiento (Kaplan, Chinchilla), sobre-entrenamiento para inferencia, destilación | ej07 |
| 8 | Razonamiento en inferencia: CoT, self-consistency, best-of-N, pass@k, test-time compute | ej08 |
| 9 | RLVR y GRPO; process vs outcome reward models; el debate "¿RLVR expande o redistribuye?" | ej09 |
| 10 | Flow matching y rectified flow | ej10 |

## Lecturas
**Papers (en este orden):**
1. Su et al. (2021) *RoFormer: Enhanced Transformer with Rotary Position Embedding*.
2. Zhang & Sennrich (2019) *Root Mean Square Layer Normalization*; Shazeer (2020) *GLU Variants Improve Transformer*.
3. Ainslie et al. (2023) *GQA: Training Generalized Multi-Query Transformer Models*.
4. Dao et al. (2022) *FlashAttention*; Dao (2023) *FlashAttention-2*.
5. Fedus et al. (2021) *Switch Transformers*; Jiang et al. (2024) *Mixtral of Experts*; DeepSeek-AI (2024) *DeepSeek-V3 Technical Report*.
6. Gu & Dao (2023) *Mamba: Linear-Time Sequence Modeling with Selective State Spaces*.
7. Kaplan et al. (2020) *Scaling Laws for Neural Language Models*; Hoffmann et al. (2022) *Training Compute-Optimal LLMs* (Chinchilla).
8. Hinton et al. (2015) *Distilling the Knowledge in a Neural Network*.
9. Wei et al. (2022) *Chain-of-Thought Prompting*; Wang et al. (2022) *Self-Consistency*.
10. Lightman et al. (2023) *Let's Verify Step by Step* (PRM); Snell et al. (2024) *Scaling LLM Test-Time Compute Optimally*.
11. Shao et al. (2024) *DeepSeekMath* (introduce GRPO); DeepSeek-AI (2025) *DeepSeek-R1*.
12. Yue et al. (2025) *Does Reinforcement Learning Really Incentivize Reasoning Capacity in LLMs Beyond the Base Model?* — y las respuestas de 2026 (p. ej. ICLR 2026, métrica CoT-Pass@K).
13. Lipman et al. (2022) *Flow Matching for Generative Modeling*; Liu et al. (2022) *Rectified Flow*.

**Libros:** Raschka, *Build a LLM from Scratch*, cap. 3–4 y apéndices; Bishop & Bishop (2024) cap. 12 y 20; Prince *UDL* cap. 12 y 18.
**Videos:** Karpathy, *Let's reproduce GPT-2* y *Deep Dive into LLMs*.

## Evaluación
| Componente | Peso |
|---|---|
| Ejercicios (`pytest modulo-18b-arquitecturas-y-razonamiento`) | 30 % |
| Quiz (`evaluacion/quiz.md`) | 30 % |
| Proyecto GRPO (`proyecto/README.md`) | 30 % |
| Ensayo de 2 páginas: "¿RLVR crea razonamiento nuevo o solo lo hace más probable?", con ≥ 4 papers citados | 10 % |

Aprobado: ≥ 8/10.

> Este campo cambia cada pocos meses. Al empezar el módulo, busca los reportes técnicos más recientes de modelos abiertos (DeepSeek, Qwen, Llama, Mistral, Gemma) y compara su arquitectura con la tabla de `teoria.md`.
