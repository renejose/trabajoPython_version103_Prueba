print("Esto es segudno")
def calcular_promedio(notas):
    return sum(notas) / len(notas)

def clasificar_promedio(promedio):
    if promedio >= 18:
        return "Excelente"
    elif promedio >= 14:
        return "Bueno"
    elif promedio >= 11:
        return "Regular"
    else:
        return "Reprobado"

def main():
    try:
        nombre = input("Ingrese el nombre del alumno: ")
        cantidad = int(input("¿Cuántas notas desea ingresar?: "))
        
        notas = []
        for i in range(cantidad):
            nota = float(input(f"Ingrese la nota #{i+1}: "))
            if 0 <= nota <= 20:
                notas.append(nota)
            else:
                print("La nota debe estar entre 0 y 20. Intente de nuevo.")
                return

        promedio = calcular_promedio(notas)
        clasificacion = clasificar_promedio(promedio)

        print(f"\nAlumno: {nombre}")
        print(f"Promedio: {promedio:.2f}")
        print(f"Desempeño: {clasificacion}")

    except ValueError:
        print("Error: Ingrese solo números válidos.")

if __name__ == "__main__":
    main()
