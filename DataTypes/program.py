#Data Types
"""
Python data types define what a value can represent and what operations are valid on it. A value’s type controls behavior: numbers can be added, strings can be sliced, dictionaries
map keys to values, and sets enforce uniqueness.
"""

"""
int
int stores whole numbers with arbitrary precision.
"""

x = 2
y = -42
z = 10**6

"""
float
float stores decimal numbers in binary floating-point format.
"""

price = 82.6
ratio = 2.0

#Floating-point values can have precision artifacts:
0.1 + 0.2   # 0.30000000000000004

"""
complex
complex stores numbers with real and imaginary parts.
"""
value = 2 + 4j
value.real   # 2.0
value.imag   # 4.0

"""
bool
bool has two values: True and False.
"""
is_ready = True
is_empty = False

#bool is a subclass of int:
isinstance(True, int)  # True
True + True            # 2

"""
Text Type (str)
Strings are immutable Unicode text.
"""
name = "Alice"
lang = "Python"

#You can index and slice strings, but not mutate characters in place:
s = "Python"
s[0]      # "P"
s[1:4]    # "yth"
# s[0] = "J"  # TypeError - strings are immutable

"""
Sequence Types
list (mutable)
Lists are ordered, allow duplicates, and can be modified.
"""
nums = [2, 4, 6]
nums.append(8)    # [2, 4, 6, 8]

"""
tuple (immutable)
Tuples are ordered and allow duplicates, but cannot be changed after creation.
"""
point = (2, 4)
# point[0] = 6  # TypeError

"""
range (lazy sequence of integers)
range represents arithmetic progressions efficiently.
"""
r = range(0, 8, 2)
list(r)   # [0, 2, 4, 6]

"""
Mapping Type (dict)
Dictionaries store key-value pairs.
"""
user = {"name": "Alice", "score": 82}
user["score"]      # 82
user["score"] = 84

#Keys must be hashable (e.g. str, int, tuples of hashables).

"""
Set Types
set (mutable)
Sets store unique, unordered elements.
"""
vals = {2, 4, 4, 6}
vals   # {2, 4, 6}