# In Python, range() is a built-in function that generates an immutable sequence of numbers. It is commonly used inside for loops to repeat an action a specific number of times without storing all the numbers in memory at once.

# Syntax: range(start, stop, step)

# start (optional): The starting number (default is 0).

# stop (required): The number where the sequence stops (not included).

# step (optional): The step value or increment (default is 1).

# Example

# 1. Single argument: range(stop) - generates numbers from 0 to 4
for i in range(5):
    print(i, end=" ")  # Output: 0 1 2 3 4
print()

# 2. Two arguments: range(start, stop) - generates numbers from 2 to 6
for i in range(2, 7):
    print(i, end=" ")  # Output: 2 3 4 5 6
print()

# 3. Three arguments: range(start, stop, step) - increments by 2
for i in range(1, 10, 2):
    print(i, end=" ")  # Output: 1 3 5 7 9
print()

# 4. Counting backwards with a negative step
for i in range(5, 0, -1):
    print(i, end=" ")  # Output: 5 4 3 2 1


# When to Use range()
# Fixed Number of Iterations: When you want to run a loop a specific number of times (e.g., range(100) to execute code 100 times).

# Indexing Sequences: When you need the index number while looping through a list or string (e.g., for i in range(len(my_list))).

# Step Sequences: When you need to generate numbers at custom intervals, such as skipping every second item or counting backward.

# Why to Use range() (Key Advantages)

# Memory Efficient: range() creates a range object that generates numbers on demand (lazy evaluation) rather than storing all the numbers in memory. Generating range(1000000) takes the same tiny amount of memory as range(5).

# Fast and Lightweight: Because it does not construct a full list in RAM, it runs faster and optimizes performance during large loop cycles.