def suma_nr(n):
    suma = 0
    for i in range(1, n+1):
        suma= suma+ i
    return suma

# Testează funcția
n = 7
print(f"Suma primelor {n} numere este {suma_nr(n)}")
