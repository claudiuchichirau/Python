# Write a function that receives a list of numbers and returns a list of the prime numbers found in it.

import math

def prime_numbers(numbers):
    prime_numbers_list = []
    for num in numbers:
        if num < 2:
            continue  
        is_prime = True
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            prime_numbers_list.append(num)
    
    return prime_numbers_list

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 17, 23, 29]
print(f"Numerele prime din lista data sunt: {prime_numbers(numbers)}")
