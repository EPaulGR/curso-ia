# 25 papers clave (en orden de lectura sugerido)

| # | Paper | Año | Tema | Módulo |
|---|---|---|---|---|
| 1 | Turing — *Computing Machinery and Intelligence* | 1950 | Fundamentos | 04 |
| 2 | McCarthy et al. — *Proposal for the Dartmouth Summer Research Project on AI* | 1955 | Historia | 04 |
| 3 | Hart, Nilsson & Raphael — *A Formal Basis for the Heuristic Determination of Minimum Cost Paths* (A*) | 1968 | Búsqueda | 05 |
| 4 | Knuth & Moore — *An Analysis of Alpha-Beta Pruning* | 1975 | Adversarial | 06 |
| 5 | Kirkpatrick et al. — *Optimization by Simulated Annealing* | 1983 | Metaheurísticas | 07 |
| 6 | Deb et al. — *A Fast and Elitist Multiobjective GA: NSGA-II* | 2002 | Multiobjetivo | 07 |
| 7 | Pearl — *Probabilistic Reasoning in Intelligent Systems* (cap. 1–2) | 1988 | Bayes | 10 |
| 8 | Rumelhart, Hinton & Williams — *Learning Representations by Back-propagating Errors* | 1986 | Redes | 13 |
| 9 | Breiman — *Random Forests* | 2001 | ML clásico | 11 |
| 10 | LeCun et al. — *Gradient-Based Learning Applied to Document Recognition* | 1998 | CNN | 14 |
| 11 | Krizhevsky, Sutskever & Hinton — *ImageNet Classification with Deep CNNs* (AlexNet) | 2012 | Visión | 14 |
| 12 | Kingma & Ba — *Adam* | 2014 | Optimización | 13 |
| 13 | He et al. — *Deep Residual Learning* (ResNet) | 2015 | Visión | 14 |
| 14 | Hochreiter & Schmidhuber — *Long Short-Term Memory* | 1997 | Secuencias | 15 |
| 15 | Mikolov et al. — *Efficient Estimation of Word Representations* (word2vec) | 2013 | Embeddings | 15 |
| 16 | Bahdanau, Cho & Bengio — *Neural Machine Translation by Jointly Learning to Align and Translate* | 2014 | Atención | 16 |
| 17 | Vaswani et al. — *Attention Is All You Need* | 2017 | Transformers | 16 |
| 18 | Goodfellow et al. — *Generative Adversarial Nets* | 2014 | Generativos | 17 |
| 19 | Ho, Jain & Abbeel — *Denoising Diffusion Probabilistic Models* | 2020 | Difusión | 17 |
| 20 | Brown et al. — *Language Models are Few-Shot Learners* (GPT-3) | 2020 | LLMs | 18 |
| 21 | Hoffmann et al. — *Training Compute-Optimal LLMs* (Chinchilla) | 2022 | Escalamiento | 18 |
| 22 | Ouyang et al. — *Training LMs to Follow Instructions with Human Feedback* | 2022 | RLHF | 18, 20 |
| 23 | Lewis et al. — *Retrieval-Augmented Generation for Knowledge-Intensive NLP* | 2020 | RAG | 19 |
| 24 | Mnih et al. — *Human-level Control through Deep RL* (DQN) | 2015 | RL | 20 |
| 25 | Silver et al. — *Mastering the Game of Go without Human Knowledge* (AlphaGo Zero) | 2017 | RL + búsqueda | 06, 20 |

**Lecturas extra recomendadas:** Hu 2021 (LoRA), Rafailov 2023 (DPO), Bai 2022 (Constitutional AI), Kaplan 2020 (scaling laws), Radford 2021 (CLIP), Dosovitskiy 2020 (ViT), Yao 2022 (ReAct), Schulman 2017 (PPO), Wei 2022 (chain-of-thought), DeepSeek-AI 2025 (R1), Gu & Dao 2023 (Mamba).

Para cada paper llena una ficha (ver `teoria.md`, sección 1) y regístralo con tu `Biblioteca` del ejercicio 3.

---

# Ampliación 2023–2026 (lo más actual)

Leer después de los 25 anteriores. Acompañan a los módulos 18b y 19b.

| # | Paper | Año | Tema | Módulo |
|---|---|---|---|---|
| 26 | Su et al. — *RoFormer: Rotary Position Embedding* (RoPE) | 2021 | Arquitectura | 18b |
| 27 | Ainslie et al. — *GQA: Training Generalized Multi-Query Transformer Models* | 2023 | Arquitectura | 18b |
| 28 | Dao et al. — *FlashAttention* (1 y 2) | 2022–23 | Atención eficiente | 18b |
| 29 | Fedus et al. — *Switch Transformers* / Jiang et al. — *Mixtral of Experts* | 2021/24 | MoE | 18b |
| 30 | Gu & Dao — *Mamba: Linear-Time Sequence Modeling with Selective State Spaces* | 2023 | SSM | 18b |
| 31 | Lipman et al. — *Flow Matching for Generative Modeling* | 2023 | Generativos | 18b |
| 32 | Wei et al. — *Chain-of-Thought Prompting* / Wang et al. — *Self-Consistency* | 2022 | Razonamiento | 18b |
| 33 | Lightman et al. — *Let's Verify Step by Step* (process reward models) | 2023 | Razonamiento | 18b |
| 34 | Rafailov et al. — *Direct Preference Optimization* | 2023 | Alineamiento | 20, 18b |
| 35 | Shao et al. — *DeepSeekMath* (introduce GRPO) | 2024 | RLVR | 18b |
| 36 | DeepSeek-AI — *DeepSeek-R1: Incentivizing Reasoning via RL* | 2025 | RLVR / razonamiento | 18b |
| 37 | Snell et al. — *Scaling LLM Test-Time Compute Optimally* | 2024 | Test-time compute | 18b |
| 38 | Yue et al. — *Does RL Really Incentivize Reasoning Capacity Beyond the Base Model?* | 2025 | Debate RLVR | 18b |
| 39 | Leviathan et al. — *Fast Inference via Speculative Decoding* | 2023 | Inferencia | 19b |
| 40 | Kwon et al. — *Efficient Memory Management for LLM Serving with PagedAttention* (vLLM) | 2023 | Inferencia | 19b |
| 41 | Radford et al. — *CLIP* / Liu et al. — *Visual Instruction Tuning* (LLaVA) | 2021/23 | Multimodal | 19b |
| 42 | Yao et al. — *ReAct* / Schick et al. — *Toolformer* | 2022/23 | Agentes | 19, 19b |
| 43 | Jimenez et al. — *SWE-bench* | 2024 | Evaluación de agentes | 19b |
| 44 | Xie et al. — *OSWorld* / Jia et al. — *OSWorld-MCP* (ICLR 2026) | 2024/26 | Computer use + MCP | 19b |
| 45 | Greshake et al. — *Indirect Prompt Injection* | 2023 | Seguridad de agentes | 19b, 22 |

> El campo cambia cada pocos meses: cada trimestre revisa arXiv (cs.LG, cs.CL), las actas de NeurIPS/ICML/ICLR y los reportes técnicos de los laboratorios para actualizar esta lista.
