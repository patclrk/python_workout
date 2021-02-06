'''
Two functions:
 1. find_longest_word: Input = filename, Output = longest word in file
 2. find_all_longest_words: Input = Directory name, Output = Dictionary, keys=filesname, values=longest word in file
'''
import os

def find_longest_word(file):
    longest_word = ''
    with open(file) as f:
        for line in f:
            words = line.split()
            for word in words:
                if len(word) > len(longest_word):
                    longest_word = word
    return longest_word

# def find_all_longest_words(files):
#     longest_words = {}
#     for file in files:
#         longest_words[file] = find_longest_word(file)
#     print(longest_words)


# find_all_longest_words(['books/1342-0.txt', 'books/2701-0.txt', 'books/43-0.txt', 'books/46-0.txt', 'books/61105-0.txt', 'books/84-0.txt', 'books/pg25525.txt', 'books/pg28860.txt', 'books/pg345.txt'])


# book solution

def find_all_longest_words(dirname):
    return {
        filename: find_longest_word(os.path.join(dirname, filename))
        for filename in os.listdir(dirname) 
        if os.path.isfile(os.path.join(dirname, filename))
        }

print(find_all_longest_words('books'))