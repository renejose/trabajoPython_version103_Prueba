# Lista de estudiantes (estructura de datos: lista de diccionarios)
estudiantes = [
    {"nombre": "Ana", "edad": 20, "notas": [15, 17, 18]},
    {"nombre": "Luis", "edad": 22, "notas": [14, 13, 16]},
    {"nombre": "María", "edad": 21, "notas": [18, 19, 17]}
]

# Función para calcular el promedio de un estudiante
def calcular_promedio(notas):
    return sum(notas) / len(notas)

# Función para mostrar información de los estudiantes
def mostrar_estudiantes(estudiantes):
    for estudiante in estudiantes:
        promedio = calcular_promedio(estudiante["notas"])
        print(f"{estudiante['nombre']} (Edad: {estudiante['edad']} años) - Promedio: {promedio:.2f}")

# Ejecutar la función
mostrar_estudiantes(estudiantes)