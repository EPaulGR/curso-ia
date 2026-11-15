# Respuestas — Módulo 20

1. RL aprende de recompensas por interacción y secuencial; supervisado, de etiquetas; no supervisado, de estructura sin etiquetas.
2. (S, A, P, R, γ); el futuro depende solo del estado actual, no de la historia.
3. Q*(s,a) = Σ_s' P(s'|s,a)[R + γ max_a' Q*(s',a')].
4. El operador de Bellman es una contracción en norma infinito (factor γ < 1); punto fijo único (Banach).
5. Descuento: γ=0 miope (solo recompensa inmediata); γ→1 valora el largo plazo, convergencia más lenta.
6. MC: sin sesgo, varianza alta; TD: con sesgo (bootstrap), varianza baja, aprende en línea.
7. SARSA usa Q(s',a') con a' de la política; Q-learning usa max_a' Q(s',a').
8. SARSA, porque su valor incluye la exploración ε que puede hacerlo caer al borde.
9. Aproximación de funciones + bootstrapping + off-policy → posible divergencia.
10. Replay: decorrelaciona y reutiliza datos; red objetivo: objetivos estables.
11. Sobreestimación por usar el mismo max para elegir y evaluar.
12. ∇E[f] = E[f ∇log p] porque ∇p = p ∇log p.
13. E[∇log π · b] = b ∇Σπ = b ∇1 = 0.
14. Que el cociente π_nuevo/π_viejo se aleje de [1−ε, 1+ε] → actualizaciones conservadoras.
15. SFT; modelo de recompensa con preferencias; optimización por RL (PPO) con KL.
16. Que la política explote el modelo de recompensa (reward hacking) y pierda fluidez.
17. Sin modelo de recompensa ni muestreo en el bucle; entrenamiento supervisado estable y barato.
18. MCTS guiado por una red de política (prioridades) y valor (evaluación); el resultado de la búsqueda sirve de objetivo para entrenar la red por self-play.
