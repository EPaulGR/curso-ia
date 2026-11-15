# Teoría — Redes neuronales

## 1. Neurona y perceptrón
Una neurona calcula a = φ(w·x + b). El perceptrón usa φ = signo y la regla w ← w + η·y·x cuando clasifica mal; converge si los datos son linealmente separables (teorema de Novikoff). No puede aprender XOR: hace falta una capa oculta.

## 2. MLP como composición
f(x) = W₃ φ(W₂ φ(W₁x + b₁) + b₂) + b₃. Sin φ no lineal, toda la red colapsa a una sola transformación lineal. El **teorema de aproximación universal** dice que una capa oculta suficientemente ancha aproxima cualquier función continua en un compacto; en la práctica, la profundidad da representaciones jerárquicas con muchos menos parámetros.

## 3. Pérdidas
- Regresión: MSE ↔ máxima verosimilitud con ruido gaussiano.
- Clasificación: softmax + entropía cruzada L = −log p_y ↔ máxima verosimilitud categórica.
Gradiente clave: ∂L/∂z = p − onehot(y). Por eso softmax y entropía cruzada se combinan (más estable y simple).

## 4. Backpropagation
Para la capa z = aW + b, con δ = ∂L/∂z:
- ∂L/∂W = aᵀ δ
- ∂L/∂b = Σ δ (sobre el batch)
- ∂L/∂a = δ Wᵀ
- A través de la activación: ∂L/∂z_prev = ∂L/∂a ⊙ φ'(z_prev)
Backprop es la regla de la cadena aplicada en orden topológico inverso: cuesta lo mismo (orden) que el forward. Esto es **autodiferenciación en modo reverso**; PyTorch construye el grafo dinámicamente y llama `backward()`.

**Gradient checking:** compara con (f(θ+h) − f(θ−h)) / 2h; error relativo < 1e-6 indica implementación correcta.

## 5. Inicialización
Si los pesos son muy grandes/pequeños, la varianza de las activaciones explota o se anula con la profundidad. Xavier: Var(W) = 1/n_in (tanh/sigmoide); He: 2/n_in (ReLU). Nunca inicializar todos iguales (simetría).

## 6. Optimización
- SGD: θ ← θ − η g. Mini-batches dan ruido útil y eficiencia.
- Momentum: v ← βv + g; θ ← θ − ηv (acelera en valles alargados).
- Adam: medias móviles de g y g² con corrección de sesgo; paso adaptativo por parámetro. AdamW desacopla el weight decay.
- Learning rate: el hiperparámetro más importante. Warmup + decaimiento coseno es el estándar moderno.

## 7. Regularización
- L2 / weight decay: añade λ/2‖W‖².
- Dropout (invertido): en entrenamiento multiplica por máscara Bernoulli/(1−p); en inferencia no hace nada.
- Early stopping: detener cuando la pérdida de validación deja de mejorar.
- BatchNorm/LayerNorm: normalizan activaciones, estabilizan y aceleran.

## 8. PyTorch en Mac
```python
device = "mps" if torch.backends.mps.is_available() else "cpu"
model = Net().to(device)
for xb, yb in loader:
    xb, yb = xb.to(device), yb.to(device)
    opt.zero_grad(); loss = crit(model(xb), yb); loss.backward(); opt.step()
```
Consejos MPS: usa float32 (float64 no está soportado en MPS), lotes grandes para aprovechar la GPU, `PYTORCH_ENABLE_MPS_FALLBACK=1` para operaciones faltantes, y `torch.mps.synchronize()` antes de medir tiempos.

## 9. Diagnóstico
- Pérdida no baja: learning rate, bug en gradiente, datos sin normalizar.
- Sobreajusta: más datos/augmentation, regularización, modelo menor.
- Primer sanity check: sobreajustar un batch pequeño hasta pérdida ≈ 0.
