# Hello World
# A minimal Python program prints output to the console. This lesson focuses on print() basics so you can run and verify your first scripts quickly.

# The print() Function
# print() sends text to standard output. It accepts one or more arguments and converts them to strings before writing.

print("Hello, World!")

# Multiple arguments: Arguments are separated by spaces by default. The sep parameter controls the separator.
print("Hello", "World", "!")

print("2", "4", "6", sep="-")

# End parameter: The end parameter controls what is printed after the last argument. The default is a newline (\n).
print("Line one", end="")
print("Line two")

# Multiple values in one line:
name = "Alice"
score = 82
print("Name:", name, "Score:", score)

# Custom separator for compact output:
print("2", "4", "6", sep="-")

#Colon: A colon (:) starts a block. The block must be indented.
if True:
    print("indented block")
    
#Comments: Lines starting with # are comments and are ignored.
# This is a comment
print("Hello")  # inline comment