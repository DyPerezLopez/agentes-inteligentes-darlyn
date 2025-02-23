#hacemos importacion de librerias time y random
import time
import random #se utiliza para generar numeros en aleatorio

#se crea una clase
class SemaforoInteligente: #definimos un constructor, se llama automaticamente cuando se crea una clase
    def __init__(self):
        self.estado = "rojo"  # Estado inicial del semáforo (inicializa)
        self.tiempo_verde = 10  # Tiempo inicial en verde
        self.tiempo_amarillo = 3  # Tiempo en amarillo
        self.tiempo_rojo = 5  # Tiempo en rojo
        self.umbral_vehiculos = 5  # Umbral para ajustar el tiempo (representa el numero de vehiculos )

    def detectar_vehiculos(self):
        # Simulamos la detección de vehículos (número aleatorio entre 0 y 10)
        return random.randint(0, 10)

    def ajustar_tiempo(self, vehiculos_detectados):
        # Ajustamos el tiempo en verde según el número de vehículos detectados
        if vehiculos_detectados > self.umbral_vehiculos: # numero de vehiculos mayor al umbral
            self.tiempo_verde = min(20, self.tiempo_verde + 2)  # Aumentamos el tiempo en verde si en dado caso hay varios vehiculos
        else:
            self.tiempo_verde = max(5, self.tiempo_verde - 2)  # Disminuimos el tiempo en verde si no hay muchos vehiculos

    def cambiar_estado(self): #cambia de estado del semaforo
        if self.estado == "verde": #si esta en verde
            print("Cambiando a amarillo...") #cambiara mensaje de cambio
            self.estado = "amarillo" #pasara al estado de cambio
            time.sleep(self.tiempo_amarillo) #pausa del programa por el tiempo definido
        elif self.estado == "amarillo":
            print("Cambiando a rojo...")
            self.estado = "rojo"
            time.sleep(self.tiempo_rojo)
        elif self.estado == "rojo":
            print("Cambiando a verde...")
            self.estado = "verde"
            time.sleep(self.tiempo_verde)

    def ejecutar(self): #ciclo principal del semaforo
        while True: #ciclo infinito
            vehiculos = self.detectar_vehiculos() #llama al metodo
            print(f"Vehículos detectados: {vehiculos}") #imprime los vehiculos que detecta
            self.ajustar_tiempo(vehiculos) #ajusta el tiempo segun la deteccion de vehiculos
            print(f"Estado actual del semáforo: {self.estado}") # imprime el estado del semaforo
            self.cambiar_estado() #cambia el estado

if __name__ == "__main__": #comprueba que el script funciona
    semaforo = SemaforoInteligente() #crea una instancia para acceder a los metodos 
    semaforo.ejecutar() #llama al metodo ejecutar para inicial el ciclo del semaforo