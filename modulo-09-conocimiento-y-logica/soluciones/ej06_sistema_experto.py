"""Ejercicio 06 — Mini sistema experto / mini-Prolog (AIMA 9.3–9.4; Negnevitsky cap. 2).

Base de conocimiento de primer orden con cláusulas definidas:
    hechos: átomos base, p. ej. ('padre', 'ana', 'luis')
    reglas: (lista_de_premisas, conclusion) con variables, p. ej.
            ([('padre','?x','?y'), ('padre','?y','?z')], ('abuelo','?x','?z'))

1. encadenamiento_adelante_fol: aplica reglas hasta punto fijo (FOL-FC-ASK) → todos los hechos.
2. consultar: encadenamiento hacia atrás estilo Prolog (SLD, profundidad primero), genera
   todas las sustituciones que hacen verdadera la meta; renombra variables de cada regla.
3. explicar: devuelve la cadena de reglas usadas para derivar un hecho (capacidad de
   explicación típica de sistemas expertos como MYCIN).
"""
import itertools

_contador = itertools.count()


def _var(t):
    return isinstance(t, str) and t.startswith("?")


def _sust(t, th):
    if _var(t):
        return _sust(th[t], th) if t in th else t
    if isinstance(t, tuple):
        return tuple(_sust(x, th) for x in t)
    return t


def _unificar(x, y, th):
    """DADO (ver ej05)."""
    if th is None:
        return None
    x, y = _sust(x, th), _sust(y, th)
    if x == y:
        return th
    if _var(x):
        return {**th, x: y}
    if _var(y):
        return {**th, y: x}
    if isinstance(x, tuple) and isinstance(y, tuple) and len(x) == len(y):
        for a, b in zip(x, y):
            th = _unificar(a, b, th)
        return th
    return None


def _renombrar(t, sufijo):
    if _var(t):
        return f"{t}_{sufijo}"
    if isinstance(t, tuple):
        return tuple(_renombrar(x, sufijo) for x in t)
    return t


def encadenamiento_adelante_fol(hechos, reglas):
    """Conjunto de todos los hechos base derivables."""
    conocidos = set(hechos)
    while True:
        nuevos = set()
        for prem, concl in reglas:
            thetas = [{}]
            for p in prem:
                thetas = [t2 for th in thetas for h in conocidos
                          if (t2 := _unificar(p, h, th)) is not None]
            for th in thetas:
                c = _sust(concl, th)
                if c not in conocidos:
                    nuevos.add(c)
        if not nuevos:
            return conocidos
        conocidos |= nuevos


def consultar(meta, hechos, reglas, profundidad=20):
    """Generador de sustituciones (dict) restringidas a las variables de `meta`."""
    vars_meta = set()

    def recoger(t):
        if _var(t):
            vars_meta.add(t)
        elif isinstance(t, tuple):
            for x in t:
                recoger(x)
    recoger(meta)
    clausulas = [([], h) for h in hechos] + list(reglas)

    def resolver(metas, th, d):
        if not metas:
            yield th
            return
        if d == 0:
            return
        primera, resto = metas[0], metas[1:]
        for prem, concl in clausulas:
            s = next(_contador)
            prem_r = [_renombrar(p, s) for p in prem]
            th2 = _unificar(primera, _renombrar(concl, s), th)
            if th2 is not None:
                yield from resolver(prem_r + resto, th2, d - 1)

    vistos = set()
    for th in resolver([meta], {}, profundidad):
        r = {v: _sust(v, th) for v in vars_meta}
        clave = tuple(sorted(r.items()))
        if clave not in vistos:
            vistos.add(clave)
            yield r


def explicar(hecho, hechos, reglas):
    """Lista de pasos (premisas_instanciadas, conclusion) que prueban `hecho`, desde los
    hechos hasta la conclusión; [] si es un hecho dado; None si no se puede probar."""
    if hecho in hechos:
        return []
    for prem, concl in reglas:
        th = _unificar(concl, hecho, {})
        if th is None:
            continue
        thetas = [th]
        for p in prem:
            thetas = [t2 for t in thetas for h in encadenamiento_adelante_fol(hechos, reglas)
                      if (t2 := _unificar(p, h, t)) is not None]
        for t in thetas:
            pasos, ok = [], True
            inst = [_sust(p, t) for p in prem]
            for p in inst:
                sub = explicar(p, hechos, reglas)
                if sub is None:
                    ok = False
                    break
                pasos += sub
            if ok:
                return pasos + [(inst, hecho)]
    return None
