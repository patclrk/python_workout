'''
Return the first an last item from an iterable
'''
def firstlast(x):
    result = x[:1]
    result += x[-1:]
    return result

if __name__ == "__main__":
    print(firstlast('abcd'))
    print(firstlast((1,2,3,4)))
    print(firstlast([5,6,7,8,9]))
    #print(firstlast({'a':1,'b':2,'c':3}))


# book solution
# def firstlast(sequence):
    #return sequence[1:] + sequence[-1:]