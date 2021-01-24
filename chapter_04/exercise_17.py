'''
Input: list of integers
Output: integer representing unique number of integers in input list
'''

def how_many_different_numbers(number_list):
    return len(set(number_list))

l1 = [1, 1, 2, 3, 4, 4, 4, 3]

print(how_many_different_numbers(l1))

# book solution
# def how_many_different_numbers(numbers):
#     unique_numbers = set(numbers)
#     return len(unique_numbers)