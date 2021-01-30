'''
write a wordcount function that mimics wc
Input: filename
Output: 4 lines
  - Number of characters (including whitespace)
  - Number of words (separated by whitespace)
  - Number of lines
  - Number of unique words (case sensitive)
'''

def wordcount(file):
    counts = {'lines': 0, 'words': 0, 'uniqwords': 0, 'chars': 0}
    unique_words = set()
    with open(file) as f:
        for line in f.readlines():
            counts['lines'] += 1
            counts['chars'] += len(line)
            counts['words'] += len(line.split())
            for word in line.split():
                unique_words.add(word)
    
    # debug
    #print(f'unique words: {unique_words}')


    print(f'''
    Number of characters: {counts['chars']}
    Number of words: {counts['words']}
    Number of lines: {counts['lines']}
    Number of unique words: {len(unique_words)}
    ''')

wordcount('ex20.txt')