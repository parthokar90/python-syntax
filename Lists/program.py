# In Python, a List is a built-in data type used to store a collection of items in a single variable. Lists are one of the most versatile and frequently used data structures in Python.

# Key Characteristics of Python Lists
# Ordered: Items have a defined order, and that order will not change unless explicitly modified.

# Mutable: You can change, add, or remove items after the list has been created.

# Allows Duplicates: Lists can have items with the same value.

# Heterogeneous: A single list can contain different data types (e.g., integers, strings, booleans, or even other lists).

Python List Examples
1. Creating a List
You create a list by placing items inside square brackets [], separated by commas:

# A list of strings
fruits = ["apple", "banana", "cherry"]

# A list of mixed data types
mixed_list = [42, "hello", 3.14, True]

print(fruits)

# 2. Accessing Items (Indexing)
# List items are indexed starting from 0. You can also use negative indexing to start from the end (-1 is the last item).

fruits = ["apple", "banana", "cherry", "date"]

print(fruits[0])   # Output: apple (First item)
print(fruits[-1])  # Output: date (Last item)

# 3. Modifying Items
# Since lists are mutable, you can change an item by referring to its index:

fruits = ["apple", "banana", "cherry"]
fruits[1] = "blueberry"

print(fruits)  # Output: ['apple', 'blueberry', 'cherry']

# 4. Adding Items

append(): Adds an item to the end of the list.

insert(): Adds an item at a specific index.

numbers = [1, 2, 3]

numbers.append(4)        # Adds 4 to the end -> [1, 2, 3, 4]
numbers.insert(1, 1.5)   # Inserts 1.5 at index 1 -> [1, 1.5, 2, 3, 4]

print(numbers)

# 5. Removing Items

remove(): Removes the first occurrence of a specific value.

pop(): Removes and returns an item at a given index (or the last item if no index is given).

colors = ["red", "green", "blue", "yellow"]

colors.remove("green")  # Removes "green"
colors.pop(0)           # Removes item at index 0 ("red")

print(colors)  # Output: ['blue', 'yellow']

# 6. Looping Through a List
# You can iterate through list items using a for loop:

animals = ["cat", "dog", "rabbit"]

for animal in animals:
    print(animal)

# 7. List Slicing
# Extract a sub-section of a list using the [start:stop] syntax:

numbers = [0, 10, 20, 30, 40, 50]

# Extract items from index 1 up to (but not including) index 4
subset = numbers[1:4]

print(subset)  # Output: [10, 20, 30]

