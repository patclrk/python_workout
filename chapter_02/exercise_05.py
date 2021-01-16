def pig_latin(s):
    """ accepts string, returns pig-latin conversion of the string
    if word begins with vowel, append 'way'
    if word begins with consonant, move to end of word, append 'ay'
    air = airway
    python = ythonpay """
    vowels = ['a','e','i','o','u']
    
    if (s[0] in vowels):
        return s + 'way'
    else:
        return s[1:] + s[0] + 'ay'
        

print(pig_latin('air'))
print(pig_latin('python'))


# book solution

# def pig_latin2(word):
#     if word[0] in 'aeiou':
#         return f'{word}way'
    
#     retrun f'{word[1:]}{word[0]}ay'