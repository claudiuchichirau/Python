# Write a function to return a list of the first n numbers in the Fibonacci string

def fibonacci(n):
    sir = [0, 1]
    for i in range(2, n):
        element = sir[i-1] + sir[i-2]
        sir.append(element)
    return sir

n = 13
print(f"Primele {n} numere din sirul fibonacci sunt: {fibonacci(n)}")