def calcular_promedio(numeros):
    if not numeros:
        return 0  # Evitar división por cero si la lista está vacía
    suma = sum(numeros)
    promedio = suma / len(numeros)
    return promedio

# Ejemplo de uso
lista = [7.5, 8.0, 9.2, 6.8]
prom = calcular_promedio(lista)
print(f"El promedio es: {prom:.2f}")


def sumar_numeros(num1,num2):
    resultado= num1 + num2
    return resultado
