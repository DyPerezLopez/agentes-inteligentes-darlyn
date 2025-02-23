

#define la funcion del sistema
def sistema():
    ##bienvenida y explicacion en consola
    print("Bienvenido al Sistema Experto de Diagnóstico Simple")
    print("Por favor, responde las siguientes preguntas con 'sí' o 'no'.")

    # Preguntas para recopilar síntomas
    #.strip().lower elimina espacios y convierte mayusculas en minusculas
    fiebre = input("¿Tienes fiebre? (sí/no): ").strip().lower()
    tos = input("¿Tienes tos? (sí/no): ").strip().lower()
    dolor_garganta = input("¿Tienes dolor de garganta? (sí/no): ").strip().lower()
    congestion_nasal = input("¿Tienes congestión nasal? (sí/no): ").strip().lower()
    dolor_cabeza = input("¿Tienes dolor de cabeza? (sí/no): ").strip().lower()
    estornudos = input("¿Tienes estornudos frecuentes? (sí/no): ").strip().lower()
    fatiga = input("¿Te sientes fatigado/a? (sí/no): ").strip().lower()

    # Reglas de diagnóstico
    if fiebre == "sí" and tos == "sí" and dolor_garganta == "sí" and fatiga == "sí":
        print("\nDiagnóstico: Podrías tener **gripe**.")
    elif congestion_nasal == "sí" and estornudos == "sí" and dolor_cabeza == "sí":
        print("\nDiagnóstico: Podrías tener **alergia estacional**.")
    elif tos == "sí" and congestion_nasal == "sí" and dolor_garganta == "sí":
        print("\nDiagnóstico: Podrías tener un **resfriado común**.")
    else:
        print("\nDiagnóstico: Tus síntomas no coinciden con las condiciones evaluadas. Consulta a un médico para un diagnóstico preciso.")

# Ejecutar el sistema experto
if __name__ == "__main__":
    sistema()