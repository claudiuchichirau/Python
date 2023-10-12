def generare_cod_ascii(caracter_initial, nr_elemente):
    input = [n for n in range(ord(caracter_initial), ord(caracter_initial) + nr_elemente)]

    # convertesc codurile ASCII în formatul hex
    result = " ".join(hex(n)[2:] for n in input)

    return result


print(generare_cod_ascii('0', 10))
print(generare_cod_ascii('a', 16))

