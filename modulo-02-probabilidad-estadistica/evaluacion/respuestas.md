# Respuestas — Módulo 02

1. $P(H|E) = P(E|H)P(H)/P(E)$: prior P(H), verosimilitud P(E|H), evidencia P(E), posterior P(H|E).
2. $0.99\cdot0.001/(0.99\cdot0.001+0.05\cdot0.999) \approx 0.019$. Con base muy baja, los falsos positivos superan a los verdaderos.
3. Si $P(A\cap B)=P(A)P(B)$. No: pueden volverse dependientes al condicionar (explaining away).
4. $P(x_1..x_n) = \prod P(x_t|x_{<t})$; un LLM predice cada token dado el contexto previo.
5. Poisson; exponencial.
6. $E[(X-\mu)^2] = E[X^2] - 2\mu E[X] + \mu^2 = E[X^2]-\mu^2$.
7. La media muestral estandarizada tiende a N(0,1); permite IC $\bar x\pm z\,s/\sqrt n$ sin conocer la distribución.
8. $\ell = k\log p + (n-k)\log(1-p)$; $\ell' = 0 \Rightarrow \hat p = k/n$.
9. Usa $\bar x$ en lugar de μ, subestimando la dispersión: $E[\hat\sigma^2] = \frac{n-1}{n}\sigma^2$.
10. Prior cuya posterior es de la misma familia: Beta–Bernoulli, Normal–Normal, Dirichlet–Categórica.
11. Gaussiana; Laplace.
12. Remuestrear con reemplazo B veces, calcular el estadístico en cada remuestra, usar percentiles 2.5 % y 97.5 %.
13. Probabilidad bajo H₀ de un resultado tan o más extremo. No es P(H₀ verdadera) ni el tamaño del efecto.
14. Por el TLC: la varianza del promedio es σ²/N, sin depender de la dimensión del espacio.
15. La razón de aceptación p(x')/p(x) cancela la constante.
16. $-0.9\log_2 0.9 - 0.1\log_2 0.1 \approx 0.469$ bits.
17. No es simétrica ni cumple la desigualdad triangular. VAEs, RLHF/PPO (penalización KL), destilación, inferencia variacional.
18. $H(p,q) = H(p) + KL(p\|q)$ y H(p) no depende de q.
19. $\exp$ de la entropía cruzada media por token; 10 ≈ el modelo duda como si eligiera uniformemente entre 10 tokens.
