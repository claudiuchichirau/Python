def calc_arie(X, Y):
    n = len(Y)
    arie = 0
    for i in range(1, n):
        dx = X[i] - X[i-1]
        trapez = (Y[i-1] + Y[i]) / 2
        arie += trapez * dx
    return arie

X = [1, 2, 4, 7, 8]
Y = [1, 2, 3, 4, 5]
arie = calc_arie(X, Y)
print(f"Aria aproximativă este: {arie}")
