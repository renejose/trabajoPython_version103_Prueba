def busqueda_binaria(lista, objetivo):
    inicio = 0
    fin = len(lista) - 1

    while inicio <= fin:
        medio = (inicio + fin) // 2
        if lista[medio] == objetivo:
            return medio  # Retorna el índice donde se encontró
        elif lista[medio] < objetivo:
            inicio = medio + 1
        else:
            fin = medio - 1

    return -1  # No se encontró el objetivo

# Ejemplo de uso
numeros = [1, 3, 5, 7, 9, 11, 13]
resultado = busqueda_binaria(numeros, 7)

if resultado != -1:
    print(f"Número encontrado en la posición {resultado}")
else:
    print("Número no encontrado")
