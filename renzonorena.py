def contar_frecuencia_palabras(lista_palabras):
    frecuencia = {}  # Diccionario para almacenar la frecuencia de cada palabra

    for palabra in lista_palabras:
        if palabra in frecuencia:
            frecuencia[palabra] += 1
        else:
            frecuencia[palabra] = 1

    return frecuencia

# Ejemplo de uso:
palabras = ['gato', 'perro', 'gato', 'pez', 'perro', 'perro']
frecuencias = contar_frecuencia_palabras(palabras)

# Mostrar resultado
for palabra, cuenta in frecuencias.items():
    print(f"La palabra '{palabra}' aparece {cuenta} veces.")