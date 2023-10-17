def rezolva_sistem_ecuatii(A, b):
    # matricea are nr egal de randuri si coloane?
    numar_rinduri_A = len(A)
    numar_coloane_A = len(A[0])
    if numar_rinduri_A != numar_coloane_A:
        return "Matricea nu este conforma."

    # nr de coloane al matricei = nr de elemente din b?
    if numar_coloane_A != len(b):
        return "Dimensiunea matricei A nu se potrivește cu dimensiunea vectorului b."

    # metoda eliminarii Gauss
    n = numar_coloane_A
    for pivot in range(n):
        for i in range(pivot + 1, n):
            factor = A[i][pivot] / A[pivot][pivot]
            for j in range(pivot, n):
                A[i][j] -= factor * A[pivot][j]
            b[i] -= factor * b[pivot]

    x = [0] * n
    for i in range(n - 1, -1, -1):
        x[i] = b[i]
        for j in range(i + 1, n):
            x[i] -= A[i][j] * x[j]
        x[i] /= A[i][i]

    return x

A = [[1, 2, 3, 4],
         [2, 3, 2, 1],
         [1, 0, 1, 0],
         [0, 1, 0, 1]]

b = [20, 10, 5, 7]

solutii = rezolva_sistem_ecuatii(A, b)
print(solutii)
