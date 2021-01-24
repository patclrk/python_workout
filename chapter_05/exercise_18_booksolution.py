from memory_profiler import profile
'''
Input: filename
Output: the final line of the file
'''
@profile
def get_final_line(filename):
    final_line = ''
    for current_line in open(filename):
        final_line = current_line
    return final_line

print(get_final_line('ex18.txt'))

# 2021-01-24 12:25:56 chapter_05 (main) $ sudo python3 -m memory_profiler exercise_18_booksolution.py 
# Filename: exercise_18_booksolution.py

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      6     15.4 MiB     15.4 MiB           1   @profile
#      7                                         def get_final_line(filename):
#      8     15.4 MiB      0.0 MiB           1       final_line = ''
#      9     15.4 MiB      0.0 MiB           4       for current_line in open(filename):
#     10     15.4 MiB      0.0 MiB           3           final_line = current_line
#     11     15.4 MiB      0.0 MiB           1       return final_line