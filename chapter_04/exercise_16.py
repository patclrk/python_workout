'''
Input: two dictionaries
Output: a dict that contains the difference between the two input dictionaries
If dictionaries are the same, return empty dictionary
'''

def dictdiff(*args):
    # error check args == 2
    result = {}
    d1 = args[0]
    d2 = args[1]

    for key, value in d1.items():
        if key not in d2 or d2.get(key) != value:
            result[key] = [d1.get(key),d2.get(key)]
    return result


d1 = {'a':1,'b':2,'c':3}
d2 = {'a':1,'b':2,'c':4}
print(dictdiff(d1,d2))

d3 = {'a':1,'b':2,'d':3}
d4 = {'a':1,'b':2,'c':4}
print(dictdiff(d3,d4))

d5 = {'a':1,'b':2,'c':3}
d6 = {'a':1,'b':2,'c':3}
print(dictdiff(d5,d6))