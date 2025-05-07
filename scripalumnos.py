import pandas as pd # type: ignore

# Lista de alumnos (estructura de datos tipo lista de diccionarios)
alumnos = [
    {"Nombre": "Ana", "Edad": 20, "Carrera": "Ingeniería", "Promedio": 8.9},
    {"Nombre": "Luis", "Edad": 22, "Carrera": "Medicina", "Promedio": 9.3},
    {"Nombre": "María", "Edad": 21, "Carrera": "Arquitectura", "Promedio": 8.5},
    {"Nombre": "Carlos", "Edad": 23, "Carrera": "Derecho", "Promedio": 7.8},
]

# Crear DataFrame
df = pd.DataFrame(alumnos)

# Exportar a Excel
archivo_salida = "alumnos.xlsx"
df.to_excel(archivo_salida, index=False)

print(f"Archivo '{archivo_salida}' generado con éxito.")
