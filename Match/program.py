# Match (Structural Pattern Matching)
"""
Structural pattern matching picks one branch by matching a value 
against patterns. Python’s match (3.10+) often replaces long if–elif–else 
chains when you’re branching on “one of these exact values” or on the shape of 
the value (e.g. how long a list is or which keys a dict has). The main gotchas 
come from how patterns are evaluated 
and how names get bound; those are worth getting straight.
"""

#Why match?
"""
When every branch depends on the same value (a status code, a command name,
 the shape of some structure), if–elif–else works but gets noisy. match–case puts
  the value in one place and turns each branch into a pattern: it either matches or it
   doesn’t. The first case that matches runs; nothing falls through to the next. Match
    really shines when you care about more than equality
 (e.g. “a list of two elements” or “a dict with key 'x'”).
 """

# Basic Syntax
"""
You write match followed by a subject (the value you’re inspecting), then one or more case blocks. Each case has a pattern and, optionally, a guard. Python tries the patterns in order;
the first one that matches runs, and the rest are skipped.
"""
match subject:
    case pattern_1:
        block_1
    case pattern_2:
        block_2
    case _:
        block_default
"""
Colons after match and after each case are required. The block under a case is whatever’s
indented under it. The _ in the last case is a wildcard:
it matches anything and is commonly used as the default.
"""
status = 4
match status:
    case 2:
        label = "pending"
    case 4:
        label = "active"
    case 6:
        label = "done"
    case _:
        label = "unknown"
 
print(label) # active