from memory_profiler import profile
'''
Input: filename
Output: the final line of the file
'''
@profile
def get_final_line(filename):
    with open(filename) as f:
        return f.readlines()[-1]

print(get_final_line('ex18.txt'))

# 2021-01-24 12:21:56 chapter_05 (main) $ sudo python3 -m memory_profiler exercise_18.py 
# Filename: exercise_18.py

# Line #    Mem usage    Increment  Occurences   Line Contents
# ============================================================
#      6     15.3 MiB     15.3 MiB           1   @profile
#      7                                         def get_final_line(filename):
#      8     15.3 MiB      0.0 MiB           1       with open(filename) as f:
#      9     15.3 MiB      0.0 MiB           1           return f.readlines()[-1]