# python_workout
Exercises from the Python Workout book

## Lessons Learned
1. ### Reading from a binary file
    python expects valid UTF-8 Unicode strings. For binary files, read in chunks (like a socket):

    ```
    with open(filename, 'rb') as f:
        while True:
            one_chunk = f.read(1000)
            if not one_chunk:
                break
        print(f'This chunk contains {len(one_chunk)} bytes')
    ```
2. ### Dictionary comprehension
   ```
   return {
        filename: find_longest_word(os.path.join(dirname, filename))    <--- key, value
        for filename in os.listdir(dirname)                             <--- loop and filter
        if os.path.isfile(os.path.join(dirname, filename))
        }
   ```