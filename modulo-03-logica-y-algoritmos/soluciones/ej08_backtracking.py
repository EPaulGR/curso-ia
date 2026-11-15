"""Ejercicio 08 — Backtracking."""


def n_reinas(n):
    """Número de soluciones al problema de las N reinas."""
    cols, d1, d2 = set(), set(), set()

    def bt(f):
        if f == n:
            return 1
        t = 0
        for c in range(n):
            if c in cols or f - c in d1 or f + c in d2:
                continue
            cols.add(c); d1.add(f - c); d2.add(f + c)
            t += bt(f + 1)
            cols.remove(c); d1.remove(f - c); d2.remove(f + c)
        return t
    return bt(0)


def suma_subconjuntos(nums, objetivo):
    """Lista de todos los subconjuntos (listas, en el orden original) que suman objetivo; nums positivos."""
    res = []

    def bt(i, act, s):
        if s == objetivo:
            res.append(list(act))
        if s >= objetivo:
            return
        for j in range(i, len(nums)):
            act.append(nums[j]); bt(j + 1, act, s + nums[j]); act.pop()
    bt(0, [], 0)
    return res
