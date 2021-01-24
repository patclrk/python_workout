'''
Input: filename
Output: the final line of the file
'''

def get_final_line(filename):
    with open(filename) as f:
        return f.readlines()[-1]

print(get_final_line('ex18.txt'))

# book solution

# def get_final_line(filename):
#     final_line = ''
#     for current_line in open(filename):
#         final_line = current_line
#     return final_line

# print(get_final_line('ex18.txt'))