# Conclusiones
Tomando `n` como el número de elementos en los que buscar:

* La **búsqueda secuencial**, en el peor de los casos, necesitaría `n` ejecuciones para llegar al resultado final.
* La **búsqueda binaria**, en el peor de los casos, necesitaría `log(n)` ejecuciones para llegar al resultado final.

Por lo tanto, el algoritmo de búsqueda binaria es más favorable a la hora de realizar búsquedas sobre conjuntos de datos
muy grandes, a pesar de que haya que tener que ordenar ese mismo conjunto antes de realizar esta búsqueda. Lo ideal sería
mantener una base de datos ordenada para así poder realizar consultas mucho más rápido que con una búsqueda secuencial.
