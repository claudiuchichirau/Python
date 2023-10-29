# The validate_dict function that receives as a parameter a set of tuples ( that represents validation rules for a dictionary that 
# has strings as keys and values) and a dictionary. A rule is defined as follows: (key, "prefix", "middle", "suffix"). 
# A value is considered valid if it starts with "prefix", "middle" is inside the value (not at the beginning or end) and ends 
# with "suffix". The function will return True if the given dictionary matches all the rules, False otherwise.

def validate_dict(rules, dictionary):
    for key, prefix, middle, suffix in rules:
        if key not in dictionary:
            return False  # The key is not present in the dictionary

        value = dictionary[key]
        if not value.startswith(prefix) or not value.endswith(suffix):
            return False  # Value does not start or end as specified

        # Check if "middle" is inside the value, not at the beginning or end
        middle_index = value.find(middle)
        if middle_index == -1 or middle_index == 0 or middle_index == len(value) - len(middle):
            return False

    return True  # All rules passed

validation_rules = {("key", "abc", "xyz", "def")}
data_dict = {"key": "abcinsidexyzadef"}

result = validate_dict(validation_rules, data_dict)
print(result)  
