# Respuestas — Quiz módulo 08
1. ⟨X,D,C⟩; solución = asignación completa y consistente.
2. Variables S,E,N,D,M,O,R,Y ∈ {0..9} y acarreos C1..C4 ∈ {0,1}; AllDiff(letras); S≠0, M≠0; D+E = Y+10·C1, N+R+C1 = E+10·C2, E+O+C2 = N+10·C3, S+M+C3 = O+10·C4, C4 = M.
3. Ver teoria §2.
4. O(c·d³). No: solo reduce dominios; puede quedar arco-consistente y sin solución.
5. Elegir la variable con menos valores legales; desempate: más restricciones con variables libres. Detecta fallas temprano y poda el árbol cerca de la raíz.
6. Solo se necesita UNA solución: con la variable conviene fallar pronto (todas deben asignarse), con el valor conviene acertar (no se prueban los demás si funciona).
7. FC solo revisa los vecinos de la variable recién asignada; MAC ejecuta AC-3 completo a partir de esos arcos.
8. Asignación completa y reparación local; las soluciones están densamente distribuidas en el espacio.
9. O(n·d²): orden topológico, consistencia de arco dirigida hoja→raíz, asignación raíz→hojas sin retroceso.
10. Subconjunto S de variables cuya eliminación deja el grafo como árbol.
11. PRE: En(a,o) ∧ Avión(a) ∧ Aeropuerto(o) ∧ Aeropuerto(d); EFECTO: ¬En(a,o) ∧ En(a,d).
12. Todo hecho que no se afirma en el estado se considera falso.
13. g' = (g − ADD(a)) ∪ PRE(a), aplicable si a agrega algún literal de g y no borra ninguno.
14. Con C sobre A: lograr A-sobre-B primero o B-sobre-C primero obliga a deshacer la otra; las submetas no son independientes.
15. h_add suma costos de submetas suponiendo independencia y cuenta dos veces acciones compartidas → puede sobreestimar.
16. Pares de acciones o literales que no pueden coexistir en un nivel (efectos inconsistentes, interferencia, necesidades en competencia).
