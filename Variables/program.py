#Variables
# Variables store values in named references. Python is dynamically typed: 
# a variable can hold any type, and the type can change during execution. 
# Understanding assignment, unpacking, and scope is essential for writing correct code.

#A variable is created by assigning a value to a name. No explicit declaration is required.
x = 2
name = "Alice"
items = [2, 4, 6, 8]

# Naming rules: Names must start with a letter or underscore; the rest may be letters, digits, or underscores. Names are case-sensitive: count and Count are different.

# Reassignment: A variable can be reassigned to a new value of any type.

x = 2
x = "two"
x = [2, 4]

# Multiple Assignment
# Chained assignment: Several variables can be bound to the same value in one statement.

x = y = z = None

# All three names refer to the same object. 
# For immutable values (e.g. None, integers), this is safe. For mutable values (e.g. lists), 
# all names share the same object; mutating one affects all.

a = b = c = []
a.append(2)
# b and c also see [2]

#Parallel assignment: Assign different values to multiple variables in one line.

a, b, c = 2, 4, 6

# The right-hand side is evaluated first, then values are assigned left to right. 
# The number of names must match the number of values.

# Unpacking
# Tuple or list unpacking: Assign elements of a sequence to multiple variables.

data = ["Apple", 2, 4.2]
x, y, z = data
# x = "Apple", y = 2, z = 4.2

# isinstance()
# isinstance(obj, type) returns True if the object is an instance of the given type or of a subclass of that type. 
# It is the preferred way to check types before conversion or branching.

isinstance(2, int)       # True
isinstance(4.2, float)    # True
isinstance("hi", str)    # True
isinstance(2, (int, float))  # True - tuple of types

# Subclass handling: isinstance() returns True 
# for subclasses; type() checks only the exact type.

class Child(list):
    pass
 
c = Child()
type(c) == list       # False - exact type is Child
isinstance(c, list)   # True  - Child is a subclass of list

#Multiple types: Pass a tuple of types to check against any of them.

isinstance(2, (int, float))   # True
isinstance("hi", (int, float))  # False

"""
Global Variables and the global Keyword
Variables defined at module level are global. They are visible everywhere in the module. Reading a global 
variable inside a function does not require any special keyword.

Assignment creates a local: Assigning to a name inside a 
function creates a local variable by default, even if a global with the same name exists. 
The local shadows the global.
"""

x = 2
 
def set_local():
    x = 4  # local x; global x unchanged
    print(x)
 
set_local()  # 4
print(x)    # 2

"""
The global keyword: Use global name to assign to a global variable from
inside a function. Without it, assignment creates a local.
"""
x = y = z = None
data = ["Apple", 2, 4.2]
 
def assign_globals():
    global x, y, z
    x, y, z = data[0], data[1], data[2]
 
assign_globals()
# x == "Apple", y == 2, z == 4.2