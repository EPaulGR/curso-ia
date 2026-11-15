"""Ejercicio 03 — Decoradores y clausuras."""
import functools

def contar_llamadas(f):
    """Decorador que añade el atributo `llamadas` a la función, incrementándolo en cada llamada."""
    raise NotImplementedError  # TODO

def memoizar(f):
    """Decorador de caché manual (sin usar lru_cache) para argumentos posicionales hashables."""
    raise NotImplementedError  # TODO

def crear_contador(inicio: int=0):
    """Clausura: devuelve una función que cada vez que se llama regresa el siguiente entero desde inicio."""
    raise NotImplementedError  # TODO
