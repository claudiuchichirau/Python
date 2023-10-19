#  Write a function that receives a number x, default value equal to 1, a list of strings, and a boolean flag set to True. 
# For each string, generate a list containing the characters that have the ASCII code divisible by x if the flag is set to True, 
# otherwise it should contain characters that have the ASCII code not divisible by x.

def filter_characters_by_ascii(x=1, strings=[], flag=True):
    result = []

    for string in strings:
        filtered_chars = []
        for char in string:
            ascii_code = ord(char)

            if flag and ascii_code % x == 0:
                filtered_chars.append(char)
            elif not flag and ascii_code % x != 0:
                filtered_chars.append(char)

        result.append(filtered_chars)

    return result

x = 2
strings = ["test", "hello", "lab002"]
flag = False
filtered_lists = filter_characters_by_ascii(x, strings, flag)

for filtered_chars in filtered_lists:
    print(filtered_chars)
