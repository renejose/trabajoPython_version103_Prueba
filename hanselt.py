def fibonacci_rec(n):
    if n <= 1:
        return n
    else:
        return fibonacci_rec(n-1) + fibonacci_rec(n-2)

# Imprimir los primeros 10 números
for i in range(10):
    print(fibonacci_rec(i), end=" ")
