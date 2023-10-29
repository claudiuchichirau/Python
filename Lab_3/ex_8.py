# Write a function that receives a single dict parameter named mapping. This dictionary always contains a string key "start". 
# Starting with the value of this key you must obtain a list of objects by iterating over mapping in the following way: the value 
# of the current key is the key for the next value, until you find a loop (a key that was visited before). 
# The function must return the list of objects obtained as previously described.

def loop(mapping):
    visited = set() 
    result = []

    current_key = "start" 
    while current_key not in visited:
        visited.add(current_key)
        next_key = mapping.get(current_key)

        if next_key is not None:
            result.append(next_key)
            current_key = next_key
        else:
            break  

    return result

mapping = {'start': 'a', 'b': 'a', 'a': '6', '6': 'z', 'x': '2', 'z': '2', '2': '2', 'y': 'start'}
result_list = loop(mapping)
print(result_list)
