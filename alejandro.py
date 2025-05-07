def es_primo(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def generar_primos(cantidad):
    primos = []
    numero = 2
    while len(primos) < cantidad:
        if es_primo(numero):
            primos.append(numero)
        numero += 1
    return primos

# Ejemplo de uso
n = int(input("¿Cuántos números primos deseas generar?: "))
print("Los primeros", n, "números primos son:")
print(generar_primos(n))
