"""
Type Conversion
Type conversion (casting) transforms a value from one type to another. Explicit conversion uses built-ins such as str(), int(), float(), bool(), list(), tuple(), and set(). 
Understanding conversion rules and edge cases avoids subtle bugs.
"""
"""
str() Conversion
From any type: Produces a string representation of the value. Every built-in type supports this.
"""
str(66)      # "66"
str(82.6)    # "82.6"
str(True)    # "True"
str([2, 4])  # "[2, 4]"
str(None)    # "None"

"""
int() Conversion
From string: Parses a string as an integer. Leading and trailing whitespace 
is ignored. The string must represent a valid integer literal.
"""
int("222")    # 222
int("  42  ") # 42
int("-8")     # -8

"""
float() Conversion
From string: Parses a string as a floating-point number.
Accepts integers and decimals.
"""
float("82.6")   # 82.6
float("42")     # 42.0
float("-2.4")   # -2.4
float("  6.8 ") # 6.8

"""
bool() Conversion
Truthiness: bool(x) returns False for “falsy” values and True otherwise. 
Falsy values include None, 0, 0.0, "", [], (), {}, and set().
"""
bool(0)       # False
bool(1)       # True
bool("")      # False
bool("hi")    # True
bool([])      # False
bool([2, 4])  # True
bool(None)    # False

"""
list() Conversion
From iterable: Builds a new list from any iterable. Order is preserved.
"""
list("abc")       # ['a', 'b', 'c']
list((1, 2, 3))   # [1, 2, 3]
list(range(3))    # [0, 1, 2]
list({2, 4, 6})   # [2, 4, 6] - order not guaranteed

"""
tuple() Conversion
From iterable: Builds a new tuple from any iterable.
Immutable and hashable (if elements are hashable).
"""
tuple([1, 2, 3])   # (1, 2, 3)
tuple("ab")        # ('a', 'b')
tuple(range(2))    # (0, 1)
tuple({2, 4})      # (2, 4) - order not guaranteed

"""
set() Conversion
From iterable: Builds a set of unique elements.
Duplicates are removed; order is not preserved.
"""
set([1, 2, 2, 3])   # {1, 2, 3}
set("hello")        # {'h', 'e', 'l', 'o'}
set((1, 1, 2))      # {1, 2}


#Exercise pattern: Given DATA = ["222", 82.6, 66], cast each element to its natural type:
DATA = ["222", 82.6, 66]
 
def cast():
    return (int(DATA[0]), float(DATA[1]), str(DATA[2]))
# (222, 82.6, "66")

"""
Implicit vs Explicit Conversion
Explicit: Using int(), float(), str(), bool(), list(), tuple(), set() - clear and controlled.

Implicit: Python converts automatically in some contexts (e.g. 2 + 4.0 → 6.0). 
Relying on implicit conversion can 
obscure intent; explicit casting is often clearer.
"""