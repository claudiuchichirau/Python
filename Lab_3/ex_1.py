# Write a function that receives as parameters two lists a and b and returns a list of sets containing: 
# (a intersected with b, a reunited with b, a - b, b - a)

def calculate_operations(a, b):
    intersection = set(a) & set(b)
    union = set(a) | set(b)
    diff_a_b = set(a) - set(b)
    diff_b_a = set(b) - set(a)

    return [intersection, union, diff_a_b, diff_b_a]

list_a = [1, 2, 3, 4, 5]
list_b = [3, 4, 5, 6, 7]

intersection, union, diff_a_b, diff_b_a = calculate_operations(list_a, list_b)
print("Intersection: ", intersection)
print("Union: ", union)
print("Difference A - B: ", diff_a_b)
print("Difference B - A: ", diff_b_a)
