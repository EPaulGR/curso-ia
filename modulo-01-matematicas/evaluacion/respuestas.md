# Respuestas — Módulo 01

1. $\cos\theta = x\cdot y/(\|x\|\|y\|)$. Ignora la magnitud (longitud del documento, frecuencia) y compara solo dirección/semántica.
2. $Ax = \sum_j x_j a_j$: combinación lineal de las columnas.
3. Columnas linealmente dependientes; $Ax=b$ tiene cero o infinitas soluciones; $A$ no es invertible.
4. Evita dividir entre pivotes pequeños que amplifican errores de redondeo; también evita pivotes cero.
5. O(n³).
6. Si $Av=\lambda v$, $\bar v^TAv = \lambda\|v\|^2$ y también $= \overline{(\bar v^T A v)}$ por simetría, así $\lambda = \bar\lambda$.
7. Descomponiendo $v_0$ en eigenvectores, $A^kv_0$ queda dominado por $\lambda_1^k$; la velocidad depende de $|\lambda_2/\lambda_1|$.
8. La mejor aproximación de rango k en norma de Frobenius (y espectral) es la SVD truncada a k valores singulares.
9. Con datos centrados $X = U\Sigma V^T$, las columnas de $V$ son las direcciones principales y $\sigma_i^2/(n-1)$ las varianzas.
10. $(A+A^T)x$; $2X^T(Xw-y)$.
11. La derivada de una composición es el producto de jacobianos; backprop calcula ese producto de salida a entrada reutilizando resultados intermedios.
12. Por Taylor, los términos de orden h se cancelan en la diferencia central, dejando O(h²).
13. $f(\theta x+(1-\theta)y)\le\theta f(x)+(1-\theta)f(y)$; todo mínimo local es global.
14. Diverge u oscila; converge muy lento.
15. Momentum amortigua oscilaciones y acelera en valles alargados. La corrección de sesgo compensa que m y s inician en 0.
16. $L = \|Xw-y\|^2$, $\nabla L = 2X^T(Xw-y) = 0 \Rightarrow X^TXw = X^Ty$.
17. Encoge $w$ hacia 0 y mejora el condicionamiento al sumar λ a todos los eigenvalores.
18. $y = \lambda$, $x = \lambda$, $x+y=10$ ⇒ $x=y=5$, máximo 25.
