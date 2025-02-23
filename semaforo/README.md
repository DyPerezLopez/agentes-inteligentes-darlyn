## proyeto

este proyecto simula el comportamiento de un semaforo inteligente se ajustan los colores dependiendo a la funcion del trafico detectado:

## Tecnologias utilizadas

- python

## como funciona

uncionamiento:
Detección de vehículos:

Simula la detección de vehículos generando un número aleatorio entre 0 y 10.

Ajuste del tiempo:

Si el número de vehículos detectados supera un umbral (por defecto, 5), aumenta el tiempo en verde.

Si no, disminuye el tiempo en verde.

Cambio de estado:

El semáforo cambia de estado en este orden: verde → amarillo → rojo → verde.

Cada estado tiene un tiempo de espera configurable.

Salida:

Imprime el estado actual del semáforo y el número de vehículos detectados en cada ciclo.
