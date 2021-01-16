'''
Combines two sequences to return a single sequence
or sums the values contained in a single sequence
'''
def mysum(*args):
    if not args:
        return args
    output = args[0]
    for arg in args[1:]:
        output += arg
    return output
        

if __name__ == "__main__":
    print(mysum([1,2,3],[4,5,6]))
    print(mysum('abc','def'))
    print(mysum(1,2,3))
