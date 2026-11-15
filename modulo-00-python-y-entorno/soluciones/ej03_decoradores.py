"""Ejercicio 03 — Decoradores y clausuras."""
import functools


def contar_llamadas(f):
    """Decorador que añade el atributo `llamadas` a la función, incrementándolo en cada llamada."""
    @functools.wraps(f)
    def envoltura(*args, **kwargs):
        envoltura.llamadas += 1
        return f(*args, **kwargs)
    envoltura.llamadas = 0
    return envoltura


def memoizar(f):
    """Decorador de caché manual (sin usar lru_cache) para argumentos posicionales hashables."""
    cache = {}

    @functools.wraps(f)
    def envoltura(*args):
        if args not in cache:
            cache[args] = f(*args)
        return cache[args]
    return envoltura


def crear_contador(inicio: int = 0):
    """Clausura: devuelve una función que cada vez que se llama regresa el siguiente entero desde inicio."""
    estado = [inicio - 1]

    def siguiente():
        estado[0] += 1
        return estado[0]
    return siguiente
