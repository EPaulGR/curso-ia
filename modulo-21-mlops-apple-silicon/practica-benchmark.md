# Práctica: benchmark CPU vs MPS vs MLX

Usa `soluciones/ej02_benchmark.py` (o el tuyo) y mide matmul de n = 512, 1024, 2048, 4096, 8192 en fp32 y fp16:

```python
import numpy as np, torch, mlx.core as mx
from ej02_benchmark import medir, gflops_matmul

for n in [512, 1024, 2048, 4096]:
    a = np.random.rand(n, n).astype(np.float32)
    r_cpu = medir(lambda: a @ a)
    ta = torch.tensor(a, device="mps")
    r_mps = medir(lambda: ta @ ta, sincronizar=torch.mps.synchronize)
    ma = mx.array(a)
    r_mlx = medir(lambda: mx.eval(ma @ ma))
    print(n, [round(gflops_matmul(n, r["mediana"])) for r in (r_cpu, r_mps, r_mlx)])
```

Preguntas para el reporte:
1. ¿En qué n la GPU supera a la CPU? ¿Por qué no antes?
2. ¿Qué pasa si quitas la sincronización?
3. Mide tokens/s de un LLM 4-bit con `mlx_lm.generate` y compáralo con ancho_de_banda / tamaño_del_modelo.
4. Repite todo en la Mac Studio M5 Ultra cuando llegue y documenta la mejora.
