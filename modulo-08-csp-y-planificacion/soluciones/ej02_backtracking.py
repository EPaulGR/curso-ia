"""Ejercicio 02 — Búsqueda con retroceso (backtracking) y heurísticas (AIMA 6.3).

- MRV (mínimos valores restantes): elegir la variable con dominio actual más pequeño
  (desempate: mayor grado = más vecinos sin asignar).
- LCV (valor menos restrictivo): probar primero el valor que elimina menos opciones a los vecinos.
- Forward checking: al asignar X=x, borrar de los dominios de los vecinos no asignados
  los valores incompatibles; si alguno queda vacío → retroceder.
"""


def backtracking(csp, mrv=True, lcv=True, forward_checking=True):
    """Devuelve (asignacion dict o None, nodos) donde nodos = número de asignaciones probadas.
    No debe dejar modificados los dominios del csp al terminar."""
    nodos = 0
    dom = {v: list(d) for v, d in csp.dominios.items()}

    def elegir(asig):
        libres = [v for v in csp.variables if v not in asig]
        if not mrv:
            return libres[0]
        return min(libres, key=lambda v: (len(dom[v]), -sum(1 for w in csp.vecinos[v] if w not in asig)))

    def ordenar(var, asig):
        vals = list(dom[var])
        if not lcv:
            return vals
        def costo(x):
            return sum(1 for w in csp.vecinos[var] if w not in asig
                       for y in dom[w] if not csp.restriccion(var, x, w, y))
        return sorted(vals, key=costo)

    def bt(asig):
        nonlocal nodos
        if len(asig) == len(csp.variables):
            return dict(asig)
        var = elegir(asig)
        for x in ordenar(var, asig):
            if not csp.consistente(asig, var, x):
                continue
            nodos += 1
            asig[var] = x
            podados, ok = [], True
            if forward_checking:
                for w in csp.vecinos[var]:
                    if w in asig:
                        continue
                    for y in list(dom[w]):
                        if not csp.restriccion(var, x, w, y):
                            dom[w].remove(y)
                            podados.append((w, y))
                    if not dom[w]:
                        ok = False
                        break
            if ok:
                r = bt(asig)
                if r is not None:
                    return r
            for w, y in podados:
                dom[w].append(y)
            del asig[var]
        return None

    return bt({}), nodos
