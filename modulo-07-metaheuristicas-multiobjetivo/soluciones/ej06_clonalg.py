"""Ejercicio 06 — Sistema inmune artificial: CLONALG (BUAP 4.5; de Castro & Von Zuben 2002).

Principio de selección clonal, para MINIMIZAR f: R^n → R:
1. Población de anticuerpos aleatorios en [lim_inf, lim_sup]^n.
2. Seleccionar los n_sel mejores (mayor afinidad = menor f).
3. Clonar: el de rango r (1 = mejor) produce round(beta·N / r) clones.
4. Hipermutación inversamente proporcional a la afinidad: clon + N(0, σ_r) con
   σ_r = escala · exp(−ρ · afinidad_normalizada), afinidad normalizada en [0,1] (1 = mejor).
5. Reemplazar la población por los mejores (originales + clones) y sustituir los
   d peores por anticuerpos aleatorios nuevos (diversidad).
"""
import numpy as np


def clonalg(f, dim, lim_inf, lim_sup, tam=30, n_sel=10, beta=1.0, rho=2.0, escala=None,
            d=3, generaciones=100, semilla=0):
    """Devuelve (mejor_x: np.ndarray, mejor_f: float)."""
    rng = np.random.default_rng(semilla)
    escala = escala if escala is not None else 0.1 * (lim_sup - lim_inf)
    pob = rng.uniform(lim_inf, lim_sup, (tam, dim))
    for _ in range(generaciones):
        fx = np.array([f(x) for x in pob])
        orden = np.argsort(fx)
        sel = pob[orden[:n_sel]]
        fsel = fx[orden[:n_sel]]
        rango = fsel.max() - fsel.min()
        afin = 1 - (fsel - fsel.min()) / rango if rango > 0 else np.ones(n_sel)
        clones = []
        for r, (x, a) in enumerate(zip(sel, afin), start=1):
            nc = max(1, round(beta * tam / r))
            sigma = escala * np.exp(-rho * a)
            c = x + rng.normal(0, sigma, (nc, dim))
            clones.append(np.clip(c, lim_inf, lim_sup))
        todos = np.vstack([pob] + clones)
        ft = np.array([f(x) for x in todos])
        pob = todos[np.argsort(ft)[:tam]]
        pob[-d:] = rng.uniform(lim_inf, lim_sup, (d, dim))
    fx = np.array([f(x) for x in pob])
    i = int(np.argmin(fx))
    return pob[i], float(fx[i])
