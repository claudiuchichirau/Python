# Write a function that receives a variable number of lists and returns a list of tuples as follows: the first tuple contains 
# the first items in the lists, the second element contains the items on the position 2 in the lists, etc. Ex: for lists [1,2,3], 
# [5,6,7], ["a", "b", "c"] return: [(1, 5, "a ") ,(2, 6, "b"), (3,7, "c")]. 

def lists(*lists):
    result = []
    min_length = min(len(lst) for lst in lists)

    for i in range(min_length):
        tuple_items = tuple(lst[i] for lst in lists)
        result.append(tuple_items)

    return result

list1 = [1, 2, 3]
list2 = [5, 6, 7]
list3 = ["a", "b", "c"]

print(lists(list1, list2, list3))
