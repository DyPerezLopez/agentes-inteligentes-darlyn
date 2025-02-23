#importamos libreria random
import random


# Tamaño de la cuadrícula
#definimos constantes
FILAS = 5 
COLUMNAS = 5

# Símbolos para representar el entorno
#definimos constantes
AGENTE = "A"
OBJETO = "O"
VACIO = "-"

# Función para crear una cuadrícula vacía
#cada celda se inicializa con el simbolo vacio (-)
def crear_cuadricula(filas, columnas):
    return [[VACIO for _ in range(columnas)] for _ in range(filas)]

# Función para mostrar la cuadrícula
#recorre cada fila de la cuadricula y la imprime el .join une los elementos de la fila con un espacio
def mostrar_cuadricula(cuadricula):
    for fila in cuadricula:
        print(" ".join(fila))
    print()

# Función para colocar el agente y el objeto en posiciones aleatorias
#coloca al agente en una posicion aleatoria, y de igual manera al objeto 
def colocar_agente_y_objeto(cuadricula):
    # Posición aleatoria del agente
    agente_fila = random.randint(0, FILAS - 1)
    agente_columna = random.randint(0, COLUMNAS - 1)
    cuadricula[agente_fila][agente_columna] = AGENTE

    # Posición aleatoria del objeto (diferente a la del agente)
    objeto_fila, objeto_columna = agente_fila, agente_columna
    while (objeto_fila, objeto_columna) == (agente_fila, agente_columna):
        objeto_fila = random.randint(0, FILAS - 1)
        objeto_columna = random.randint(0, COLUMNAS - 1)
    cuadricula[objeto_fila][objeto_columna] = OBJETO

    return (agente_fila, agente_columna), (objeto_fila, objeto_columna)

# Función para mover al agente hacia el objeto
#mueve al agente hacia el objeto, ajusta la fila arriba/abajo columna izquierda/derecha
# para devolver la posición del agente
def mover_agente(cuadricula, agente_pos, objeto_pos):
    agente_fila, agente_columna = agente_pos
    objeto_fila, objeto_columna = objeto_pos

    # Mover hacia la fila del objeto
    if agente_fila < objeto_fila:
        agente_fila += 1
    elif agente_fila > objeto_fila:
        agente_fila -= 1

    # Mover hacia la columna del objeto
    if agente_columna < objeto_columna:
        agente_columna += 1
    elif agente_columna > objeto_columna:
        agente_columna -= 1

    # Actualizar la posición del agente en la cuadrícula
    cuadricula[agente_pos[0]][agente_pos[1]] = VACIO
    cuadricula[agente_fila][agente_columna] = AGENTE

    return (agente_fila, agente_columna)

# Función principal
# crea y coloca al agente y al objeto
#usa un bucle para mover al agente hasta que enccuentre al objeto
# imprime el numero de pasos que hizo hasta encontrarlo
def main():
    # Crear la cuadrícula
    cuadricula = crear_cuadricula(FILAS, COLUMNAS)

    # Colocar al agente y al objeto en posiciones aleatorias
    agente_pos, objeto_pos = colocar_agente_y_objeto(cuadricula)

    # Mostrar la cuadrícula inicial
    print("Cuadrícula inicial:")
    mostrar_cuadricula(cuadricula)

    # Bucle para mover al agente hasta encontrar el objeto
    pasos = 0
    while agente_pos != objeto_pos:
        agente_pos = mover_agente(cuadricula, agente_pos, objeto_pos)
        pasos += 1
        print(f"Paso {pasos}:")
        mostrar_cuadricula(cuadricula)

    print(f"¡Objeto encontrado en {pasos} pasos!")

# Ejecutar el programa
# asegura que el programa se ejecute solo  si el aarchivo es el programa principal 
if __name__ == "__main__":
    main()