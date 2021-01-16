'''
Translate a sentence into piglatin.
Returns a string
'''
def pl_sentence(sentence):
    words = sentence.split()
    result = []
    for word in words:
        result.append(pig_latin(word))
    
    return(' '.join(result))

def pig_latin(word):
    if word[0] in 'aeioi':
        return f'{word}way'
    return f'{word[1:]}{word[0]}ay'

if __name__  == "__main__":
    print(pl_sentence("this is a sentence"))