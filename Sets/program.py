"""
  A Python set is an unordered, mutable collection of unique elements written 
   with curly braces {}. Sets automatically eliminate duplicate values and support mathematical set
  operations like union, intersection, and difference.
 """

# Creating a set (duplicates are automatically removed)
fruits = {"apple", "banana", "apple", "cherry"}
print(fruits)  # Output: {'banana', 'apple', 'cherry'}

# Adding and removing elements
fruits.add("orange")
fruits.remove("banana")

# Mathematical set operations
set_a = {1, 2, 3, 4}
set_b = {3, 4, 5, 6}

print(set_a.union(set_b))        # Output: {1, 2, 3, 4, 5, 6}
print(set_a.intersection(set_b)) # Output: {3, 4}
print(set_a.difference(set_b))   # Output: {1, 2}


# When to Use Sets

# Removing Duplicates: When you have a list or dataset with duplicate values and need to extract only unique items.

# Membership Testing: When you frequently need to check if an item exists inside a collection (e.g., if item in my_set:).

# Venn Diagram Operations: When performing mathematical operations like finding common elements (intersection), combined elements (union), or unique differences between datasets.

# Why to Use Sets (Advantages over Lists)

# Fast Lookups: Membership testing in a set takes O(1) constant time on average, whereas searching inside a list takes O(n) linear time.

# Automatic Uniqueness: Sets prevent duplicate entries by design, saving you from writing manual filtering logic.
