def lists(list_1, list_2):
    intersection = []
    reunion = []
    dif1 = []
    dif2 = []

    intersection.append(list_1)
    intersection.append(list_2)
    for i in range(0, len(intersection)):
        for j in range(i + 1, len(intersection)):
            if (intersection[i] == intersection[j]):
                intersection.remove(intersection[i])
            print(f"i[{i}]:{intersection[i]}, i[{j}]:{intersection[j]}")

    return intersection


list_1 = [1, 2, 3, 4, 5, 6]
list_2 = [6, 7, 8, 9, 10, 11]
print(f"Intersectia numerelor: {lists(list_1, list_2)}")