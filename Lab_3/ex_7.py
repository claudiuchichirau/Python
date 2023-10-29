# Write a function that receives a variable number of sets and returns a dictionary with the following operations from all sets 
# two by two: reunion, intersection, a-b, b-a. The key will have the following form: "a op b", where a and b are two sets, and op 
# is the applied operator: |, &, -. 

def set_operations(*sets):
    result = {}

    for i in range(len(sets)):
        for j in range(i + 1, len(sets)):
            set1 = sets[i]
            set2 = sets[j]
            key = f"{set1} | {set2}"
            result[key] = set1 | set2  # Union
            key = f"{set1} & {set2}"
            result[key] = set1 & set2  # Intersection
            key = f"{set1} - {set2}"
            result[key] = set1 - set2  # Set difference
            key = f"{set2} - {set1}"
            result[key] = set2 - set1  # Set difference

    return result

set1 = {1, 2}
set2 = {2, 3}

result = set_operations(set1, set2)
for key, value in result.items():
    print(f"{key}: {value}")
