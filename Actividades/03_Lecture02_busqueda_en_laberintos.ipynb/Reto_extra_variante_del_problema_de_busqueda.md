# Reto Extra: Variante del problema de búsqueda

## Variante elegida: Múltiples metas

### Estado

El estado está compuesto por:

- La posición actual del agente `(fila, columna)`
- El conjunto de metas que aún no ha alcanzado

Por ejemplo:

```text
((3,5), {M2, M4})
```

El agente se encuentra en la posición `(3,5)` y todavía no ha visitado las metas `M2` y `M4`.

La posición del agente solamente no puede determinar el comportamiento futuro, ya que llegar a una misma celda después de haber visitado distintas metas representa situaciones totalmente diferentes

---

### Acciones

 Siempre que no exista un muro, el agente puede realizar las siguientes acciones en cada uno de los estados:

- Moverse hacia arriba
- Moverse hacia abajo
- Moverse hacia la izquierda
- Moverse hacia la derecha

---

### Modelo de transición

Al ser ejecutada una acción se tienen las siguientes posibilidades:

1. El agente cambia a la celda correspondiente.
2. Si la nueva celda contiene una meta pendiente, esta se elimina del conjunto de metas restantes.
3. En caso contrario, únicamente cambia la posición del agente.

El problema termina cuando el conjunto de metas pendientes queda vacío.

---

### Costo de cada acción

Cada movimiento tiene un costo de **1**.

El costo total del camino es igual al número de movimientos que se requirieron para visitar todas las metas

---

### Heurística propuesta

Se utiliza como heurística la distancia Manhattan desde la posición actual hasta la **meta pendiente más cercana**

\[
h(n)=\min_{g\in G} |x_n-x_g|+|y_n-y_g|
\]

donde \(G\) es el conjunto de metas que aún no han sido visitadas

---

### ¿La heurística es admisible?

Sí, porque la distancia Manhattan nunca sobreestima el costo mínimo necesario para llegar a una meta, ella supone un recorrido directo sin considerar obstáculos. Además, al seleccionar la meta pendiente más cercana, el valor que se calcula es menor o igual al costo real restante para completar el problema

Por esto, la heurística es **admisible** y puede utilizarse con A* la garantía de encontrar una solución óptima
