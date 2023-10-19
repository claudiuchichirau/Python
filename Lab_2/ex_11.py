# Write a function that will order a list of string tuples based on the 3rd character of the 2nd element in the tuple. 
# Example: ('abc', 'bcd'), ('abc', 'zza')] ==> [('abc', 'zza'), ('abc', 'bcd')]

def get_third_char_of_second_element(tup):
    return tup[1][2]

def order_tuples_by_third_char(lst):
    sorted_lst = sorted(lst, key=get_third_char_of_second_element)
    return sorted_lst

input_tuples = [('abc', 'bcd'), ('abc', 'zza')]
ordered_tuples = order_tuples_by_third_char(input_tuples)
print(ordered_tuples)
