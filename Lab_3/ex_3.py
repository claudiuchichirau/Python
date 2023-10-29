# Compare two dictionaries without using the operator "==" returning True or False. (Attention, dictionaries must be recursively 
# covered because they can contain other containers, such as dictionaries, lists, sets, etc.)

def compare_dicts(dict1, dict2):
    if type(dict1) != type(dict2):
        return False

    if isinstance(dict1, dict): # verific daca dict1 este de tip dictionar
        if set(dict1.keys()) != set(dict2.keys()):   # verific daca cele doua dictionare au chei diferite
            return False

        for key in dict1:
            if not compare_dicts(dict1[key], dict2[key]):
                return False
    elif isinstance(dict1, (list, set, tuple)):
        if len(dict1) != len(dict2):
            return False

        for val1, val2 in zip(dict1, dict2):
            if not compare_dicts(val1, val2):
                return False
    else:
        return dict1 == dict2

    return True

dict1 = {"a": 1, "b": [1, 2, 3], "c": {"x": 10, "y": [7, 8]}}
dict2 = {"a": 1, "b": [1, 2, 3], "c": {"x": 10, "y": [7, 8]}}

result = compare_dicts(dict1, dict2)
print(result)
