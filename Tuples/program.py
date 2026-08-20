# A Python tuple is an ordered, immutable (unchangeable) sequence of elements written with parentheses ().
# Once a tuple is created, its items cannot be modified, added, or removed.

# Creating a tuple
coordinates = (23.8103, 90.4125)

# Accessing elements by index
print(coordinates[0])  # Output: 23.8103

# Returning multiple values from a function using a tuple
def get_user_details():
    name = "Alice"
    role = "Developer"
    return name, role  # Returns ('Alice', 'Developer')

# Tuple unpacking
user_name, user_role = get_user_details()
print(user_name)  # Output: Alice


# When to Use Tuples

# Constant Data: When working with values that should never change while the program is running (e.g., GPS coordinates, RGB color codes like (255, 0, 0), or database configurations).

# Heterogeneous Records: When grouping related values of different types that represent a single record (e.g., ("Product A", 19.99, 50) representing product name, price, and stock count).

# Multiple Return Values: When a function needs to return more than one value at a time.

# Dictionary Keys: When you need a composite key for a dictionary, since dictionary keys must be immutable.

# Why to Use Tuples (Advantages over Lists)

# Data Integrity: Immutability ensures that data remains write-protected against accidental modifications across your codebase.

# Better Performance: Tuples are faster to iterate through and use less memory than lists because Python allocates a static block of memory for them.

# Hashability: Tuples are hashable, meaning they can be stored inside set objects or used as dict keys, whereas lists cannot.