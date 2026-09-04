# A Python for loop is used to iterate over a sequence (such as a list, tuple, 
# dictionary, set, or string) or a range of numbers, executing a block of code once for each item in that sequence.

# Iterating over a list
fruits = ["apple", "banana", "cherry"]
for fruit in fruits:
    print(fruit)

# Using range() to loop a fixed number of times
for i in range(3):
    print(f"Count: {i}")  # Output: Count: 0, Count: 1, Count: 2

# Iterating over dictionary key-value pairs
user = {"name": "Alice", "role": "Developer"}

for key, value in user.items():
    print(f"{key}: {value}")


#  When to Use for Loops

# Sequence Processing: When you need to perform an operation on every item in a list, set, dictionary, or string.

# Fixed Number of Repetitions: When you know in advance how many times a code block should run (using range()).

# Filtering or Transforming Data: When building a new collection by filtering or modifying elements from an existing sequence.

# Why to Use for Loops (Advantages over while Loops)

# Prevents Infinite Loops: A for loop automatically stops when it reaches the end of the sequence, reducing the risk of accidental infinite loops.

# Clean and Readable: You do not need to manually create, increment, or manage index variables (e.g., i = 0 and i += 1). Python handles the iterator state automatically.   