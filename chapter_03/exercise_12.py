# from collections import Counter

# def most_repeating_word(*args):
#     '''accepts a sequence of words
#     and returns the word with the
#     most repeated letters'''

#     result = {'word':'','score':0}
    
#     for words in args:
#         for word in words:
#             c = Counter(word).most_common(1)
#             if (c[0][1] > result['score']):
#                 result['word'] = word
#                 result['score'] = c[0][1]
    
#     return result['word']

# if __name__ == '__main__':
#     print(most_repeating_word(['this','is','elementary','logic']))


# book solution

from collections import Counter
import operator

WORDS = {'this', 'is', 'an', 'elementary', 'test', 'example'}

def most_repeating_letter_count_word(word):
    return Counter(word).most_common(1)[0][1]

def most_repeating_word(words):
    return max(words, key=most_repeating_letter_count_word)
                
print(most_repeating_word(WORDS))