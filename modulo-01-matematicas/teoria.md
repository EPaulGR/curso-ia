# Teoría — Matemáticas para IA

## 1. Vectores
- Norma Lp: $\|x\|_p = (\sum_i |x_i|^p)^{1/p}$. L2 = euclidiana, L1 = Manhattan (heurística en búsqueda en cuadrículas), L∞ = máximo.
- Producto punto: $x\cdot y = \sum x_i y_i = \|x\|\|y\|\cos\theta$. **Similitud coseno** = $\frac{x\cdot y}{\|x\|\|y\|}$ — la métrica estándar entre embeddings.
- Proyección de $x$ sobre $y$: $\text{proj}_y x = \frac{x\cdot y}{y\cdot y} y$.

## 2. Matrices como transformaciones
$Ax$ es una combinación lineal de las columnas de $A$. Una capa de red neuronal es $\sigma(Wx + b)$: transformación lineal + no linealidad.
- $(AB)^T = B^T A^T$; $(AB)^{-1} = B^{-1}A^{-1}$.
- Rango = dimensión del espacio columna. $A$ (n×n) invertible ⇔ rango n ⇔ $\det A \neq 0$.

### Eliminación gaussiana con pivoteo parcial
```
para k = 0..n-1:
    p = argmax_i>=k |A[i,k]|; intercambiar filas k,p
    para i = k+1..n-1:
        f = A[i,k]/A[k,k];  A[i,:] -= f*A[k,:];  b[i] -= f*b[k]
sustitución hacia atrás: x[i] = (b[i] - sum_{j>i} A[i,j] x[j]) / A[i,i]
```
Complejidad O(n³). El pivoteo evita dividir entre números pequeños (estabilidad numérica).

## 3. Ortogonalidad
Base ortonormal: $q_i\cdot q_j = \delta_{ij}$. Gram-Schmidt: $u_k = a_k - \sum_{j<k}(q_j\cdot a_k)q_j$, $q_k = u_k/\|u_k\|$. Produce $A = QR$.

## 4. Eigen-descomposición
$Av = \lambda v$. Si $A$ es simétrica: $A = Q\Lambda Q^T$ con $Q$ ortogonal y eigenvalores reales. Matriz de covarianza → PCA (módulo 12).
**Método de la potencia:** $v_{k+1} = Av_k/\|Av_k\|$ converge al eigenvector dominante; $\lambda \approx v^T A v$. (Así funciona PageRank.)

## 5. SVD
Toda matriz $A = U\Sigma V^T$. La mejor aproximación de rango $k$ (teorema de Eckart–Young) es $A_k = U_k\Sigma_k V_k^T$. Usos: compresión, PCA, sistemas de recomendación, LoRA (módulo 18) se basa en que las actualizaciones de pesos tienen rango bajo.

## 6. Cálculo vectorial
- Gradiente $\nabla f(x) = [\partial f/\partial x_1, \ldots]$ apunta a la dirección de máximo crecimiento.
- Jacobiano $J_{ij} = \partial f_i/\partial x_j$; Hessiano $H_{ij} = \partial^2 f/\partial x_i\partial x_j$.
- Identidades útiles: $\nabla_x(a^Tx) = a$, $\nabla_x(x^TAx) = (A + A^T)x$, $\nabla_x\|Ax-b\|^2 = 2A^T(Ax-b)$.
- **Regla de la cadena:** si $y = f(g(x))$, $\frac{dy}{dx} = f'(g(x))g'(x)$; en varias variables se multiplican jacobianos. Backpropagation = regla de la cadena aplicada en reversa sobre el grafo computacional.
- **Verificación de gradientes:** $\frac{\partial f}{\partial x_i} \approx \frac{f(x+he_i) - f(x-he_i)}{2h}$ (error O(h²)).

## 7. Optimización
- Convexa: $f(\theta x + (1-\theta)y) \le \theta f(x) + (1-\theta)f(y)$ ⇒ todo mínimo local es global.
- **Descenso de gradiente:** $x \leftarrow x - \eta\nabla f(x)$.
- **Momentum:** $v \leftarrow \beta v + \nabla f$; $x \leftarrow x - \eta v$.
- **Adam:** $m \leftarrow \beta_1 m + (1-\beta_1)g$, $s \leftarrow \beta_2 s + (1-\beta_2)g^2$, $\hat m = m/(1-\beta_1^t)$, $\hat s = s/(1-\beta_2^t)$, $x \leftarrow x - \eta\hat m/(\sqrt{\hat s}+\epsilon)$.
- **Newton:** $x \leftarrow x - H^{-1}\nabla f$ (convergencia cuadrática, costoso).
- Mínimos cuadrados: $\min\|Xw-y\|^2$ ⇒ ecuaciones normales $X^TXw = X^Ty$.
- Lagrange: optimizar $f$ s.a. $g(x)=0$ ⇒ $\nabla f = \lambda\nabla g$.
