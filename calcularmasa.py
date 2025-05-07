def calcular_imc(peso, estatura):
    """Calcula el índice de masa corporal (IMC)."""
    return peso / (estatura ** 2)

def clasificar_imc(imc):
    """Clasifica el IMC en distintas categorías."""
    if imc < 16:
        return "Anémico"
    elif 16 <= imc < 18.5:
        return "Delgado"
    elif 18.5 <= imc < 25:
        return "Normal"
    elif 25 <= imc < 30:
        return "Gordo"
    else:
        return "Obeso"

# Solicita datos al usuario
try:
    peso = float(input("Ingrese su peso en kilogramos (kg): "))
    estatura = float(input("Ingrese su estatura en metros (m): "))

    if peso <= 0 or estatura <= 0:
        print("Error: el peso y la estatura deben ser valores positivos.")
    else:
        imc = calcular_imc(peso, estatura)
        categoria = clasificar_imc(imc)

        print(f"\nSu IMC es: {imc:.2f}")
        print(f"Clasificación: {categoria}")

except ValueError:
    print("Error: Ingrese valores numéricos válidos.")