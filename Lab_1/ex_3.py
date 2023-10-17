def impartire(numarator, numitor, nr_zecimale=100):
    result = ""
    rest = numarator

    for _ in range(nr_zecimale + 1):
        cat, rest = divmod(rest * 10, numitor)
        result += str(cat)
        if _ == 0:
            result += "."
    return result

numarator = 1
numitor = 7
print(impartire(numarator, numitor))
