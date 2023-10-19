# Write a function that receives as a parameter a variable number of lists and a whole number x. 
# Return a list containing the items that appear exactly x times in the incoming lists. 

def find_items_appearing_x_times(x, *lists):
    item_count = {} #dictionar

    for lst in lists:
        for item in lst:
            item_count[item] = item_count.get(item, 0) + 1

    result = []

    for item, count in item_count.items():
        if count == x:
            result.append(item)

    return result

list1 = [1, 2, 2, 3, 4, 4, 4]
list2 = [2, 4, 4, 5, 6, 6]
list3 = [1, 3, 4, 5, 7]
x = 2

print(f"Elementele care apar exact de {x} ori sunt: {find_items_appearing_x_times(x, list1, list2, list3)}")
