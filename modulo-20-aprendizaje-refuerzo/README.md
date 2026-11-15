# Módulo 20 — Aprendizaje por refuerzo

**Duración:** 4–5 semanas (~60 h) · **Prerrequisitos:** 02, 13 (y 06 para MCTS)

## Objetivos
- Formalizar problemas de decisión secuencial como MDPs.
- Dominar programación dinámica, métodos Monte Carlo y diferencias temporales.
- Implementar DQN y gradientes de política; entender PPO.
- Conectar RL con el ajuste de LLMs (RLHF, DPO) y con la búsqueda adversarial (AlphaZero).

## Temario
1. Bandidos multibrazo: ε-greedy, UCB, Thompson.
2. MDPs, ecuaciones de Bellman, iteración de valor y de política.
3. Monte Carlo y TD(0), SARSA, Q-learning, TD(λ).
4. Aproximación de funciones: DQN, replay, red objetivo, Double/Dueling DQN.
5. Gradientes de política: REINFORCE, baseline, actor-crítico, A2C, PPO.
6. RL basado en modelo y planificación: Dyna, MCTS, AlphaZero, MuZero.
7. RL con retroalimentación humana: modelo de recompensa, PPO-KL, DPO, GRPO y RL con recompensas verificables en modelos de razonamiento.

## Lecturas
- **Sutton & Barto, 2ª ed.**: caps. 2–6, 9, 13 (núcleo); 8 y 16 (planificación, casos).
- Russell & Norvig: caps. 17 y 22.
- Papers: Mnih 2015 (DQN), Schulman 2017 (PPO), Silver 2017 (AlphaZero), Christiano 2017 (preferencias humanas), Ouyang 2022 (InstructGPT), Rafailov 2023 (DPO), DeepSeek-R1 2025 (GRPO).
- Curso: David Silver (UCL), OpenAI Spinning Up.

## Ejercicios
| # | Archivo | Tema |
|---|---|---|
| 1 | ej01_mdp.py | GridWorld + iteración de valor |
| 2 | ej02_iteracion_politica.py | Iteración de política |
| 3 | ej03_qlearning_sarsa.py | Q-learning y SARSA |
| 4 | ej04_dqn_componentes.py | Replay, objetivos DQN/Double DQN |
| 5 | ej05_reinforce.py | REINFORCE con baseline |
| 6 | ej06_dpo.py | Bradley-Terry y DPO |

Instala `gymnasium` para los retos (CartPole, LunarLander) con PyTorch en MPS.

## Criterios
Tests (30 %), quiz (30 %), proyecto (30 %), comparación escrita Q-learning vs. SARSA en "cliff walking" (10 %).
