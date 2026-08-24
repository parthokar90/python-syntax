# Functions
# Functions are reusable blocks of code that accept inputs, perform a task, and optionally return a result.

# Defining a function with parameters and default values
def calculate_total(price, tax_rate=0.05):
    """Calculates total price including tax."""
    total = price + (price * tax_rate)
    return total

# Calling the function
item1 = calculate_total(100)          # Uses default tax_rate (0.05)
item2 = calculate_total(100, 0.10)    # Overrides tax_rate

print(f"Item 1: ${item1}")  # Output: Item 1: $105.0
print(f"Item 2: ${item2}")  # Output: Item 2: $110.0

# When to Use Functions

# Repetitive Code: Whenever you find yourself writing the same code logic twice or more across your program.

# Complex Tasks: To break down a large, complicated problem into smaller, manageable sub-tasks.

# Modular Codebases: When building modules, packages, or libraries that expose specific utility features to other parts of your app.

# Why to Use Functions (Key Advantages)

# DRY Principle (Don't Repeat Yourself): Saves time and reduces code redundancy by centralizing shared logic into one place.

# Maintainability & Debugging: If a bug occurs in a calculation, you only need to fix it inside its specific function rather than updating code scattered everywhere.

# Readability & Scope Isolation: Replaces long, complex code blocks with descriptive function names (process_payment(), send_email()). Variables created inside a function are isolated from the main program scope, preventing accidental variable overwriting.