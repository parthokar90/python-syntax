# Strings
"""
Strings are immutable sequences of Unicode characters. They support concatenation,
formatting, modification, search, slicing, and type-checking methods. Mastery of these operations is essential 
for text processing and interview problems.
"""

# Creating Strings
"""
Strings are created with single, double, or triple quotes. Triple quotes allow multiline strings.
"""
s = "hello"
s = 'world'
s = """line two
line four
line six"""

# Slicing and Indexing
"""
Indexing
Indices start at 0. Negative indices count from the end: -1 is the last character.
"""
s = "Python"
s[0]    # "P"
s[-1]   # "n"
s[2]    # "t"

# Out of range: s[20] raises IndexError.

# Slicing
"""
s[start:stop:step] - elements from start up to but not including stop, with optional step. Omitted values use 
defaults: start=0, stop=len(s), step=1.
"""
s = "Python"
s[:2]       # "Py"
s[2:]       # "thon"
s[-4:-2]    # "th"
s[::-1]     # "nohtyP"

# reversed() and join()
# reversed(s) returns a reverse iterator. Combine with join() to build a reversed string.

"".join(reversed("Python"))  # "nohtyP"

# len()
# len(s) returns the number of characters in the string.

len("Python")  # 6

# Concatenation
"""
The + Operator
+ joins two strings into a new string. Both operands must be strings.
"""
"Hello" + "World"        # "HelloWorld"
"2" + "4" + "6"          # "246"

# Type error: "2" + 4 raises TypeError. Convert numbers with str(): "2" + str(4) → "24".

# The join() Method
"""
sep.join(iterable) joins an iterable of strings with the separator. The separator is the string calling join();
the iterable provides the parts.
"""
"-".join(["a", "b", "c"])   # "a-b-c"
"".join(["2", "4", "6"])    # "246"
" | ".join(["x", "y", "z"]) # "x | y | z"

"""
Order: sep.join(parts) produces parts[0] + sep + parts[1] + sep + .... 
The separator appears only between elements.
"""

# Formatting
# F-Strings
# F-strings embed expressions in {} within a string prefixed with f or F.
name = "Alice"
score = 86.8
f"Name: {name}, Score: {score}"  # "Name: Alice, Score: 86.8"

# Format specifiers: Use : followed by a format spec. :.2f formats a float to two decimal places.

x = 2.444
f"{x:.2f}"   # "2.44"

# Expressions in braces: Any valid expression can appear inside {}.

x, y = 4, 6
f"{x}*{y}={x*y}"  # "4*6=24"

# The format() Method
"""
template.format(*args, **kwargs) fills placeholders in the template. Placeholders use {};
positional and keyword arguments fill them.
"""
"{} and {}".format("a", "b")           # "a and b"
"{0} and {1}".format("x", "y")          # "x and y"
"{name} is {age}".format(name="Alice", age=24)  # "Alice is 24"