# Teoría — Probabilidad, estadística e información

## 1. Fundamentos
- $P(A\mid B) = P(A\cap B)/P(B)$.
- Regla de la cadena: $P(A,B,C) = P(A)P(B\mid A)P(C\mid A,B)$. Un LLM modela exactamente esto: $P(w_1..w_n) = \prod_t P(w_t\mid w_{<t})$.
- Probabilidad total: $P(B) = \sum_i P(B\mid A_i)P(A_i)$.
- **Bayes:** $P(H\mid E) = \frac{P(E\mid H)P(H)}{P(E)}$ — posterior ∝ verosimilitud × prior.

*Ejemplo:* enfermedad con prevalencia 1 %, prueba con sensibilidad 99 % y especificidad 95 %. $P(\text{enf}\mid +) = \frac{0.99\cdot0.01}{0.99\cdot0.01 + 0.05\cdot0.99} \approx 0.167$. La tasa base domina.

## 2. Distribuciones
| Distribución | PMF/PDF | Media | Varianza |
|---|---|---|---|
| Bernoulli(p) | $p^x(1-p)^{1-x}$ | p | p(1−p) |
| Binomial(n,p) | $\binom{n}{k}p^k(1-p)^{n-k}$ | np | np(1−p) |
| Poisson(λ) | $e^{-\lambda}\lambda^k/k!$ | λ | λ |
| Normal(μ,σ²) | $\frac{1}{\sqrt{2\pi}\sigma}e^{-(x-\mu)^2/2\sigma^2}$ | μ | σ² |
| Exponencial(λ) | $\lambda e^{-\lambda x}$ | 1/λ | 1/λ² |
| Beta(α,β) | $\propto x^{\alpha-1}(1-x)^{\beta-1}$ | α/(α+β) | — |

## 3. Esperanza y varianza
$E[aX+b] = aE[X]+b$; $\text{Var}(X) = E[X^2]-E[X]^2$; $\text{Cov}(X,Y) = E[XY]-E[X]E[Y]$.

## 4. Teoremas límite
- LGN: $\bar X_n \to \mu$.
- TLC: $\sqrt{n}(\bar X_n-\mu)/\sigma \to N(0,1)$. Fundamenta los intervalos de confianza $\bar x \pm 1.96\, s/\sqrt n$.

## 5. Estimación
- **MLE:** $\hat\theta = \arg\max_\theta \sum_i \log p(x_i\mid\theta)$. Para Bernoulli: $\hat p = \bar x$. Para normal: $\hat\mu = \bar x$, $\hat\sigma^2 = \frac1n\sum(x_i-\bar x)^2$.
- **MAP:** $\arg\max_\theta \log p(x\mid\theta) + \log p(\theta)$. Con prior Beta(α,β) y k éxitos en n: $\hat p_{MAP} = \frac{k+\alpha-1}{n+\alpha+\beta-2}$; posterior Beta(α+k, β+n−k) (conjugada).
- Regularización L2 = MAP con prior gaussiano; L1 = prior de Laplace.

## 6. Inferencia y bootstrap
Bootstrap: remuestrear con reemplazo B veces, calcular el estadístico, tomar percentiles 2.5 y 97.5 → IC al 95 %. Prueba de hipótesis: p-valor = probabilidad, bajo H₀, de un resultado al menos tan extremo.

## 7. Monte Carlo
$E[f(X)] \approx \frac1N\sum f(x_i)$, error $O(1/\sqrt N)$. π ≈ 4 × fracción de puntos en el círculo unitario.
**Metropolis–Hastings** (propuesta simétrica): proponer $x' = x + \epsilon$; aceptar con probabilidad $\min(1, p(x')/p(x))$. Solo requiere $p$ hasta una constante.

## 8. Teoría de la información
- Entropía: $H(p) = -\sum p_i\log p_i$ (bits si log₂). Máxima con la uniforme.
- Entropía cruzada: $H(p,q) = -\sum p_i\log q_i$ — **la pérdida de clasificación y de los LLMs**.
- KL: $D_{KL}(p\|q) = \sum p_i\log\frac{p_i}{q_i} = H(p,q)-H(p) \ge 0$, no simétrica. Aparece en VAEs, RLHF (penalización KL), destilación.
- Información mutua: $I(X;Y) = H(X)+H(Y)-H(X,Y)$. Usada en árboles de decisión (ganancia de información).
- Perplejidad de un modelo de lenguaje: $2^{H}$ (o $e^{H}$ con log natural).
