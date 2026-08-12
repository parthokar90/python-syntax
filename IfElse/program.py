#If and Else
"""
Conditionals decide which code runs from whether something
is true or false. Python uses if, elif, and else; one condition is
checked and one branch runs. Truthiness and short-circuit behavior cause most
of the gotchas, so they’re worth getting straight.
"""

if condition:
    # block runs only when condition is true
    statement_1
    statement_2

#if and else
#else runs a different block when the condition is false. Exactly one of the two blocks runs.
if condition:
    # when condition is true
    block_a
else:
    # when condition is false
    block_b

if, elif, and else
"""
More than two outcomes? Use elif (else-if). Python evaluates the conditions in order; the first one that’s true runs its block and the rest are skipped. else, if present, runs only
when every if and elif condition is false.
"""
if condition_1:
    block_1
elif condition_2:
    block_2
elif condition_3:
    block_3
else:
    block_else

#At most one block runs. When it’s done, execution continues after the whole chain.
status_code = 4
if status_code == 2:
    label = "pending"
elif status_code == 4:
    label = "active"
elif status_code == 6:
    label = "done"
else:
    label = "archived"

"""
Order matters. If condition_1 is true, condition_2 and condition_3 are never evaluated, so put the most specific or most likely cases 
first when that affects correctness or performance.
"""

"""
Nested Conditionals
if and elif blocks can contain more if–elif–else chains. Indentation defines which if an else belongs to;
else attaches to the nearest if at the same indentation level.
"""
x = 6
y = 4
if x > 4:
    if y > 2:
        print("both large")
    else:
        print("x large, y not")
else:
    print("x not large")
# Output: both large

#Conditional Expression (Ternary)

"""
Pick one of two values with a conditional expression: value_when_true if
condition else value_when_false. It’s an expression, so it fits anywhere a value
goes: assignments, arguments, return values.
"""
x = 6
label = "even" if x % 2 == 0 else "odd"   # "even"

