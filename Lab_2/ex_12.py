# Write a function that will receive a list of words  as parameter and will return a list of lists of words, grouped by rhyme. 
# Two words rhyme if both of them end with the same 2 letters.
# group_by_rhyme(['ana', 'banana', 'carte', 'arme', 'parte']) will return [['ana', 'banana'], ['carte', 'parte'], ['arme']] 

def group_by_rhyme(words):
    rhymes = {}
    for word in words:
        rhyme = word[-2:]
        if rhyme in rhymes:
            rhymes[rhyme].append(word)
        else:
            rhymes[rhyme] = [word]

    grouped_words = list(rhymes.values())
    return grouped_words

words = ['ana', 'banana', 'carte', 'arme', 'parte']
rhyme_groups = group_by_rhyme(words)
print(rhyme_groups)
