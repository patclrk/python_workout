"""
String manipulation: if character is a vowel, preface with 'ub'
Returns a string
"""
def ubbi_dubbi(word):
    result = []
    for letter in word:
        if letter in 'aeiuo':
            result.append(f'ub{letter}')
        else:
            result.append(f'{letter}')
    return ''.join(result)

if __name__ == "__main__":
    print(ubbi_dubbi('translation'))