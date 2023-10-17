import itertools

def generare_permutari(alfabet, p, n):
    perms = list(itertools.product(alfabet, repeat=p))
    if n < len(perms):
        return perms[:n]
    else:
        return "n este prea mare"

alfabet = ['a', 'b', 'c', 'd', 'e']
p = 3
n = 5

print(generare_permutari(alfabet, p, n))
