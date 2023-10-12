def bit_sequence(numbers):
    bit_string = ' '.join([format(n, '08b') for n in numbers])
    count_0 = bit_string.count('0')
    count_1 = bit_string.count('1')
    return bit_string, count_0, count_1

numbers = [5,6,7,8,9]
bit_string, count_0, count_1 = bit_sequence(numbers)
print(f"Sirul: {bit_string}, nr de cifree 0: {count_0}, nr de cifre 1: {count_1}")
