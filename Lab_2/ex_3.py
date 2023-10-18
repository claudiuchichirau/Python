# Write a function that receives as parameters two lists a and b and returns: 
# (a intersected with b, a reunited with b, a - b, b - a)

def list_operations(list_1, list_2):
    intersection = []
    for element in list_1:
        if element in list_2 and element not in intersection:
            intersection.append(element)

    reunion = list_1 + [element for element in list_2 if element not in list_1]

    # diferența a - b
    dif1 = [element for element in list_1 if element not in list_2]

    # diferența b - a
    dif2 = [element for element in list_2 if element not in list_1]

    return intersection, reunion, dif1, dif2

list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [6, 7, 8, 9, 10, 11]

intersection, reunion, dif1, dif2 = list_operations(list_1, list_2)
print(f"Intersecția numerelor: {intersection}")
print(f"Reuniunea numerelor: {reunion}")
print(f"Diferența a - b: {dif1}")
print(f"Diferența b - a: {dif2}")
