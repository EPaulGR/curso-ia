"""Ejercicio 03 — Monte Carlo."""
import numpy as np

def estimar_pi(n, semilla=0):
    """Estima pi con n puntos uniformes en [-1,1]^2."""
    raise NotImplementedError  # TODO

def integral_mc(f, a, b, n, semilla=0):
    """Estima la integral de f en [a,b] (f vectorizada)."""
    raise NotImplementedError  # TODO

def muestreo_rechazo(p, a, b, M, n, semilla=0):
    """n muestras de densidad p en [a,b] con p(x) <= M, propuesta uniforme."""
    raise NotImplementedError  # TODO
