# Write a function that receives as a parameter a list and returns a tuple (a, b), representing the number of unique elements 
# in the list, and b representing the number of duplicate elements in the list (use sets to achieve this objective).

def count_unique_and_duplicate_elements(input_list):
    unique_elements = len(set(input_list))
    duplicate_elements = len(input_list) - unique_elements
    return unique_elements, duplicate_elements

my_list = [1, 2, 2, 3, 4, 4, 5, 6]
unique_count, duplicate_count = count_unique_and_duplicate_elements(my_list)
result_tuple = (unique_count, duplicate_count)
print(result_tuple)
