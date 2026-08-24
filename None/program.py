# None
# None is Python’s null value. It is the only instance of NoneType and represents the absence of a value, an empty result, or an uninitialized state.

# 1. Default variable assignment before getting data
user_response = None

# 2. Function without an explicit return statement returns None
def log_message(msg):
    print(f"LOG: {msg}")

result = log_message("System boot")
print(result)  # Output: None

# 3. Checking for None using identity operator 'is'
if user_response is None:
    print("No response received yet.")


# When to Use None

# Default Function Arguments: When an optional parameter should default to an empty or uninitialized state (especially for mutable types like lists or dicts to avoid bugs: def add_item(item, list=None):).

# Placeholder for Missing Data: Representing optional database fields, missing API response values, or uninitialized variables.

# Return Value for Intentional Failure: Returning None from a search function when an item isn't found in a dataset.

# Why to Use None (Key Advantages)

# Explicit Over Implicit: Python prefers being explicit. Using None clearly signals "this variable exists, but it deliberately has no value right now", rather than leaving it undefined.

# Safer Checks (is None): Checking if val is None: checks the exact identity in memory. This prevents bugs where falsy values like 0, "" (empty string), False, or [] (empty list) might otherwise be confused with a missing value.